# NLP100本ノック
# 
# 56. 共参照解析
# Stanford Core NLPの共参照解析の結果に基づき，
# 文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
# ただし，置換するときは，「代表参照表現（参照表現）」のように，
# 元の参照表現が分かるように配慮せよ．

import re
import xml.etree.ElementTree as ET

def get_coreferences(elem):
    """
    coreferenceの関係を使いやすい形で抜き出しておく関数
    args:
        elem: nlp.txt.xmlを読み込んだETオブジェクト
    return:
        {
            s_id:[(s_id, e_id, mention, rep_mention), ...],
            ...
        }
        sentence_idをkeyとする辞書型、要素はタプルのリスト
        各タプル()は(開始id, 終端id, mention, rep_mention)
    """

    cf_list = elem.find(".//coreference")
    cf_dic = {}
    for cf in cf_list:
        for m in cf.findall("mention"):
            if m.get("representative") == "true":
                rep_mention = m.findtext("text")
            else:
                s_id = m.findtext("sentence")
                m_tuple = (m.findtext("start"), m.findtext("end"), 
                    m.findtext("text"), rep_mention)
                cf_dic[s_id] = cf_dic.get(s_id, [])
                cf_dic[s_id].append(m_tuple)
    return cf_dic


def replace_mention(elem):
    """
    参照表現を代表参照表現に置換しながら出力する関数
    args:
        elem: nlp.txt.xmlを読み込んだETオブジェクト
    """
    cf_dic = get_coreferences(elem)

    for sentence in elem.find(".//sentences"):
        if sentence.get("id") in cf_dic:
            for rep in cf_dic[sentence.get("id")]:
                for token in sentence.findall(".//token"):
                    if token.get("id") == rep[0]:
                        token.find("word").text = "{}({})".format(rep[3], rep[2])
                    elif int(rep[0]) < int(token.get("id")) < int(rep[1]):
                        token.find("word").text = ""
            word_list = [token.findtext("word") for token in sentence.findall(".//token") \
                            if token.findtext("word") != ""]
        else:
            word_list = [token.findtext("word") for token in sentence.findall(".//token")]
        print(" ".join(word_list))


if __name__ == '__main__':
    tree = ET.parse("nlp.txt.xml")
    elem = tree.getroot()
    replace_mention(elem)

