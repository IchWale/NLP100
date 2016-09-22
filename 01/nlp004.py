# NLP100本ノック
# 
# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
# 連想配列（辞書型もしくはマップ型）を作成せよ．

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace(".", "")
word_list = s.split()

dic = {}
l = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for cnt, word in enumerate(word_list):
    if cnt+1 in l:
        dic.update({word[0]:cnt+1})
    else:
        dic.update({word[0:2]:cnt+1})

print(dic)

# {'H': 1, 'B': 5, 'S': 16, 'Li': 3, 'Ar': 18, 
# 'O': 8, 'He': 2, 'Mi': 12, 'Na': 11, 'Cl': 17, 
# 'C': 6, 'Ne': 10, 'Be': 4, 'F': 9, 'Si': 14, 
# 'P': 15, 'Al': 13, 'N': 7, 'K': 19, 'Ca': 20}