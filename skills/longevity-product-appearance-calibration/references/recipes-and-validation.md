# 配方与验证

[English](recipes-and-validation.en.md)

## 适用边界与命令

`apply_glb_recipe.py` 用于几何不变的显式外观修改。需要 Python 3，无第三方依赖。输入为 GLB 2.0，至多一个内嵌 buffer，不支持外部 buffer URI 或额外未知 chunk。先确认输入有效且外部图像依赖可解析；本工具并非完整 glTF 验证器，也不执行图像解码。

它不决定美感，不自动生成 UV，不减面，不处理压缩或高级扩展的语义，不替代视觉验收。只对已理解且目标查看器支持的材质/贴图/灯光字段应用配方；修改材质并不确保材质变体扩展中的所有替代材质同步改变。

从不可变备份生成单独输出：

```bash
python3 scripts/apply_glb_recipe.py original.glb recipe.json calibrated.glb --report report.json
```

输出已存在时拒绝。仅在确认可替换该输出后使用 `--overwrite`；不要把源文件作为输出。报告路径与模型、源文件和配方路径分开，避免报告覆盖其他文件。对配方、图像文件与来源的读取仅使用可信本地文件，不下载资源、不执行配方代码。

## 配方示例

下列名称和数值均为格式示例；不是任何产品的实测参数。`textures/wood-normal.png` 必须由操作者提供真实可用的 PNG；纹理并未随包提供。

```json
{
  "id": "example-calibration-r1",
  "note": "Identify the approved reference and reason for calibration",
  "textures": {
    "wood_normal": {"file": "textures/wood-normal.png", "mimeType": "image/png"}
  },
  "materials": {
    "Exact material name": {
      "remove": ["alphaMode"],
      "set": {
        "pbrMetallicRoughness": {"metallicFactor": 0, "roughnessFactor": 0.42},
        "normalTexture": {"index": "wood_normal", "scale": 0.3}
      }
    }
  },
  "lights": [{
    "name": "Example lamp", "type": "point",
    "color": [1, 0.1, 0.05], "intensity": 0.65,
    "range": 2.3, "translation": [-0.4, 1.7, 0],
    "group": "interior", "controlMaterial": "Exact emitter material name"
  }]
}
```

- `id` 为必填配方版本。对已经标记同一 id 的模型再次运行时，工具原样复制，不重复添加灯光和贴图，也不重新执行修改。更改配方内容时更换 id，或从原始备份重新生成。仅 id 相同不能证明内容相同。
- `source_sha256` 可选，填写原始文件完整 SHA-256；幂等重跑核对模型记录的原始来源哈希。
- `materials` 以精确名称选择材质。未知名称拒绝；重名默认拒绝，只有顶层 `match_all_material_names: true` 才修改全部匹配项，报告给出索引。
- `set` 对字典递归合并，对其他值替换；`remove` 以点分隔路径删除字段。需改变整个嵌套对象时先删除再设置，避免残留旧字段。
- 纹理路径相对配方；PNG 默认 MIME 为 `image/png`，JPEG 需显式设 `image/jpeg`。操作者负责核对图像真实格式、可解码性和 UV。颜色图按 sRGB，normal/ORM 按非颜色数据读取。ORM 通道是 R=occlusion、G=roughness、B=metallic；入口为 `pbrMetallicRoughness.metallicRoughnessTexture`，不是 `roughnessTexture`。
- 字符串纹理索引可引用本配方新增的纹理名；已有纹理使用有效整数索引。未解析名称或越界索引拒绝。需要的 sampler 可在每张纹理的 `sampler` 对象中指定。
- `lights` 添加 `KHR_lights_punctual` 灯和场景节点；`translation`、可选 `rotation` 放在节点中。按实际资产单位与渲染器确定光强、范围和位置。`group`、`controlMaterial` 只生成 node extras；没有自动开关集成。其他光源字段按 glTF lights 格式填写，工具不做完整语义检查。

## 验证与回退

脚本在写入前检查 meshes/accessors/animations/skins 声明、原节点和原 BIN 前缀不变，新增图像附加在后。它不证明 UV、灯位、门运动视觉或最终查看器正确。先运行结构测试，再在实际浏览器和原生渲染中检查。

```bash
python3 scripts/test_apply_glb_recipe.py
```

随包测试使用自建三角形、合成门动画和微型 PNG，检查二进制及几何/动画保持、贴图/灯光新增、幂等、哈希不匹配、未知/重名材质、未解析贴图、外部 buffer、已有输出与报告覆盖源文件的拒绝。没有真实产品资产，未声称完整生产视觉验证。

逐配置记录：型号、配置、实际 URL、旧新 SHA、配方、前后图、已验证操作、缺项和运行副本状态。保留原模型、查看器与配置备份；回退时同步恢复模型、查看器、缓存指纹及索引。两种显示链路、全部授权配置与功能分别记录状态，不能以少量截图代替全量验收。
