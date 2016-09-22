# NLP100本ノック
# 
# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# 文字ngram
def char_ngram(text, n):
    ngram_dic = {}
    text = text.replace(" ", "")

    for i in range(len(text)-n+1):
        ngram_dic[text[i:i+n]] = ngram_dic.get(text[i:i+n], 0) + 1
        # dict.get()メソッドはkeyを渡して、その対応する要素を取り出す.
        # 第2引数を指定するとkeyが存在していなかったときに返すデフォルト値を設定できる
    return ngram_dic

# 単語ngram
def word_ngram(text, n):
    ngram_dic = {}
    word_list = text.split()
    word_tuple = tuple(word_list)

    for i in range(len(word_list)-n+1):
        ngram_dic[word_tuple[i:i+n]] = ngram_dic.get(word_tuple[i:i+n], 0) + 1 

    return ngram_dic

# 以上は頻度を求める関数だけど、
# 巷の回答を見ると、頻度は不要で、共起関係のリストを出力すればよいらしい
# 関数も一つにまとめた単語&文字ngram
def ngram(text, n, mode="char"):
    ngram_list = []

    if mode == "char":
        text = text.replace(" ", "")
        unit_list = text
    elif mode == "word":
        unit_list = tuple(text.split())

    for i in range(len(unit_list)-n+1):
        ngram_list.append(unit_list[i:i+n])

    # 文字ngramは文字列のリスト, 単語ngramはタプルのリストで返す.
    return ngram_list


if __name__ == '__main__':
    print("string:")
    text = input()
    print("n:")
    n = int(input())
    print(char_ngram(text, n))
    print(word_ngram(text, n))
    print(ngram(text, n))
    print(ngram(text, n, "word"))