# NLP100本ノック
# 
# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
# 1行に1記事の情報がJSON形式で格納される
# 各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
# そのオブジェクトがJSON形式で書き出される
# ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．

# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，
# 「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import json

with open("jawiki-country.json", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            print(data["text"])
            with open("jawiki-britain.txt", "w", encoding="utf-8") as f2:
                f2.write(data["text"])
            # WindowsだとたぶんUnicodeEncodeErrorになるので以下をつかう
            # print(data["text"].encode("sjis", "ignore").decode("sjis"))

"""
めも

与えられたjsonファイルをファイルオブジェクトからjson.load()で一度に読み込もうとすると,

In [1]: f = open("jawiki-country.json", "r", encoding="utf-8")
In [2]: s = json.load(f)
JSONDecodeError: Extra data: line 2 column 1 (char 27837)

と怒られた. 

与えられたjsonファイルは次のような形式

{"text": "本文1", "title": "国名1"}
{"text": "本文2", "title": "国名2"}
{"text": "本文3", "title": "国名3"}
...略

これは辞書型を羅列した形になっていて, pythonのデータ構造として一度に読み込めない. 
つまり、たぶんjson.load()で読み込めない. (オプションを指定すれば解決できる？)
json.load()で読み込むには, 

[
    {"text": "本文1", "title": "国名1"},
    {"text": "本文2", "title": "国名2"},
    {"text": "本文3", "title": "国名3"}
]

みたいに、各辞書が配列の要素となるような構造となってる必要がある. 

"""