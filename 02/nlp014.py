# NLP100本ノック
# 
# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

print("行数:")
N = int(input())

with open("hightemp.txt", "r", encoding="utf-8") as f:
    for i in range(N):
        print(f.readline())