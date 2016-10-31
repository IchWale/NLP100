# mongodbクライアント

import pymongo
from pymongo import MongoClient

class ArtistsDataBase():
    def __init__(self, db, collection, hostname="localhost", port=27017):
        self.client = MongoClient(hostname, port)
        self.coll = self.client[db][collection]


    def generate_query(self, elem):
        """
        pymongoの検索条件のリストを生成するメソッド
        """
        query = []
        for field in ["name", "area"]:
            if elem.get(field, ""):
                query.append({field: elem[field]})

        if elem.get("aliase", ""):
            query.append({"aliase":{"$elemMatch": {"name": elem["aliase"]}}})

        if elem.get("tag", ""):
            query.append({"tags":{"$elemMatch": {"value": elem["tag"]}}})

        return query
        

    def search_artists(self, query):
        """
        検索条件のリストからand検索した結果をratingでソートして返すメソッド
        """
        data = self.coll.find({"$and": query})
        data = data.sort("rating.count", pymongo.DESCENDING).limit(50)
        results = []
        for doc in data:
            art_dic = {}
            art_dic["name"] = doc.get("name", "")
            art_dic["aliases"] = ", ".join([i["name"] for i in doc.get("aliases", [{"name": ""}])])
            art_dic["area"] = doc.get("area", "")
            art_dic["tags"] = ", ".join([i["value"] for i in doc.get("tags", [{"value": ""}])])
            art_dic["rating"] = doc.get("rating", {"count": ""})["count"]
            results.append(art_dic)

        return results


if __name__ == '__main__':
    DATABASE = "test_db"
    COLLECTION = "test_coll"

    art_db = ArtistsDataBase(db=DATABASE, collection=COLLECTION)
    elem_dic = {}
    elem_dic.update({"name":"", "area": "", "tag": "dance"})
    results = art_db.search_artists(art_db.generate_query(elem_dic))
    print(results)
    fields = ["name", "aliases", "area", "tags", "rating"]
    for artist in results:
        for field in fields:
            print(artist[field])
        print("---------------------")
