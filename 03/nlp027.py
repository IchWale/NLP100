# NLP100本ノック
# 
# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
# テキストに変換せよ（参考: マークアップ早見表）．

# 内部リンクとは[[]]で囲まれている部分らしい. 
# とくに指定がないので, [[記事名|表示文字]]となっているものは表示文字を残すことにする

import re
from nlp025 import parse_info
from nlp026 import remove_emphasis

def remove_link(info_list):
    pattern = re.compile(r"\[{2}(?:[^\|\[\]]+\|)?([^\]]+)\]{2}")
    for info in info_list:
        info[1] = re.sub(pattern, "\g<1>", info[1])
    return info_list


if __name__ == '__main__':
    with open("jawiki-britain.txt", "r", encoding="utf-8") as f:
        text = f.read()
    info_list = parse_info(text)
    info_list = remove_emphasis(info_list)
    info_list = remove_link(info_list)
    for info in info_list:
        print("{}: \n{}\n".format(info[0], info[1]))