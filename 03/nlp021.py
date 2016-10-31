# NLP100本ノック
# 
# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

with open("jawiki-britain.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "Category:" in line:
            print(line)
