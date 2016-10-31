# NLP100本ノック
# 
# 61. KVSの検索
# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ

import redis


def get_area(r, art_id):
    area = r.hget(art_id, "area").decode("utf-8") if r.hget(art_id, "area") else "該当なし"
    return area


if __name__ == '__main__':
    r = redis.StrictRedis(host="localhost", port=6379, db=0)
    print("artist id:", end="")
    art_id = input()
    area = get_area(r, art_id)
    print(area)

"""
修正版 -> nlp061_2.py
"""
