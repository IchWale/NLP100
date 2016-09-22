# NLP100本ノック
# 
# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．

from nlp030 import read_mecab


file_name = "neko.txt.mecab"
all_sentences = read_mecab(file_name)

for sentence in all_sentences:
    for morph in sentence:
        if morph["pos"] == "動詞":
            print(morph["base"])
