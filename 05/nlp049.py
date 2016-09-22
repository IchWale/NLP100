# NLP100本ノック
# 
# 49. 名詞間の係り受けパスの抽出
# 文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
# ただし，名詞句ペアの文節番号がiとj（i<j）のとき，
# 係り受けパスは以下の仕様を満たすものとする．

# 問題48と同様に，パスは開始文節から終了文節に至るまでの
# 各文節の表現（表層形の形態素列）を"->"で連結して表現する
# 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
# また，係り受けパスの形状は，以下の2通りが考えられる．

# 文節iから構文木の根に至る経路上に文節jが存在する場合: 
#     文節iから文節jのパスを表示
# 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 
#     文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，
#     文節kの内容を"|"で連結して表示

# 例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

# Xは | Yで -> 始めて -> 人間という -> ものを | 見た
# Xは | Yという -> ものを | 見た
# Xは | Yを | 見た
# Xで -> 始めて -> Y
# Xで -> 始めて -> 人間という -> Y
# Xという -> Y

from nlp041 import read_cabocha


def noun_path(chunk_list):
    
    path_list = []
    for chunk in chunk_list:
        if "名詞" in chunk.get_pos_list():
            for r_chunk in chunk_list[chunk.num+1:]:
                if "名詞" in r_chunk.get_pos_list():
                    path = get_toward_path(chunk_list, chunk.num, r_chunk.num)
                    if path:
                        path_list.append(path)
    return path_list


def get_toward_path(chunk_list, chunk_num_start, chunk_num_end):
    """
    与えられた文のChunkリストから, 
    指定された文節番号(文節i)から、指定された文節番号(文節j)までの係り受けのパスを返す。
    係り受けパスが通っていない場合、
    文節iと文節jから構文木の根に至るまでの共通の文節kをさがし、
    文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を返す.
    """
    path = [chunk_list[chunk_num_start]]
    i_path = [replace_noun(chunk_list[chunk_num_start], "X")]
    dst = chunk_list[chunk_num_start].dst
    while dst != -1:
        if dst == chunk_num_end:
            i_path.append(replace_noun(chunk_list[dst], "Y"))
            return [i_path]
        path.append(chunk_list[dst])
        i_path.append(chunk_list[dst].get_surf())
        dst = chunk_list[dst].dst
    else:
        j_dst = chunk_num_end
        j_path = [replace_noun(chunk_list[j_dst], "Y")]
        while j_dst != -1:
            for cnt, i_path_chunk in enumerate(path):
                if chunk_list[j_dst].dst == i_path_chunk.dst:
                    return [i_path[:cnt+1], j_path, [chunk_list[i_path_chunk.dst].get_surf()]]
            j_dst = chunk_list[j_dst].dst
            j_path.append(chunk_list[j_dst].get_surf())
    return None


def replace_noun(chunk, re_noun):
    """
    文節から名詞句をre_nounに変換した文字列を返す
    """
    re_str = ""
    flag = 0
    morphs = chunk.get_morphs()
    for morph in morphs:
        if morph.pos == "名詞":
            if flag == 0:
                flag = 1
                re_str += re_noun
        elif morph.pos != "記号":
            re_str += morph.surface
    return re_str


if __name__ == '__main__':
    all_sentences = read_cabocha("neko.txt.cabocha")
    for sentence in all_sentences:
        path_list = noun_path(sentence)
        for path in path_list:
            path_str = " | ".join([" -> ".join(x_path) for x_path in path])
            print(path_str)
        print("-------------------------------------")
