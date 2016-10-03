# NLP100本ノック
# 
# 53. Tokenization
# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
# また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．


# java -Xmx5g -cp stanford-corenlp-3.6.0.jar:stanford-corenlp-3.6.0-models.jar:* edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,mention,coref -file nlp050_result.txt -outputFormat xml

import re

pattern = re.compile(r"<word>([^<]+)</word>")

with open("nlp.txt.xml", "r", encoding="utf-8") as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            print(match.group(1))



