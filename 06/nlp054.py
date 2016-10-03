# NLP100本ノック
# 
# 54. 品詞タグ付け
# Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

# xmltodictというパッケージを使ってみる

import re

pattern_token = re.compile(r"<token(.+?)</token>", re.DOTALL)
pattern_word = re.compile(r"<word>(.+?)</word>")
pattern_lemma = re.compile(r"<lemma>(.+?)</lemma>")
pattern_pos = re.compile(r"<POS>(.+?)</POS>")

with open("nlp.txt.xml", "r", encoding="utf-8") as f:
    text = f.read()
    tokens = re.findall(pattern_token, text)
    for token in tokens:
        word = re.search(pattern_word, token).group(1)
        lemma = re.search(pattern_lemma, token).group(1)
        pos = re.search(pattern_pos, token).group(1)
        print("{}, {}, {}".format(word, lemma, pos))

# xmltodictというパッケージを使って見る単語、練磨,瀕死をタブ区切り形式で出力してい
