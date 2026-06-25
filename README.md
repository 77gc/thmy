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
- `rime/thmy_code_lookup.tsv`: 团码-ym 字词反查索引，供 `//` 反查码值使用
- `rime/thmy_jj_code_lookup.tsv`: 团码-jj 字词反查索引，供 `//` 反查码值使用
- `rime/rime.lua`、`rime/lua/thmy_code_lookup.lua`: `//` 反查逻辑
- `android/`: Trime 用方案、词典和 Dvorak 键盘主题
- `windows/`: Weasel 用方案和词典
- `data/`: 字频、多音字读音频率、词条来源和自定义词条
- `scripts/`: 离线构建脚本

## 构建

构建脚本只更新本仓库内文件，不会部署到系统输入法目录。当前默认只构建
`团码-ym`，先把主方案定稳；`团码-jj` 暂时冻结，需要时显式开启。

```sh
sh scripts/build.sh
```

生成结果：

- `THMY.txt`
- `rime/thmy.dict.yaml`
- `rime/thmy_code_lookup.tsv`
- `android/thmy.dict.yaml`
- `android/thmy_code_lookup.tsv`
- `windows/thmy.dict.yaml`
- `windows/thmy_code_lookup.tsv`

如需同时刷新 `团码-jj`：

```sh
THMY_WITH_JJ=1 sh scripts/build.sh
```

会额外生成：

- `rime/thmy_jj.dict.yaml`
- `rime/thmy_jj_code_lookup.tsv`
- `android/thmy_jj.dict.yaml`
- `android/thmy_jj_code_lookup.tsv`
- `windows/thmy_jj.dict.yaml`
- `windows/thmy_jj_code_lookup.tsv`

## macOS 部署

部署到鼠须管：

```sh
scripts/deploy-macos-rime.sh
```

脚本会先构建，再复制 `thmy.schema.yaml` 和 `thmy.dict.yaml` 到
`~/Library/Rime/`，最后只编译 `thmy`，避免每次都刷新较慢的 `thmy_jj`。

如需连 `团码-jj` 一起构建和编译：

```sh
THMY_WITH_JJ=1 scripts/deploy-macos-rime.sh
```

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
- `rime/thmy_code_lookup.tsv`
- `rime/thmy_jj_code_lookup.tsv`
- `rime/rime.lua`
- `rime/lua/thmy_code_lookup.lua`
- `rime/default.custom.yaml`

Windows 小狼毫可使用：

- `windows/thmy.schema.yaml`
- `windows/thmy.dict.yaml`
- `windows/thmy_jj.schema.yaml`
- `windows/thmy_jj.dict.yaml`
- `windows/thmy_code_lookup.tsv`
- `windows/thmy_jj_code_lookup.tsv`
- `windows/rime.lua`
- `windows/lua/thmy_code_lookup.lua`
- `windows/default.custom.yaml`

Android 同文可使用：

- `android/thmy.schema.yaml`
- `android/thmy.dict.yaml`
- `android/thmy_jj.schema.yaml`
- `android/thmy_jj.dict.yaml`
- `android/thmy_code_lookup.tsv`
- `android/thmy_jj_code_lookup.tsv`
- `android/rime.lua`
- `android/lua/thmy_code_lookup.lua`
- `android/default.custom.yaml`
- `android/thmy_dvorak.trime.yaml`

## 码值反查

`thmy` 和 `thmy_jj` 都支持 `//` 反查最近一次上屏的字词码值。

反查规则固定为“各表查各表”：

- `团码-ym` 只查 `rime/thmy.dict.yaml` 生成的 `thmy_code_lookup.tsv`
- `团码-jj` 只查 `rime/thmy_jj.dict.yaml` 生成的 `thmy_jj_code_lookup.tsv`
- 后续新增方案或新增码表时，也必须单独生成自己的反查索引，不把其他方案的码混入当前方案

用法：

- 先正常输入并上屏一个字或词，再输入 `//`
- 候选正文显示码值，候选注释显示被反查的字词
- 反查会标出前 4 位候选的选键：首候选不加后缀，第 2/3/4 候选分别加 `'`、`,`、`.`
- 如果最近上屏的是一个词，会优先显示整词码；同时补一个“末字”的单字码
- 若平台允许在输入串中粘贴中文，也可以用 `//字词` 直接查指定内容

注意：输入法通常不能稳定读取当前 App 光标前已有正文，所以这里记录的是“最近一次通过本方案上屏的内容”，不是任意编辑器里光标前的历史文本。

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
- 辅助码重码按手机候选键优化：允许同码候选落在左上三键加空格的 4 键选择区内，超过 4 候选才显著惩罚
- 单字读音主源来自 `data/hanzi_reading_frequency_baishuang_8105.tsv`
- 正确读音都应保留可打；罕见副读音使用低权重，避免同一个字同时抢占多个音码首候选
- 若罕见副读音的带辅码条目挤出 4 键快选区，只给该“副读音打法”追加第二辅码；源辅码表和主读音打法不变
- 每个首码自动生成最多 4 个一简候选，低频副读音不抢一键首候选
- 一键首选已经覆盖的单字，会在对应双键全码里让位给同码第二候选，避免首选重复浪费
- 单字保留一简和所有可映射的两码音码；主读音和常用副读音正常排序，罕见副读音低权重靠后
- 词条保留四码压缩词码，并额外生成完整纯双拼音码
- `;` 作为辅助码分隔符，`/` 作为符号入口

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

## 辅助码循环优化

正式方案固定双拼音码，只训练和生成辅码。音码参与辅码评分，但不作为优化变量，
这样可以保留现有双拼肌肉记忆，并避免词码和整句方案跟随音码整体漂移。

`scripts/optimize_thmy_aux.py` 可以循环搜索辅码生成参数，流程是：

```text
生成辅码 -> 统计手感和重码 -> 综合评分 -> 保留最优参数和辅码表
```

快速烟测：

```bash
python3 scripts/optimize_thmy_aux.py \
  --rounds 5 \
  --char-limit 1200 \
  --candidate-limit 48 \
  --report /tmp/thmy_aux_optimize_1200.md
```

正式搜索：

```bash
python3 scripts/optimize_thmy_aux.py \
  --rounds 100 \
  --candidate-limit 96 \
  --report data/thmy_aux_optimize_report.md \
  --output /tmp/thmy_aux_best.tsv
```

围绕当前方案精修可使用模拟退火：

```bash
python3 scripts/optimize_thmy_aux.py \
  --method anneal \
  --rounds 500 \
  --candidate-limit 96 \
  --seed 20260625 \
  --report data/thmy_aux_optimize_report_anneal500_seed20260625.md
```

报告会列出最佳 `same_code_slot_weight`、`same_code_overflow_weight`、
`phrase_code_collision_weight` 和负载权重。评分中也包含靠后的同指长跨键惩罚：
同键重复、临近和斜向邻键不算，只有同指跨两行的不同键才计入，例如 `yx`、
`fb`、`px`。确认方案后，应把最佳参数同步到 `scripts/generate_thmy_aux.py`
的常量，再运行 `sh scripts/build.sh` 生成正式码表。

`scripts/optimize_thmy_sound_aux.py` 是音码也参与变化的实验脚本，只用于评估
“重排音码 + 重训辅码”的理论空间，不参与正式构建。当前 100 轮实验报告见
`data/thmy_sound_aux_optimize_report.md`：最佳仍为现有音码不变，说明正式方案
继续固定音码、只优化辅码。
