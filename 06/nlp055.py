# NLP100本ノック
# 
# 55. 固有表現抽出
# 入力文中の人名をすべて抜き出せ.

import re

pattern_token = re.compile(r"<token(.+?)</token>", re.DOTALL)
pattern_word = re.compile(r"<word>(.+?)</word>")
pattern_ner = re.compile(r"<NER>(.+?)</NER>")

with open("nlp.txt.xml", "r", encoding="utf-8") as f:
    text = f.read()
    tokens = re.findall(pattern_token, text)
    for token in tokens:
        ner = re.search(pattern_ner, token).group(1)
        if ner == "PERSON":
            print(re.search(pattern_word, token).group(1))
