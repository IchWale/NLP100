# NLP100本ノック
# 
# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

# File:で始まってるやつを抜き出せばよいのかな?

import re

pattern = re.compile(r"File:([^|]+)\|")

with open("jawiki-britain.txt", "r", encoding="utf-8") as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            print(match.group(1))
