# NLP100本ノック
# 
# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
# 国の基本情報を整形せよ.

# <>で囲まれたタグと{{}}を消せばよい?

import re
from nlp025 import parse_info
from nlp026 import remove_emphasis
from nlp027 import remove_link

def remove_markup(info_list):
    pattern = re.compile(r"<[^>]+>|\**\{{2}|\}{2}")
    for info in info_list:
        info[1] = re.sub(pattern, "", info[1])
    return info_list

if __name__ == '__main__':
    f = open("jawiki-britain.txt", "r", encoding="utf-8")
    text = f.read()
    info_list = parse_info(text)
    info_list = remove_emphasis(info_list)
    info_list = remove_link(info_list)
    info_list = remove_markup(info_list)
    for info in info_list:
        print("{}: \n{}\n".format(info[0], info[1]))