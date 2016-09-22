# NLP100本ノック
# 
# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ.

from nlp030 import read_mecab


file_name = "neko.txt.mecab"
all_sentences = read_mecab(file_name)

for sentence in all_sentences:
    noun_list = []
    for cnt, morph in enumerate(sentence):
        if morph["pos"] == "名詞":
            noun_list.append(morph["surface"])
            if cnt == len(sentence)-1 and len(noun_list) > 1:
                print("".join(noun_list))
                noun_list = []
        elif len(noun_list) > 1:
            print("".join(noun_list))
            noun_list = []
        else:
            noun_list = []
