# NLP100本ノック
# 
# 67. 複数のドキュメントの取得
# 特定の（指定した）別名を持つアーティストを検索せよ．

# Mongoシェル
# > db.test_coll.find({aliases: {$exists: true}}).count()
# 82644

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    coll = client.test_db.test_coll
    print(coll.find({"aliases": {"$exists": True}}).count())
    client.close()