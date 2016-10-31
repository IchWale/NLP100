# NLP100本ノック
# 
# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

print("何分割:")
N = int(input())

with open("hightemp.txt", "r", encoding="utf-8") as f
    lines = f.readlines()

n = len(lines) // N
a = len(lines) % N
 
# 割り切れないときどうするか指定がないので適当
if n < 1:
    print("無理")
else:
    for i in range(N):
        if i < N-1:
            new_lines = lines[i*n:i*n+n]
        elif i == N-1:
            new_lines = lines[i*n:i*n+n+a]
        print("".join(new_lines))
        print("-----------------------------------------")