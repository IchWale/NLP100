# NLP100本ノック
# 
# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

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
X = [i for i in range(1, 11)]
Y = [i[1] for i in freq_list_desc[:10]]
plt.bar(X,Y, align="center")
plt.xticks(X, [i[0] for i in freq_list_desc[:10]], fontproperties=fp)
plt.title("出現頻度上位10単語", fontproperties=fp)
plt.xlabel("単語",fontproperties=fp)
plt.ylabel("出現回数",fontproperties=fp)

plt.show()
