# NLP100本ノック
# 
# 68. ソート
# "dance"というタグを付与されたアーティストの中で
# レーティングの投票数が多いアーティスト・トップ10を求めよ．

# Mongoシェル
# db.test_coll.find({tags: {$elemMatch: {value: "dance"}}}, {name: true, tags: true, rating:true}).sort({"rating.count": -1}).limit(10)

import pymongo
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    coll = client.test_db.test_coll

    data = coll.find({"tags":{"$elemMatch": {"value": "dance"}}})
    data = data.sort("rating.count", pymongo.DESCENDING)[0:10]
    for art in data:
        print(art["name"], art["rating"]["count"])

    client.close()

