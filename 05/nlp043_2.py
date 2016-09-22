# NLP100本ノック
# 
# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．

# set_chunk_depをテキスト返すのではなく、
# Chunkオブジェクトとして返すように修正した

from nlp041 import read_cabocha

def set_chunk_pos(chunk_list, src_pos="名詞", dst_pos="動詞"):
    """
    1文のchunkリストから
    指定した品詞を含む文節->指定した品詞を含む文節の係り受けを見つけ、
    (係り元の文節のChunk, 係り先の文節のChunk)という
    タプルのリストとして返す関数
    """
    chunk_dep_list = []
    for chunk in chunk_list:
        if chunk.dst == -1:
            continue
        elif src_pos in chunk.get_pos_list() and dst_pos in chunk_list[chunk.dst].get_pos_list():
            dst_chunk = chunk_list[chunk.dst]
            chunk_dep_list.append((chunk, dst_chunk))

    return chunk_dep_list


if __name__ == '__main__':
    all_sentences = read_cabocha("neko.txt.cabocha")
    for sentence in all_sentences:
        chunk_dep_list = set_chunk_pos(sentence)
        for chunk_dep in chunk_dep_list:
            print("{}\t{}".format(chunk_dep[0].get_surf(), 
                chunk_dep[1].get_surf()))
        print("\n")
