# NLP100本ノック
# 
# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

# ,と.の除去
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(",", "").replace(".", "")

# 正規表現なら
# import re
# s = re.sub("[,.]", "", s)

word_list = s.split(" ")
l = []

for i in word_list:
    l.append(len(i))

print(l)