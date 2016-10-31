# NLP100本ノック
# 
# 62. KVS内の反復処理
# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．


import redis
import time

def count_by_area(r, area):
    cnt = 0
    keys = r.keys()
    for key in keys:
        data = r.hgetall(key)
        for key, value in data.items():
            if value == area:
                cnt += 1

    return cnt


if __name__ == '__main__':
    r = redis.StrictRedis(host="localhost", port=6379, db=1)
    area = b"Japan"
    cnt = count_by_area(r, area)
    print(cnt)
