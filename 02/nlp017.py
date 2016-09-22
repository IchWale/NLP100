# NLP100本ノック
# 
# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

f = open("hightemp.txt", "r", encoding="utf-8")
word_set = set()

for line in f:
    word_set.add(line.split()[0])

print(word_set)