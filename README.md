# 团码 / thmy

团码是一个独立的 Rime 输入方案，仓库名为 `thmy`。

这个仓库作为从头重构的干净起点：只保留团码方案本身、当前可用词典产物、生成所需数据和最小脚本，不包含原 `xii`、`xii_uat` 方案及旧仓库部署流程。

## 文件结构

- `THMY.txt`: 团码 fcitx-table 风格源表
- `data/phrase_source.txt`: 重构期词条来源
- `rime/thmy.schema.yaml`: Rime 方案配置
- `rime/thmy.dict.yaml`: Rime 词典
- `rime/thmy_jj.schema.yaml`: 团码-jj 整句实验方案
- `rime/thmy_jj.dict.yaml`: 团码-jj 整句词典
- `android/`: Trime 用方案、词典和 Dvorak 键盘主题
- `windows/`: Weasel 用方案和词典
- `data/`: 字频、多音字读音频率、词条来源和自定义词条
- `scripts/`: 离线构建脚本

## 构建

构建脚本只更新本仓库内文件，不会部署到系统输入法目录。

```sh
sh scripts/build.sh
```

生成结果：

- `THMY.txt`
- `rime/thmy.dict.yaml`
- `rime/thmy_jj.dict.yaml`
- `android/thmy.dict.yaml`
- `android/thmy_jj.dict.yaml`
- `windows/thmy.dict.yaml`
- `windows/thmy_jj.dict.yaml`

## macOS 部署

部署到鼠须管：

```sh
scripts/deploy-macos-rime.sh
```

脚本会先构建，再复制 `thmy.schema.yaml` 和 `thmy.dict.yaml` 到
`~/Library/Rime/`，最后编译 `thmy` 和 `thmy_jj` 两个方案，避免其他旧方案的
全量部署错误。

部署过程中会用旋转进度条显示长步骤：

```text
==> 构建码表和词典 /
==> 构建码表和词典 -
==> 构建码表和词典 \
==> 构建码表和词典 |
==> 构建码表和词典 完成
```

默认会收起构建和编译的详细日志，只显示阶段状态。若需要排查构建细节，可开启
详细输出：

```sh
THMY_DEPLOY_VERBOSE=1 scripts/deploy-macos-rime.sh
```

## 手动安装

macOS 鼠须管可复制这些文件到 `~/Library/Rime/` 后重新部署：

- `rime/thmy.schema.yaml`
- `rime/thmy.dict.yaml`
- `rime/thmy_jj.schema.yaml`
- `rime/thmy_jj.dict.yaml`
- `rime/default.custom.yaml`

Windows 小狼毫可使用：

- `windows/thmy.schema.yaml`
- `windows/thmy.dict.yaml`
- `windows/thmy_jj.schema.yaml`
- `windows/thmy_jj.dict.yaml`
- `windows/default.custom.yaml`

Android 同文可使用：

- `android/thmy.schema.yaml`
- `android/thmy.dict.yaml`
- `android/thmy_jj.schema.yaml`
- `android/thmy_jj.dict.yaml`
- `android/default.custom.yaml`
- `android/thmy_dvorak.trime.yaml`

## 团码-jj

`thmy_jj` 是独立整句实验方案，显示名为 `团码-jj`。主方案 `thmy`
仍然保留表码手感；整句、句中补辅码先在 `thmy_jj` 中验证。

- 纯音整句按双键音节连续输入，例如 `wumz` 可出“我们”
- 单字辅码词典内部写作 `音码;辅码`，例如“的”是 `de;d`
- 直接补一位辅码可输入 `ded`，句中补辅码可用 `de[d`
- 桌面端可用 `Control+1..7` 跳到第几个音节插入 `[`，再输入辅码
- 桌面端可用 `Shift+A..Z` 给当前音节补对应辅码并跳到下一音节

## 设计状态

- 当前重构版以音码为主；辅助码源 `data/thmy_aux.tsv` 由 `scripts/generate_thmy_aux.py` 生成
- 辅助码设计以 Dvorak 手感优先：优先减少同指、大跨度同指和同手连续，同时兼顾左右手、手指负载与常用字分流
- 单字读音主源来自 `data/hanzi_reading_frequency_baishuang_8105.tsv`
- 常用异读可以补入读音表，但备用读音应使用较低权重，避免同一个字同时抢占多个音码首候选
- 每个首码生成一个一简字，低频副读音不抢一键码位
- 单字保留一简和两码音码
- 词条保留四码压缩词码，并额外生成完整纯双拼音码
- `;` 作为辅助码分隔符，`/` 作为笔画反查入口

## 多音字和首候选

单字可以保留多个有效读音，但首候选尽量避免浪费在同一个字上。规则是：

- 主读音可以保持较高权重，作为该字的主要打法
- 备用读音保留可打，但降低权重，不抢其他常用字的首候选
- 构建后应检查“同一个字占多个音码首候选”的数量，理想值为 `0`

例如“谁”同时保留 `shei` 和 `shui`：

```text
up  谁
uk  水、睡、税、谁
```

也就是 `up` 仍是“谁”的主打法；`uk` 可以找到“谁”，但首候选留给“水”。

后续重构建议优先从 `scripts/build_thmy.py` 开始。
