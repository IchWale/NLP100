# NLP100本ノック
# 
# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．

# set_chunk_depをテキスト返すのではなく、Chunkオブジェクトとして返すように
# 修正したものを作成した(nlp42_2.py)

from nlp041 import read_cabocha

def set_chunk_dep(chunk_list):
    """
    1文のchunkリストから(係り元の文節のテキスト, 係り先の文節のテキスト)という
    タプルのリストとして返す関数
    """
    chunk_dep_list = []
    for chunk in chunk_list:
        src_surf = chunk.get_surf()
        if src_surf == "":
            continue
        elif chunk.dst == -1:
            dst_surf = ""
        else:
            dst_surf = chunk_list[chunk.dst].get_surf()
        chunk_dep_list.append((src_surf, dst_surf))

    return chunk_dep_list



if __name__ == '__main__':
    all_sentences = read_cabocha("neko.txt.cabocha")
    for sentence in all_sentences:
        chunk_dep_list = set_chunk_dep(sentence)
        for chunk_dep in chunk_dep_list:
            print("{}\t{}".format(chunk_dep[0], chunk_dep[1]))
        print("\n")
