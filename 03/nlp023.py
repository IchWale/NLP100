# NLP100本ノック
# 
# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import re


f = open("jawiki-britain.txt", "r", encoding="utf-8")
pattern = re.compile(r"(={2,})([^=]+)(={2,})")

for line in f:
    match = re.search(pattern, line)
    if match:
        print(match.group())
        print("セクション名:{}, レベル:{}".format(match.group(2), len(match.group(1))-1))

