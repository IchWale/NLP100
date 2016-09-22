# NLP100本ノック
# 
# 38. ヒストグラム
# 単語の出現頻度のヒストグラム
# (横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの)
# を描け.

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
data = [i[1] for i in freq_list_desc[200:1001]]
plt.hist(data, bins=30)
plt.title("出現頻度ヒストグラム", fontproperties=fp)
plt.xlabel("出現頻度",fontproperties=fp)
plt.ylabel("単語の種類数",fontproperties=fp)

plt.show()
