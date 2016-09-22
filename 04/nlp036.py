# NLP100本ノック
# 
# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

from nlp030 import read_mecab


file_name = "neko.txt.mecab"
all_sentences = read_mecab(file_name)

def word_freq(all_sentences):
    """
    read_mecab()の出力から、単語の頻度を求める
    辞書に記録してから, 頻度の降順にタプルのリストに変換して返す.
    辞書をそのまま返すことも可能.
    args:
        all_sentences: list, read_mecab()で出力される形式のリスト
    return:
        freq_list_desc: list, タプル(単語, 頻度)のリスト(頻度の降順)
    """
    freq_dic = {}
    for sentence in all_sentences:
        for morph in sentence:
            freq_dic[morph["surface"]] = freq_dic.get(morph["surface"], 0) + 1
    freq_list_desc = sorted(freq_dic.items(), key=lambda x :x[1], reverse=True)
    # return freq_dic
    return freq_list_desc

if __name__ == '__main__':
    file_name = "neko.txt.mecab"
    all_sentences = read_mecab(file_name)
    freq_list_desc = word_freq(all_sentences)
    for i in freq_list_desc:
        print("{}:{}".format(i[0], i[1]))
