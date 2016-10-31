# NLP100本ノック
# 
# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

word_list=[]

with open("hightemp.txt", "r", encoding="utf-8") as f:
    for line in f:
        word_list.append(line.split()[0])

freq_dic = {}
for word in word_list:
    freq_dic[word] = freq_dic.get(word, 0) + 1

freq_list = list(freq_dic.items())
freq_list.sort(key=lambda i: i[1], reverse=True)

print(freq_list)
