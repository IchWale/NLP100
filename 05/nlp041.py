# NLP100本ノック
# 
# 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラスChunkを実装せよ．
# このクラスは形態素（Morphオブジェクト）のリスト（morphs），
# 係り先文節インデックス番号（dst），
# 係り元文節インデックス番号のリスト（srcs）
# をメンバ変数に持つこととする．
# さらに，入力テキストのCaboChaの解析結果を読み込み，
# １文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
# 第5章の残りの問題では，ここで作ったプログラムを活用せよ．

import re

class Morph(object):
    """
    表層形(surface), 基本形(base)，品詞(pos)，品詞細分類1(pos1)
    をアトリビュートに持つだけのクラス
    atr:
        self.surface: str, 表層形
        self.base: str, 基本形
        self.pos: str, 品詞
        self.pos1: str, 品詞細分類1
    """
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "surface: {}, base:{}, pos:{}, pos1:{}".format(self.surface,
            self.base, self.pos, self.pos1)


class Chunk(object):
    """
    文節の
    形態素(Morphオブジェクト)のリスト(morphs), 係り先文節インデックス番号(dst),
    係り元文節インデックス番号のリスト(srcs)をアトリビュートとして持つクラス
    atr:
        self.morphs: list, Morphモブジェクトのリスト
        self.num: int, 要件にないけど追加, 自身の文節番号
        self.dst: int, 掛かり先のインデックス番号
        self.srcs: list, 掛かり元のインデックス番号(int)のリスト
    """
    def __init__(self, morphs, num, dst, srcs):
        self.morphs = morphs
        self.num = num
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        surface = " ".join([morph.surface for morph in self.morphs])
        return "{}, num:{}, dst:{}, srcs:{}".format(surface, 
            self.num, self.dst, self.srcs)

    def get_surf(self, rm_symbol=True):
        if rm_symbol:
            return "".join([morph.surface for morph in self.morphs if morph.pos != "記号"])
        return "".join([morph.surface for morph in self.morphs])

    def get_pos_list(self):
        return [morph.pos for morph in self.morphs]

    def get_morphs(self, pos="all"):
        if pos == "all":
            return [morph for morph in self.morphs]
        else:
            return [morph for morph in self.morphs if morph.pos == pos]


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
    複数行のCaboChaの解析結果から、1行ごとに切り出して処理を行い、
    各行をChunkオブジェクトのリストとする関数
    args:
        file_neme: str, MeCabの解析結果のファイル名
    return:
        all_sentences: list, 各行のchunkリストを格納したリスト
    """
    all_sentences = []
    with open(file_name, "r", encoding="utf-8") as f:
        text_list = f.read().split("EOS\n")
        for text in text_list:
            if text != "":
                all_sentences.append(parse_chunk(text + "EOS"))
    return all_sentences


def parse_chunk(cabocha_text):
    """
    1行分のCaboChaの解析結果から、各分節のChunkオブジェクトを生成し、
    1行をChunkオブジェクトのリストとして返す関数
    args:
        cabocha_text: str, 1行分のCaboChaの解析結果
    return: 
        chunk_list: list, Chunkオブジェクトのリスト
    """
    lines = cabocha_text.split('\n')
    pattern = re.compile(r"^\*\s([0-9]+)\s([^D]+)D")
    morph_list = []
    chunk_list = []
    srcs_list = [[] for i in range(len(lines))] # 掛かり元を記録しておくためのリスト

    for line in lines:
        if re.search(r"^\*\s[0-9]+", line):
            if morph_list:
                chunk_list.append(Chunk(morph_list, num, dst, srcs))
            morph_list = []
            match = re.search(pattern, line)
            num = int(match.group(1))
            dst = int(match.group(2))
            srcs_list[int(match.group(2))].append(int(match.group(1)))
            srcs = srcs_list[int(match.group(1))]
        elif line == "EOS":
            if morph_list:
                chunk_list.append(Chunk(morph_list, num, dst, srcs))
            break
        else:
            morph_list.append(mecab_to_morph(line))

    return chunk_list


if __name__ == '__main__':
    all_sentences = read_cabocha("neko.txt.cabocha")
    for cnt, chunk in enumerate(all_sentences[7]):
        print("chunk{}:{}".format(cnt, chunk))

    # for sentence in all_sentences:
    #     for cnt, chunk in enumerate(sentence):
    #         print("chunk{}:{}".format(cnt, chunk))
    #     print("\n")


"""
メモ
後々使いやすくなるかなと思い
全文をループする関数と1文をパーズする関数を分けた

parse_chunk()について
掛かり元のリストsrcsの扱いに少し迷った
先人のコードを見ると、各分節のChunkオブジェクトを一通り生成した後、
EOSが来たときに、係り受け関係をsrcsアトリビュートに追加していた.

045のために修正.Chunkのアトリビュートにnumを追加
"""