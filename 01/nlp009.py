# NLP100本ノック
# 
# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
# を与え，その実行結果を確認せよ．

import random

def Typoglycemia(text):
    word_list = text.split()
    new_word_list = []
    
    for i in word_list:
        if len(i) > 4:
            temp = ""
            temp += i[0]
            # random.shuffle()は文字列に直接使えないのでrandom.sampleを使ってみる
            temp += "".join(random.sample(i[1:-1], len(i[1:-1])))
            temp += i[-1]
            new_word_list.append(temp)
        else:
            new_word_list.append(i)

    return " ".join(new_word_list)

if __name__ == '__main__':
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(Typoglycemia(text))
