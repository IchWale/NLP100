# NLP100本ノック
# 
# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

f = open("hightemp.txt", "r", encoding="utf-8")
f_col1 = open("col1.txt", "w", encoding="utf-8")
f_col2 = open("col2.txt", "w", encoding="utf-8")

with f, f_col1, f_col2:
    for line in f:
        f_col1.write(line.split()[0] + "\n")
        f_col2.write(line.split()[1] + "\n")
