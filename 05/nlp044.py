# NLP100本ノック
# 
# 44. 係り受け木の可視化
# 与えられた文の係り受け木を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい

# pythonからGraphvizを利用するパッケージはいくつかあるみたい.
# 問題文中で言っているpydotよりもgraphvizの方が公式ドキュメントがしっかりしてたので,
# こちらを使うことにする.
# Graphvizをpythonから利用するパッケージgraphviz ややこしい.
# http://graphviz.readthedocs.io/en/latest/index.html

# $ sudo apt-get install graphviz
# $ pip install graphviz

from graphviz import Digraph
from nlp041 import read_cabocha
from nlp042_2 import set_chunk_dep

def dep_to_graph(chunk_dep_list):
    """
    chunkの係り関係のタプルからグラフを作成する関数
    """
    g = Digraph(format="png")
    g.attr("node", fontname="TakaoPGothic")
    for chunk_dep in chunk_dep_list:
        g.edge(chunk_dep[0].get_surf(), 
            chunk_dep[1].get_surf())
    print(g)
    g.render("nlp044")


if __name__ == '__main__':
    all_sentences = read_cabocha("neko.txt.cabocha")
    chunk_dep_list = set_chunk_dep(all_sentences[6])
    dep_to_graph(chunk_dep_list)
