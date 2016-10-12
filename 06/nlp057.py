# NLP100本ノック
# 
# 57. 係り受け解析
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

import xml.etree.ElementTree as ET
from graphviz import Digraph


def dep_to_graph(elem, s_id):
    """
    Stanford Core NLPの解析結果xmlから係り受け関係のグラフを作成する関数
    args:
        elem: ETオブジェクト, Stanford Core NLPの解析結果xmlのETパーザオブジェクト
        s_id: int, グラフ化するセンテンスid
    """
    g = Digraph(format="png")

    sentence = elem.findall(".//sentence")[s_id - 1]
    coll_dep = sentence.find("dependencies[@type='collapsed-dependencies']")
    dep_list = coll_dep.findall("dep")
    for dep in dep_list:
        gov_idx = dep.find("governor").get("idx")
        gov_text = dep.find("governor").text
        dep_idx = dep.find("dependent").get("idx")
        dep_text = dep.find("dependent").text
        # ROOTは出力しない
        if gov_text == "ROOT":
            continue
        # グラフにノードとエッジを追加
        g.node(gov_idx, gov_text)
        g.node(dep_idx, dep_text)
        g.edge(dep_idx, gov_idx)

    print(g)
    g.render("nlp057_result")


if __name__ == '__main__':
    tree = ET.parse("nlp.txt.xml")
    elem = tree.getroot()
    print("sentences id: ") #標準入力でグラフ化するsentence idを指定
    s_id = int(input())
    dep_to_graph(elem, s_id)
