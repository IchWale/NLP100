# NLP100本ノック
# 
# 58. タプルの抽出
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
# 「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
# ただし，主語，述語，目的語の定義は以下を参考にせよ．

# 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
# 主語: 述語からnsubj関係にある子（dependent）
# 目的語: 述語からdobj関係にある子（dependent）

import xml.etree.ElementTree as ET


def extract_tuple(elem):
    """
    Stanford Core NLPの解析結果xmlから主語述語目的語の係り受け関係を出力する関数
    args:
        elem: ETオブジェクト, Stanford Core NLPの解析結果xmlのETパーザオブジェクト
    """
    print("{:4}\t{:15}\t{:15}\t{:15}".format("s_id", "nsubj", "sub", "dobj"))

    for sentence in elem.find(".//sentences"):
        coll_dep = sentence.find("dependencies[@type='collapsed-dependencies']")
        dep_list = coll_dep.findall("dep")
        dep_dic = {}

        for dep in dep_list:
            gov_idx = dep.find("governor").get("idx")
            gov_text = dep.find("governor").text
            dep_idx = dep.find("dependent").get("idx")
            dep_text = dep.find("dependent").text
            dep_type = dep.get("type")
            if dep_type == "nsubj" or dep_type == "dobj":
                dep_dic.setdefault((gov_idx, gov_text), {}).update({dep_type:dep_text})

        for key, value in dep_dic.items():
            if "nsubj" in value.keys() and "dobj" in value.keys():
                print("{:4}\t{:15}\t{:15}\t{:15}".format(sentence.get("id"), 
                        value["nsubj"], key[1], value["dobj"]))


if __name__ == '__main__':
    tree = ET.parse("nlp.txt.xml")
    elem = tree.getroot()
    extract_tuple(elem)
