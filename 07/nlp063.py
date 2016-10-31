# NLP100本ノック
# 
# 63. オブジェクトを値に格納したKVS
# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．
# さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．

import json
import redis
import sys


def set_db_tag(r, file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        with r.pipeline() as pipe:
            pipe.multi()
            for line in f:
                data = json.loads(line)
                # hash型:keyをname, valueはid:area
                if "tags" in data.keys():
                    value = {data["id"]:str(data.get("tags")).encode("utf-8")}
                    pipe.hmset(data["name"].encode("utf-8"), value)
            pipe.execute()


def get_tags(r, name):
    area = r.hgetall(name) if r.hgetall(name) else None
    return area


if __name__ == '__main__':
    args = sys.argv
    r = redis.StrictRedis(host="localhost", port=6379, db=2)

    if "d" in args:
        file_name = "artist.json"
        set_db_tag(r, file_name)

    print("artist name:", end="")
    name = input()
    area = get_tags(r, name)
    if area:
        for key, item in area.items():
            print("id:{}, tags:{}".format(key.decode(), item.decode()))
    else:
        print("該当なし")

"""
メモ

問題の要件がいまいち曖昧でつかみにくい

実行するときコマンドライン引数でdを指定するとデータベースに書き込む
検索のみの場合はオプションなし
"""
