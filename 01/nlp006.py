# NLP100本ノック
# 
# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．


from nlp005 import ngram

text1 = "paraparaparadise"
text2 = "paragraph"

X = set(ngram(text1, 2, "char"))
Y = set(ngram(text2, 2, "char"))

print("Xの集合: {}".format(X))
print("Yの集合: {}".format(Y))
print("XとYの和集合: {}".format(X | Y))
print("XとYの積集合: {}".format(X & Y))
print("XとYの差集合: {}".format(X - Y))
print("'se' in X: {}".format(('s', 'e') in X))
print("'se' in Y: {}".format(('s', 'e') in Y))
