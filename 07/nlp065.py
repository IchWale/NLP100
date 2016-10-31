# NLP100本ノック
# 
# 65. MongoDBの検索
# MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
# さらに，これと同様の処理を行うプログラムを実装せよ

# Mongoシェル
# > db.test_coll.find({name: "Queen"})

from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    coll = client.test_db.test_coll
    name = "Queen"

    for artist in coll.find({"name": name}):
        print(artist)

    client.close()
