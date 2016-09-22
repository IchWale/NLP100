# NLP100本ノック
# 
# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ.

from nlp030 import read_mecab


file_name = "neko.txt.mecab"
all_sentences = read_mecab(file_name)

for sentence in all_sentences:
    if len(sentence) < 3:
        continue
    for i in range(len(sentence)-2):
        if sentence[i]["pos"] == sentence[i+2]["pos"] == "名詞":
            if sentence[i+1]["surface"] == "の":
                l = [s["surface"] for s in sentence[i:i+3]]
                print("".join(l))
