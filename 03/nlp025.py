# NLP100本ノック
# 
# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．

# 公式国名が複数行にまたがっているので面倒そう

import re

# のちの問題でも使ったので関数化
def parse_info(text):

    # いったん基礎情報の部分を抜き出す
    pattern_f = re.compile(r"{{基礎情報.+^}}", re.MULTILINE | re.DOTALL)
    text = re.search(pattern_f, text).group()

    # re.split()で各情報ごとに切り取ってから処理したほうがやりやすい
    # が、あえて正規表現を使って一発で取り出すと
    pattern_g = re.compile(r"^\|([^ ]+) = (.+?)(\n(?=\|)|\n(?=}}))", re.M | re.S)
    match_list_temp = re.findall(pattern_g, text)
    match_list = [[i[0], i[1]] for i in match_list_temp]
    return match_list


if __name__ == '__main__':
    f = open("jawiki-britain.txt", "r", encoding="utf-8")
    text = f.read()
    info_list = parse_info(text)
    for info in info_list:
        print("{}: \n{}\n".format(info[0], info[1]))

"""
めも

.+?の意味を今更知る
"""
