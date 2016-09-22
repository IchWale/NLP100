# NLP100本ノック
# 
# 48. 名詞から根へのパスの抽出
# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． 
# ただし，構文木上のパスは以下の仕様を満たすものとする．

# 各文節は（表層形の）形態素列で表現する
# パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
# 「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
# 次のような出力が得られるはずである．

# 吾輩は -> 見た
# ここで -> 始めて -> 人間という -> ものを -> 見た
# 人間という -> ものを -> 見た
# ものを -> 見た

from nlp041 import read_cabocha

def chunk_path(chunk_list, leaf_pos="名詞"):
    """
    指定した品詞を持つ文節から構文木の根に至るパスを返す
    args:
        chunk_list, list, Chunkオブジェクトのリスト
        dst_pos: str, 品詞
    return:
        path_list, list, パスのリスト.　パスはChunkのリストとして表現
    """
    path_list = []
    for chunk in chunk_list:
        if leaf_pos in chunk.get_pos_list():
            path = [chunk]
            dst = chunk.dst
            while dst != -1:
                path.append(chunk_list[dst])
                dst = chunk_list[dst].dst
            path_list.append(path)
    return path_list


if __name__ == '__main__':
    all_sentences = read_cabocha("neko.txt.cabocha")
    for sentence in all_sentences:
        path_list = chunk_path(sentence)
        for path in path_list:
            print(" -> ".join([chunk.get_surf() for chunk in path]))
        print("------------------------------------")