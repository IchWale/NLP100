# NLP100本ノック
# 
# 60. KVSの構築
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．

# 要件を満たすよう修正

import json
import redis


def set_db(r, file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        with r.pipeline() as pipe:
            pipe.multi()
            for line in f:
                data = json.loads(line)
                # hash型:keyをname, valueはid:area
                value = {data["id"]:data.get("area", "unknown").encode("utf-8")}
                pipe.hmset(data["name"].encode("utf-8"), value)
            pipe.execute()


if __name__ == '__main__':
    file_name = "artist.json"
    r = redis.StrictRedis(host="localhost", port=6379, db=1)
    set_db(r, file_name)


"""
nameが重複するので, 
nameをkey, idをhash値, areaをvalueとして記録

例えば宇宙人というnameは2人いるので, 

宇宙人{1009652:Japan, 662905:Taiwan}

といったデータ構造になる

"""