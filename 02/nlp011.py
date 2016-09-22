# NLP100本ノック
# 
# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

f = open("hightemp.txt", "r", encoding="utf-8")
text = f.read().replace("\t", " ")
print(text)