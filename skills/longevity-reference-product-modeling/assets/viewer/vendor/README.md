# Bundled viewer dependency / 查看器第三方依赖

This directory contains third-party code, not original LONGEVIS code. It is excluded from the repository's MIT licensing claim; retain all copyright notices and license files when redistributing it. / 本目录为第三方代码，不属于 LONGEVIS 原创部分；再分发时请完整保留原版权声明和许可证文件。

- Package / 软件包: `@google/model-viewer` **4.0.0**
- Unmodified bundle / 未修改文件: `model-viewer.min.js`
- Source / 来源: <https://unpkg.com/@google/model-viewer@4.0.0/dist/model-viewer.min.js>
- SHA-256: `774edda21e1be2a0934e460ca5943af1fe3f88da130a9f98bd6a9d611576cacf`
- Main license / 主许可证: Apache-2.0, `LICENSE.model-viewer`.
- Embedded dependencies / 内嵌依赖: Lit (BSD-3-Clause, `LICENSE.lit`), Three.js r169 (MIT, `LICENSE.threejs`), fflate 0.8.2 (MIT, `LICENSE.fflate`). Original `@license` comments remain in the bundle. / 打包文件中的原始许可证注释已保留。

License texts were retrieved from the respective upstream repositories / 许可证文本来自各自上游：

- `LICENSE.lit`: <https://raw.githubusercontent.com/lit/lit/main/LICENSE> (SHA-256 `c94b94b40b85a5083dea825ae844b1cedb40dd425685362c135e143265dd6cd4`)

- `LICENSE.threejs`: <https://raw.githubusercontent.com/mrdoob/three.js/r169/LICENSE> (SHA-256 `4c40a1ef62450b857c3b2aaf294936304cd552d965fbcd9d32d4c5bcf4ba4454`)

- `LICENSE.fflate`: <https://raw.githubusercontent.com/101arrowz/fflate/v0.8.2/LICENSE> (SHA-256 `805f6cb28bb8b6d3a0badd83c93bccd9671fa01a3b4b92b7042b0743325ac243`)

Reference API / API 文档: <https://modelviewer.dev/docs/index.html>

The runtime imports this local module; no remote CDN script is required for ordinary GLB files with embedded textures. / 普通内嵌贴图 GLB 在运行时使用本地模块，无需远程 CDN 脚本。

Draco, Meshopt, and KTX2 models may require extra decoder/transcoder assets; these are not included. / Draco、Meshopt、KTX2 等压缩模型可能需要额外解码依赖，本包未包含。

Version 4.0.0 is retained for compatibility with this tested template. This is not a claim that it is the latest version. / 本模板为保持已测兼容性保留 4.0.0，不表示其为最新版本。
