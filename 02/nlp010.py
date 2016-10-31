# NLP100本ノック
# 
# hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」の
# タブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
# hightemp.txtを入力ファイルとして実行せよ．
# さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
# 
# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ

with open("hightemp.txt", "r", encoding="utf-8") as f:
    print(len(f.readlines()))

# UNIXコマンド
# あとで