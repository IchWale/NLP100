# NLP100本ノック
# 
# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）を
# CaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．
# このファイルを用いて，以下の問に対応するプログラムを実装せよ．

# $ cabocha -f1 neko.txt -o neko.txt.cabocha

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．
# このクラスは表層形(surface), 基本形(base)，品詞(pos)，品詞細分類1(pos1)
# をメンバ変数に持つこととする. さらに, CaboChaの解析結果(neko.txt.cabocha)を読み込み，
# 各文をMorphオブジェクトのリストとして表現し, 3文目の形態素列を表示せよ. 

import re

class Morph(object):
    """
    表層形(surface), 基本形(base)，品詞(pos)，品詞細分類1(pos1)
    をアトリビュートに持つだけのクラス
    """
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "surface: {}, base:{}, pos:{}, pos1:{}".format(self.surface,
            self.base, self.pos, self.pos1)

# CaboChaは各形態素の情報をMeCab形式で出力するので流用
def mecab_to_morph(mecab_text):
    """
    MeCabの解析結果(MeCabの出力形式)1行から、
    Morphオブジェクトを生成する
    args:
        file_name: str, MeCabの解析結果の1行分
    return: 
        morph: Morph
    """
    mecab_text =  mecab_text.replace("\n", "")
    tab_split = mecab_text.split("\t")
    elem_list = tab_split[1].split(",")
    morph = Morph(tab_split[0], elem_list[6], elem_list[0], elem_list[1])
    return morph


def read_cabocha(file_name):
    """
    CaboChaの解析結果から1行ごとに読み込んで、形態素の情報をmecab_to_morphに渡す.
    返ってきたMorphオブジェクトは元のテキスト1行分(EOSが現れる)ごとにリストに格納.
    各文のリストはさらにリストにネストする
    args:
        file_neme: str, MeCabの解析結果のファイル名
    return:
        all_sentences: list, 1文ごとの形態素のリストを要素としたリスト
    """
    morph_list = []
    all_sentences = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if line == "EOS\n":
                if morph_list:
                    all_sentences.append(morph_list)
                morph_list = []
                continue
            if re.search(r"^\*\s[0-9]+", line):
                continue
            morph = mecab_to_morph(line)
            morph_list.append(morph)
    return all_sentences


if __name__ == '__main__':
    all_sentences = read_cabocha("neko.txt.cabocha")
    for morph in all_sentences[2]:
        print(morph)
