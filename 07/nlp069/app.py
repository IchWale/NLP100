# NLP100本ノック
# 
# ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．
# アーティスト名，アーティストの別名，タグ等で検索条件を指定し，
# アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．


from flask import Flask, render_template, request, redirect, url_for
from artists_db import ArtistsDataBase

# 接続するmongodbのdb名とcollectionm名を設定
DATABASE = "test_db"
COLLECTION = "test_coll"

app = Flask(__name__)
art_db = ArtistsDataBase(db=DATABASE, collection=COLLECTION)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/send", methods=["GET"])
def search_db():
    elem_dic = {}
    for elem in ["name", "aliase", "area", "tag"]:
        elem_dic[elem] = request.args.get(elem, default="")
    results = art_db.search_artists(art_db.generate_query(elem_dic))
    fields = ["name", "aliases", "area", "tags", "rating"]
    return render_template("result.html", results=results, fields=fields)

if __name__ == "__main__":
    app.debug = True
    app.run()