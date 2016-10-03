# NLP100本ノック
# 
# 50. 文区切り
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
# 入力された文書を1行1文の形式で出力せよ．

# 改行も文の区切りとみなす

import re
import sys

pattern = re.compile(r"([\.;:?!])\s([A-Z])")
with open("nlp.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line != "\n":
            sentences = re.sub(pattern, r"\1\n\2", line)
            # print(sentences),
            sys.stdout.write(sentences)