# NLP100本ノック
# 
# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re


f = open("jawiki-britain.txt", "r", encoding="utf-8")

for line in f:
    if "Category:" in line:
        match = re.search(r"Category:([^]]+)]", line)
        print(match.group(1))
