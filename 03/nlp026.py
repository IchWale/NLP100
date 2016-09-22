# NLP100本ノック
# # 
# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの
# 強調マークアップ（弱い強調，強調，強い強調のすべて）
# を除去してテキストに変換せよ（参考: マークアップ早見表）．

# おそらく2,3,5連シングルクォーテーションを除去しろということ？

import re
from nlp025 import parse_info

def remove_emphasis(info_list):
    for info in info_list:
        info[1] = re.sub(r"'{2,5}", "", info[1])
    return info_list


if __name__ == '__main__':
    f = open("jawiki-britain.txt", "r", encoding="utf-8")
    text = f.read()
    info_list = parse_info(text)
    info_list = remove_emphasis(info_list)
    for info in info_list:
        print("{}: \n{}\n".format(info[0], info[1]))
