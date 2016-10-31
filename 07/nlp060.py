# NLP100本ノック
# 
# 60. KVSの構築
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．

import json
import redis


def set_db(r, file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        with r.pipeline() as pipe:
            pipe.multi()
            for line in f:
                data = json.loads(line)
                value = {"name":data["name"].encode("utf-8"), "area":data.get("area", "unknown").encode("utf-8")}
                pipe.hmset(data["id"], value)
            pipe.execute()


if __name__ == '__main__':
    file_name = "artist.json"
    r = redis.StrictRedis(host="localhost", port=6379, db=0)
    set_db(r, file_name)

    
"""
メモ

データベースはあんまり触れてこなかったのでよく分かってないかもしれません.

redisはpipeline処理というのでトランザクションっぽいことが可能らしい
とりあえず, 排他とか整合性は考えずに, multiとexecでまとめて処理
multi()とexecute()の間にエラーが発生したら何も実行しないようにした...つもりだけど本当になってる?

RDB, NoSQL

追記
よく問題文を見ると,
nameからareaを検索できるようなDB設計じゃないといけないらしいです

修正版 -> nlp060_2.py


"""
