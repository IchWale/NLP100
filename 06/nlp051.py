# NLP100本ノック
# 
# 51. 単語の切り出し
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
# ただし，文の終端では空行を出力せよ．

import re
import sys

def split_space(text):
    word_list = text.split()
    for word in word_list:
        print(word)

#nlp050
pattern = re.compile(r"([\.;:?!])\s([A-Z])")
with open("nlp.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line != "\n":
            sentences = re.sub(pattern, r"\1\n\2", line)
            split_space(sentences)
