# NLP100本ノック
# 
# 52. ステミング
# 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
# 単語と語幹をタブ区切り形式で出力せよ． 
# Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

# NLTKのstemパッケージを使用
# http://www.nltk.org/api/nltk.stem.html

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
with open("nlp051_result.txt", "r", encoding="utf-8") as f:
    for line in f:
        word = line.strip()
        stem_word = ps.stem(word)
        print("{}\t{}".format(word, stem_word))
