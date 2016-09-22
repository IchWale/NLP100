# NLP100本ノック
# 
# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．


import matplotlib.pyplot as plt
from nlp030 import read_mecab
from nlp036 import word_freq

# 日本語フォント読み込み
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'/usr/local/share/fonts/TakaoPGothic.ttf', size=10)

# nlp036の関数から頻度取得
file_name = "neko.txt.mecab"
all_sentences = read_mecab(file_name)
freq_list_desc = word_freq(all_sentences)

# グラフ描写
# すべてのデータだと値の範囲が広すぎてうまく表示されない
# data = [i[1] for i in freq_list_desc]
# 頻度上位200~1000を表示するとそれなりに見えるグラフになる
X = [i for i in range(len(freq_list_desc))]
Y = [i[1] for i in freq_list_desc]
plt.plot(X,Y)
plt.xscale("log") # y軸を対数目盛に
plt.yscale("log") # y軸を対数目盛に
plt.title("Zipfの法則", fontproperties=fp)
plt.xlabel("単語の出現頻度順位",fontproperties=fp)
plt.ylabel("出現頻度",fontproperties=fp)

plt.show()

