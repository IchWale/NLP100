# NLP100本ノック
# 
# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

f_col1 = open("col1.txt", "r", encoding="utf-8")
f_col2 = open("col2.txt", "r", encoding="utf-8")
f_col3 = open("col3.txt", "w", encoding="utf-8")

with f_col1, f_col2, f_col3:
    for line1, line2 in zip(f_col1, f_col2):
        line1 = line1.replace("\n", "")
        f_col3.write(line1 + "\t" + line2)
