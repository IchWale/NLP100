# NLP100本ノック
# 
# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．

from nlp030 import read_mecab


file_name = "neko.txt.mecab"
all_sentences = read_mecab(file_name)

for sentence in all_sentences:
    for morph in sentence:
        if morph["pos1"] == "サ変接続":
            print(morph["surface"])
