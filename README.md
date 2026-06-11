# 团码 / thmy

团码是一个独立的 Rime 输入方案，仓库名为 `thmy`。

这个仓库作为从头重构的干净起点：只保留团码方案本身、当前可用词典产物、生成所需数据和最小脚本，不包含原 `xii`、`xii_uat` 方案及旧仓库部署流程。

## 文件结构

- `THMY.txt`: 团码 fcitx-table 风格源表
- `data/phrase_source.txt`: 重构期词条来源
- `rime/thmy.schema.yaml`: Rime 方案配置
- `rime/thmy.dict.yaml`: Rime 词典
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
- `android/thmy.dict.yaml`
- `windows/thmy.dict.yaml`

## macOS 部署

部署到鼠须管：

```sh
scripts/deploy-macos-rime.sh
```

脚本会先构建，再复制 `thmy.schema.yaml` 和 `thmy.dict.yaml` 到
`~/Library/Rime/`，最后只编译 `thmy` 方案，避免其他旧方案的全量部署错误。

## 手动安装

macOS 鼠须管可复制这些文件到 `~/Library/Rime/` 后重新部署：

- `rime/thmy.schema.yaml`
- `rime/thmy.dict.yaml`
- `rime/default.custom.yaml`

Windows 小狼毫可使用：

- `windows/thmy.schema.yaml`
- `windows/thmy.dict.yaml`
- `windows/default.custom.yaml`

Android 同文可使用：

- `android/thmy.schema.yaml`
- `android/thmy.dict.yaml`
- `android/default.custom.yaml`
- `android/thmy_dvorak.trime.yaml`

## 设计状态

- 当前重构版先只保留音码，形码暂留空，后续接入团码自己的形码表
- 单字读音主源来自 `data/hanzi_reading_frequency_baishuang_8105.tsv`
- 每个首码生成一个一简字，低频副读音不抢一键码位
- 单字保留一简和两码音码
- 词条保留四码压缩词码，并额外生成完整纯双拼音码
- `;` 作为辅助码分隔符，`/` 作为笔画反查入口

后续重构建议优先从 `scripts/build_thmy.py` 开始。
