# NLP100本ノック
# 
# 47. 機能動詞構文のマイニング
# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
# 46のプログラムを以下の仕様を満たすように改変せよ．

# 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
# 例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，
# 以下の出力が得られるはずである．

# 返事をする      と に は        及ばんさと 手紙に 主人は

# このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

# コーパス中で頻出する述語（サ変接続名詞+を+動詞）
# コーパス中で頻出する述語と助詞パターン

from nlp041 import read_cabocha

def case_pattern(chunk_list, dst_pos):
    """
    指定した品詞に掛かる格(助詞)を調べる関数
    args:
        chunk_list, list, Chunkオブジェクトのリスト
        dst_pos: str, 品詞
    return:
        [(サ変名Chunk, 動詞のMorph, (助詞のMorph, ...), (助詞を含むChunk, ...)), ...]
    """
    case_list = []
    chunk_dep_list = set_src_chunk(chunk_list)
    for chunk_dep in chunk_dep_list:
        if dst_pos in chunk_dep[0].get_pos_list():
            sahen_chunk = None
            particles = []
            chunks_contain_part = []
            verbs = chunk_dep[0].get_morphs(dst_pos)
            for chunk in chunk_dep[1]:
                morphs = chunk.get_morphs()
                if len(morphs) == 2:
                    if morphs[0].pos1 == "サ変接続" and morphs[1].surface == "を":
                        sahen_chunk = chunk
                        continue
                if chunk.get_morphs("助詞"):
                    particles.extend(chunk.get_morphs("助詞"))
                    chunks_contain_part.append(chunk)
            if sahen_chunk:
                case_list.append((sahen_chunk, verbs[0], tuple(particles), tuple(chunks_contain_part)))        

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
            particles = " ".join([morph.surface for morph in case[2]])
            chunk_surf = " ".join([chunk.get_surf() for chunk in case[3]])
            print("{}{}\t{}\t{}".format(case[0].get_surf(), case[1].base, particles, chunk_surf))

"""
メモ
助詞の係り受けがない動詞句も出力している.

動詞句の係り元の文節に助詞が複数含まれていた場合、それをすべて抽出していたが、
問題文中の出力例をみると、最後の助詞だけでよいらしい.

入力:別段くるにも及ばんさと、主人は手紙に返事をする。

公式の出力例
返事をする     と に は   及ばんさと 手紙に 主人は

本プログラムの出力
返事をする   さ と は に   及ばんさと 主人は 手紙に

46行目を
- particles.extend(chunk.get_morphs("助詞"))
+ particles.append(chunk.get_morphs("助詞")[-1])
と修正すれば公式通りになる
"""
