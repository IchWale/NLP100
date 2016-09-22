# NLP100本ノック
# 
# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import requests
import re

# API:Imageinfoのページの例をほとんどそのまま
payload = {"action":"query", 
            "titles":"File:Flag of the United Kingdom.svg", 
            "prop":"imageinfo", 
            "iiprop":"url", 
            "format":"json"}
r = requests.get("https://ja.wikipedia.org/w/api.php", params=payload)
# jsonに直すと(辞書のkeyがページidになっていて)参照するのが面倒になるので正規表現で抽出
url = re.search(r'"url":"([^"]+)",', r.text).group(1)
print(url)


# urllibはモダンじゃないから使わないとインターン先ですごい人が言ってました.
# requestsを使っているので、入っていない場合は
# $ pip install requests
