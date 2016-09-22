# NLP100本ノック
# 
# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

print("行数:")
N = int(input())

f = open("hightemp.txt", "r", encoding="utf-8")
lines = f.readlines()

for i in range(N):
    print(lines[-N+i])