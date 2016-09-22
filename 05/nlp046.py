# NLP100本ノック
# 
# 46. 動詞の格フレーム情報の抽出
# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

# 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
# 「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
# この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
# 「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
# 始める  で      ここで
# 見る    は を   吾輩は ものを

from nlp041 import read_cabocha

def case_pattern(chunk_list, dst_pos):
    """
    指定した品詞に掛かる格(助詞)を調べる関数
    args:
        dst_pos: str, 品詞
    return:
        [(動詞のMorph, (助詞のMorph, ...), (助詞を含むChunk, ...)), ...]
    """
    case_list = []
    chunk_dep_list = set_src_chunk(chunk_list)
    for chunk_dep in chunk_dep_list:
        if dst_pos in chunk_dep[0].get_pos_list():
            particles = []
            chunks_contain_part = []
            verbs = chunk_dep[0].get_morphs(dst_pos)
            for chunk in chunk_dep[1]:
                if chunk.get_morphs("助詞"):
                    particles.extend(chunk.get_morphs("助詞"))
                    chunks_contain_part.append(chunk)
            case_list.append((verbs[0], tuple(particles), tuple(chunks_contain_part)))                
        
    return case_list


def set_src_chunk(chunk_list):
    """
    (chunk, chunkに係るchunkのタプル)のリストを返す関数
    """
    chunk_dep_list = []
    for chunk in chunk_list:
        src_chunk_list = tuple([chunk_list[i] for i in chunk.srcs])
        chunk_dep_list.append((chunk, src_chunk_list))

    return chunk_dep_list


if __name__ == '__main__':
    all_sentences = read_cabocha("neko.txt.cabocha")
    for sentence in all_sentences:
        case_list = case_pattern(sentence, "動詞")
        for case in case_list:
            particles = " ".join([morph.surface for morph in case[1]])
            chunk_surf = " ".join([chunk.get_surf() for chunk in case[2]])
            print("{}\t{}\t{}".format(case[0].base, particles, chunk_surf))
