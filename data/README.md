# Data Sources

## `hanzi_frequency_junda.tsv`

Simplified Chinese character frequency ranks used to order same-code
single-character candidates in `thmy`.

- Source: <https://github.com/ruddfawcett/hanziDB.csv>
- Upstream notes: based on Jun Da's Modern Chinese Character Frequency List
- Upstream license: MIT

Only the rank and character columns are kept here.

## `hanzi_frequency_baishuang_8105.tsv`

Simplified Chinese character frequency ranks extracted from
`cn_dicts/8105.dict.yaml` in `gaboolic/rime-shuangpin-fuzhuma`.

- Source: <https://github.com/gaboolic/rime-shuangpin-fuzhuma>
- Upstream dictionary: `cn_dicts/8105.dict.yaml`
- Upstream notes: the 8105 dictionary says its frequency data comes from a
  2.5-billion-character BLCU corpus.
- Upstream license in that repository: MIT

Columns are `rank<TAB>character<TAB>source_weight`.

## `hanzi_reading_frequency_baishuang_8105.tsv`

Simplified Chinese character-reading weights extracted from
`cn_dicts/8105.dict.yaml` in `gaboolic/rime-shuangpin-fuzhuma`.

This keeps per-reading weights so `thmy` one-key abbreviations can avoid
rare alternate readings taking prime keys, for example `区/ou` should not take
the `o` key from `哦/o`.

Columns are `character<TAB>sit_initial_key<TAB>source_weight<TAB>pinyin`.

## `yehe_sound_shape.tsv`

Yehe sound-shape single-character entries used as the primary single-character
source for `thmy`.

- Source: <https://github.com/qqj-jj/yehe>
- Upstream file: `野鹤.txt`
- Extracted scope: no-prefix sound-shape entries only
- Excluded scopes: `!` component composition codes and `/` stroke codes

Columns are `code<TAB>character`.
