# 脚本接口

需要 Python 3.10+；Blender 脚本面向 Blender 4.2+/5.x，具体版本与 GPU 后端须在使用者环境中验证。图片打包另外需要 Pillow。渲染脚本在 Blender Python 内运行，其余脚本在普通 Python 中运行。优先发现环境已有依赖，不默认下载软件或修改全局设置。

## 准备任务

将 `assets/render-job.example.json` 和 `assets/studio_recipe.py` 复制到项目工作目录。把示例 JSON 重命名为 `render-job.json`，修改源模型路径、版本、部件选择器与镜头。示例机位针对 2200×1800×2000 mm 舱体，其他产品须重新构图。

所有相对路径以 JSON 所在目录为基准，不以当前 shell 工作目录为基准。不要直接在已安装 skill 的 assets 目录里产生项目文件。

主要字段：

| 字段 | 用途 |
|---|---|
| `variants[].id` / `label` | ASCII 文件标识 / 可含中文的显示名称 |
| `source` / `version` | 原生 `.blend` 路径 / 版本标签 |
| `dependencies` | 未打包贴图等影响渲染的文件；全局和方案均可声明 |
| `recipe` | 可选本地 Python 配方，提供 `configure(scene, job, variant, shot)` |
| `shots[].size` | 输出像素，横图和竖图分别定义 |
| `camera` | `location`、`target`；`lens` 或 `ortho_scale` |
| `shots[].variants` | 可选，该镜头适用的方案 ID 列表 |
| `shots[].samples` | 可选的单镜头正式采样上限 |
| `shots[].frame` | 动画帧；默认第 1 帧 |
| `render` | 采样、反弹、自适应阈值、线程、曝光、视图变换 |

配方相关字段：`hide.names/prefixes/contains/collections` 控制渲染隐藏；精确对象和集合名称缺失会报错，前缀和包含匹配须自行检查命中结果。`object_rotations_degrees` 为指定对象的 XYZ 绝对欧拉角。`material_overrides` 按精确材料名和 Principled BSDF 输入名覆盖。`studio.scale` 缩放棚拍布光及能量，不改变产品或机位。

示例透射覆盖仅在确认材料后填写：

```json
{"material_overrides":{"Clear PC":{"Alpha":1,"Transmission Weight":1,"Roughness":0.022}}}
```

配方是本地可执行 Python，渲染指纹会包含配方文件；配方如依赖其他文件，也加入 `dependencies`。脚本不会修改源 `.blend`，不要在自定义配方中调用保存原文件的操作。

## 渲染

下面用 `product_skill_dir` 表示该 skill 的安装目录；`blender` 表示本机找到的 Blender 可执行文件。macOS 常见路径为 `/Applications/Blender.app/Contents/MacOS/Blender`。

```bash
blender --background --factory-startup --python-exit-code 1 --python "$product_skill_dir/scripts/render_batch.py" -- /project/render-job.json --proof --variants A --shots 01_hero,05_interior
blender --background --factory-startup --python-exit-code 1 --python "$product_skill_dir/scripts/render_batch.py" -- /project/render-job.json --variants A --shots 01_hero
blender --background --factory-startup --python-exit-code 1 --python "$product_skill_dir/scripts/render_batch.py" -- /project/render-job.json --resume
```

`--device AUTO` 默认发现可用 GPU，否则用 CPU；可明确选择 `CPU`、`METAL`、`OPTIX`、`CUDA`、`HIP`、`ONEAPI`。明确指定的后端不可用时会停止，不悄悄切换。

`--python-exit-code 1` 让脚本异常返回失败状态，避免把 Blender 默认的退出状态误判为成功。

每张输出到 `raw/<variant>/<shot>.png`，预览输出到 `proofs/`。`.records/` 保存完成状态、机位、耗时、输入指纹和 PNG 哈希。新图先写独立临时文件，完整验证后再替换，避免中断后误用旧图。

`manifest-final.json` 或 `manifest-proof.json` 汇总与当前配置匹配的完成记录。只渲染部分镜头时 `complete` 为 false；缺失、损坏或配置变化的图会在 `--resume` 时重渲染。变动某一机位只使该机位的记录失效；修改全局棚拍配方会使全部失效。

同一个任务输出目录只运行一个批次进程，避免完成清单被并发写入。停止时只管理本次启动的渲染进程；保留已完成记录，下次续跑。不要通过修改记录把中断的图标成完成。

脚本不会自动判断两模型的局部几何等价。共同内饰复用需要另行验证并记录复用来源；未经验证时独立渲染。

## 图片打包

```bash
python3 "$product_skill_dir/scripts/package_images.py" /project/renders/brochure/manifest-final.json --out /project/delivery/brochure
```

拒绝未完成清单、预览清单、重复机位或哈希不一致的图。从只读原图生成 `PNG/`、`JPG/`、`overview/`、`image-manifest.json`、`usage.txt` 与 `brochure-images.zip`，不改写 raw 图。ZIP 通过 CRC 检查后才替换目标包。

默认添加 sRGB ICC、300 dpi 元数据；不放大原图。`--dpi` 可指定排版密度，`--font` 可指定支持标签文字的字体。系统没有合适的中文字体时给出明确错误，不输出方框字。

## 源文件快照

```bash
python3 "$product_skill_dir/scripts/model_snapshot.py" create /project/baseline.json --root /project/variants/A/v2
python3 "$product_skill_dir/scripts/model_snapshot.py" verify /project/baseline.json
```

创建时选择模型、源码和贴图常用后缀，可用 `--suffixes` 调整。验证默认要求原有文件未修改/未缺失，同时报告新增文件；`--strict` 也将新增文件视为差异。`--root` 支持在复制或迁移目录后验证。快照记录已存在时要求换名称，以保留基线。
