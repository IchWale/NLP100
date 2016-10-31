# NLP100本ノック
# 
# 61. KVSの検索
# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ

# 名前から検索できるよう修正

import redis


def get_area(r, name):
    area = r.hgetall(name) if r.hgetall(name) else None
    return area


if __name__ == '__main__':
    r = redis.StrictRedis(host="localhost", port=6379, db=1) # 修正版のdbは1番
    print("artist name:", end="")
    name = input()
    area = get_area(r, name)
    if area:
        for key, item in area.items():
            print("id:{}, area:{}".format(key.decode(), item.decode()))
    else:
        print("該当なし")


