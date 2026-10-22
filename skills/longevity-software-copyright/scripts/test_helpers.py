"""Synthetic checks: source continuity, provenance and text length; no private fixtures."""
import json
from pathlib import Path
import tempfile
import unittest

from source_materials import inventory, extract
from check_function_text import count_cjk


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "project"
        self.root.mkdir()

    def prepare(self, content, filename="main.py"):
        (self.root / filename).write_text(content, encoding="utf-8")
        listing = self.base / "files.txt"
        listing.write_text(filename + "\n", encoding="utf-8")
        manifest_path = self.base / "manifest.json"
        inventory(self.root, listing, manifest_path)
        return manifest_path

    def material(self, manifest):
        out = self.base / "material"
        result = extract(self.root, manifest, out, "Example control software", "V1.0")
        pages = json.loads((out / "pages.json").read_text())
        return result, pages, (out / "selected-source.txt").read_text()

    def test_short_source_is_all_without_padding(self):
        manifest = self.prepare("\n# 原始注释\nprint('你好')\n\nreturn_value = 1\n")
        result, pages, text = self.material(manifest)
        self.assertEqual(result["mode"], "all")
        self.assertEqual(result["selected_lines"], 3)
        self.assertEqual(text, "# 原始注释\nprint('你好')\nreturn_value = 1\n")
        self.assertEqual([r["line"] for r in pages["pages"][0]["rows"]], [2, 3, 5])
        self.assertEqual(result["scope_status"], "unreviewed")

    def test_long_source_is_exact_front_and_back(self):
        manifest = self.prepare("".join(f"value_{i} = {i}\n" for i in range(1, 3208)))
        result, pages, text = self.material(manifest)
        lines = text.splitlines()
        self.assertEqual(result["mode"], "front-back")
        self.assertEqual(len(pages["pages"]), 60)
        self.assertTrue(all(len(p["rows"]) == 50 for p in pages["pages"]))
        self.assertEqual(lines[:1500], [f"value_{i} = {i}" for i in range(1, 1501)])
        self.assertEqual(lines[1500:], [f"value_{i} = {i}" for i in range(1708, 3208)])
        self.assertEqual(pages["pages"][-1]["rows"][-1]["line"], 3207)

    def test_exact_sixty_pages_not_duplicated(self):
        result, pages, text = self.material(self.prepare("x\n" * 3000))
        self.assertEqual(result["mode"], "all")
        self.assertEqual(len(text.splitlines()), 3000)
        self.assertEqual(len({r["global_line"] for p in pages["pages"] for r in p["rows"]}), 3000)

    def test_unicode_string_characters_do_not_become_source_newlines(self):
        content = 'message = "before\u0085middle\u2028then\u2029after"\n'
        manifest = self.prepare(content)
        data = json.loads(manifest.read_text())
        result, _, text = self.material(manifest)
        self.assertEqual(data["files"][0]["physical_lines"], 1)
        self.assertEqual(result["selected_lines"], 1)
        self.assertEqual(text, content)

    def test_changed_source_rejected_before_output_created(self):
        manifest = self.prepare("x = 1\n")
        (self.root / "main.py").write_text("x = 2\n")
        with self.assertRaisesRegex(ValueError, "changed"):
            self.material(manifest)
        self.assertFalse((self.base / "material").exists())

    def test_native_container_is_inventory_only(self):
        manifest = self.prepare("native graphical project", "project.MCP")
        data = json.loads(manifest.read_text())
        self.assertEqual(data["files"][0]["kind"], "native_or_binary")
        with self.assertRaisesRegex(ValueError, "export"):
            self.material(manifest)

    def test_explicit_file_order_and_no_automatic_vendor_inclusion(self):
        (self.root / "z.kt").write_text("last\n")
        (self.root / "a.kt").write_text("first\n")
        (self.root / "vendor.kt").write_text("unselected\n")
        listing = self.base / "files.txt"
        listing.write_text("z.kt\na.kt\n")
        manifest = self.base / "manifest.json"
        data = inventory(self.root, listing, manifest)
        result, _, text = self.material(manifest)
        self.assertEqual([f["path"] for f in data["files"]], ["z.kt", "a.kt"])
        self.assertEqual(text, "last\nfirst\n")
        self.assertEqual(result["source_files"], 2)

    def test_path_escape_duplicate_and_symlink_rejected(self):
        (self.base / "outside.py").write_text("secret\n")
        listing = self.base / "files.txt"
        for entries in ["../outside.py\n", "main.py\nmain.py\n"]:
            (self.root / "main.py").write_text("x\n")
            listing.write_text(entries)
            with self.assertRaises(ValueError):
                inventory(self.root, listing, self.base / "manifest.json")
        (self.root / "linked.py").symlink_to(self.base / "outside.py")
        listing.write_text("linked.py\n")
        with self.assertRaises(ValueError):
            inventory(self.root, listing, self.base / "manifest.json")

    def test_invalid_encoding_not_silently_replaced(self):
        (self.root / "main.py").write_bytes(b"\xff\xfe")
        listing = self.base / "files.txt"
        listing.write_text("main.py\n")
        with self.assertRaises(UnicodeError):
            inventory(self.root, listing, self.base / "manifest.json")

    def test_alias_duplicate_rejected_in_inventory(self):
        (self.root / "main.py").write_text("x\n")
        listing = self.base / "files.txt"
        listing.write_text("main.py\n./main.py\n")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            inventory(self.root, listing, self.base / "manifest.json")

    def test_existing_output_not_overwritten(self):
        manifest = self.prepare("x = 1\n")
        self.material(manifest)
        with self.assertRaises(FileExistsError):
            self.material(manifest)


class TextTests(unittest.TestCase):
    def test_counts_han_including_extensions_not_latin_or_punctuation(self):
        self.assertEqual(count_cjk("系统功能ABC 123，。\U00020000"), 5)

    def test_five_hundred_chinese_characters(self):
        self.assertEqual(count_cjk("功" * 499 + "能abc123"), 500)
        self.assertEqual(count_cjk("功" * 499 + "abc123"), 499)


if __name__ == "__main__":
    unittest.main()
