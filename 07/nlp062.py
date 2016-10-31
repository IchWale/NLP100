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
        if r.hget(key, "area") == area:
            cnt += 1

    return cnt


if __name__ == '__main__':
    start = time.time()
    r = redis.StrictRedis(host="localhost", port=6379, db=0)
    area = b"Japan"
    cnt = count_by_area(r, area)
    print(cnt)
    elapsed_time = time.time() - start
    print("elapsed_time:{} [sec]".format(elapsed_time))
    # elapsed_time:29.450867891311646 [sec]

"""
メモ

29.450867891311646 [sec]
全データを走査するので, けっこう時間が掛かります.
何か良い方法があるんでしょうか...

redisのdocumentationには

>>キー・バリュー・ストアの本質は、キーに対して、値と呼ばれるどんなデータでも格納できるという点にあります。
>>このデータは、保存時に使用した正確なキーを知っている場合にのみ、後からアクセスができます。値の側から検索する方法はありません。
http://redis.shibu.jp/tutorial/


修正版 -> nlp062_2.py

"""