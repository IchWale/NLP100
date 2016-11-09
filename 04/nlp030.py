# NLP100本ノック
# 
# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
# その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

# なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
# キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ.

# neko.txtの解析
# $ mecab neko.txt -o neko.txt.mecab

def mecab_to_dic(mecab_text):
    """
    MeCabの解析結果(MeCabの出力形式)1行から、形態素の
    表層形(surface), 基本(base), 品(pos), 品詞細分類1(pos1)を
    keyとする辞書型を作成する
    args:
        file_name: str, MeCabの解析結果の1行分
    return: 
        morph_list: list, 形態素の辞書
    """
    mecab_text =  mecab_text.replace("\n", "")
    tab_split = mecab_text.split("\t")
    element_list = tab_split[1].split(",")
    morph_dic = {"surface": tab_split[0],
                "base": element_list[6],
                "pos": element_list[0],
                "pos1": element_list[1]}
    return morph_dic


def read_mecab(file_name):
    """
    MeCabの解析結果から1行ごとに読み込んで、mecab_to_dicに渡す.
    返ってきた辞書は元のテキスト1行分(EOSが現れる)ごとにリストに格納.
    今回元のテキストneko.txtは1行1文になっているのでEOSで区切れば, 
    1文ごとに形態素をリストに格納できる.
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
            morph_dic = mecab_to_dic(line)
            morph_list.append(morph_dic)
    return all_sentences


if __name__ == '__main__':
    file_name = "neko.txt.mecab"
    all_sentences = read_mecab(file_name)
    for sentence in all_sentences[::100]:
        print(sentence)
        print('\n')
