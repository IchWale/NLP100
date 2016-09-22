# NLP100本ノック
# 
# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ.

def cipher(raw_str):
    cipher_str = ""
    for i in raw_str:
        if i.islower():
            cipher_str += chr(219 - ord(i))
        else:
            cipher_str += i

    return cipher_str


if __name__ == '__main__':
    strings = "I am an NLPer"
    print(strings)
    print(cipher(strings))
    print(cipher(cipher(strings)))

