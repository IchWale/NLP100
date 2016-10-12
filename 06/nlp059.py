# NLP100本ノック
# 
# 59. S式の解析
# Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．
# 入れ子になっている名詞句もすべて表示すること．

import xml.etree.ElementTree as ET
import re

def parse_exp(text, exp_list):
    """
    S式をパーザする関数. 与えられたテキスト中のすべてのS式をリストとして返す.
    一対の()で閉じている式を一旦{}に置換し、置換後のテキストを入力として再帰的に処理.
    式として確定した部分は{}を()に直してリストに格納
    args:
        text: str, S式のテキスト
        exp_list, list, S式のリスト
    return:
        exp_list, list, S式のリスト
    """
    pattern = re.compile(r"\(([^()]+)\)")
    pattern_s = re.compile(r"{(.+?)}")
    if re.search(pattern, text):
        rep = lambda s: "(" + s.translate(str.maketrans("{}", "()")) + ")"
        exp_list.extend([rep(s) for s in re.findall(pattern, text)])
        rep_text = re.sub(pattern, "{\g<1>}", text)
        exp_list = parse_exp(rep_text, exp_list)
    return exp_list


def extract_np(elem):
    """
    Stanford Core NLPの解析結果xmlのS式から名詞句(NP)を出力する関数
    args:
        elem: ETオブジェクト, Stanford Core NLPの解析結果xmlのETパーザオブジェクト
    """
    pattern = re.compile(r"\([A-Z]+ ([^()]+)\)")
    for sentence in elem.find(".//sentences"):
        s_exp = sentence.find("parse").text
        exp_list = parse_exp(s_exp, [])
        print("--------sentence id :{}--------".format(sentence.get("id")))

        for exp in exp_list:
            if exp[0:3] == "(NP":
                print(" ".join(re.findall(pattern, exp)))

        
if __name__ == '__main__':
    tree = ET.parse("nlp.txt.xml")
    elem = tree.getroot()
    extract_np(elem)
