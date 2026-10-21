---
name: longevis-product-appearance-calibration
description: Use when existing 3D product geometry is close to a reference but materials or lighting differ, native renders and web viewers disagree, or appearance changes must carry across product variants.
---

# 产品材质与光感校准

[English](SKILL.en.md)

以照片或已确认效果图为目标，校准已有三维模型的材质与受光，同时保留几何、动画与查看器功能。参考图表达外观意图，不能自动证明准确色值、尺寸或工程参数；未提供的反面只作合理推断。

## 工作流程

1. **找出真正加载的资产。** 追踪源模型、目录派生、运行时配置、专属查看器与下载别名，记录实际 URL、哈希、型号与配置。先核对监听端口、页面标题和服务目录，避免同名文件夹或服务误导。备份将修改的模型、查看器和配置；保留缺项、未加载与未验证状态。本公开包不含任何私有产品目录适配器。
2. **固定比较条件。** 先确认目标参考版本。保留原模型，在相同机位、环境与曝光下比较轮廓、材质、灯光与色彩管理。先调通有代表性的资产，再按用户范围推广到其余变体。详见[外观判断与显示链路](references/appearance-and-viewers.md)。
3. **按表面分类校准。** 涂层、裸金属、玻璃、木材、织物、橡胶和 UI 分开处理；核对纹理真实尺度、方向、UV、法线、AO 与粗糙度。一个产品试配的颜色或数值不能当作其他产品的测量参数。
4. **用光照产生受光。** 发光表面、真实光源和环境反射分别处理。不要把整片木材染红或增加 emissive 代替局部照明。新增光源要接入已有开关；关灯时恢复基材。检查正面、侧面、内饰、地面与接触阴影，不承诺单张参考可支持任意视角的一比一还原。
5. **保留功能契约。** 保留几何、原有节点、门轴、动画时间、屏幕贴图、标识与材质变体。显式的 JSON 材质、贴图或灯光修改可用本包脚本；UV 或几何修改使用原生模型流程，并重新验证功能。先读[配方与验证](references/recipes-and-validation.md)。
6. **沿最终显示链路验收。** 查加载后的材质改写、透射玻璃与 alpha、灯光开关、环境图、曝光和缓存指纹。原生渲染与网页截图分别验证。逐配置实际加载，检查多视角、近景、已有门/内部/拆解/配色/屏幕操作、下载和 PNG 导出。同步运行副本后复查入口与哈希。

## 工具与交付

需要 Python 3，脚本只用标准库；不含 Blender、网页查看器、产品模型或纹理。渲染、建模和查看器操作需使用当前环境提供的工具，不假定某个 MCP 或私有工作台存在。

```bash
python3 scripts/apply_glb_recipe.py original.glb recipe.json calibrated.glb --report report.json
python3 scripts/test_apply_glb_recipe.py
```

交付模型、配方、前后对照、逐配置验收表与回退来源。表中至少包含型号/配置、实际 URL、旧新哈希、配方版本、已验证操作、缺项与运行副本状态。交代验证环境、参考限制与未验证项。

导出成功、脚本通过或两张样片不能证明全量产品升级完成。不要用参考照片平面或 AI 精修图代替承诺的可交互三维交付。
