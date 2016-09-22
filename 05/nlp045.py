# NLP100本ノック
# 
# 45. 動詞の格パターンの抽出
# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 
# 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． 
# ただし，出力は以下の仕様を満たすようにせよ．

# ・動詞を含む文節において，最左の動詞の基本形を述語とする
# ・述語に係る助詞を格とする
# ・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

# 「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． 
# この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
# 「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

# 始める  で
# 見る    は を

# このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

# コーパス中で頻出する述語と格パターンの組み合わせ
# 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ


from nlp041 import read_cabocha

def case_pattern(chunk_list, dst_pos):
    """
    指定した品詞に掛かる格(助詞)を調べる関数
    args:
        dst_pos: str, 品詞
    return:
        [(動詞のMorph, (助詞のMorph, 助詞のMorph, ...)), ...]
    """
    case_list = []
    chunk_dep_list = set_src_chunk(chunk_list)
    for chunk_dep in chunk_dep_list:
        if dst_pos in chunk_dep[0].get_pos_list():
            particles = []
            verbs = chunk_dep[0].get_morphs(dst_pos)
            for chunk in chunk_dep[1]:
                particles.extend(chunk.get_morphs("助詞"))
            case_list.append((verbs[0], tuple(particles)))                
        
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
            print("{}\t{}".format(case[0].base, particles))

"""
メモ
for文でlistにappend()するか内包表記にするかいつも迷う.
可読性を取るならfor文?速度を取るなら内包表記?
"""
