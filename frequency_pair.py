# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import nltk
import json
import collections


def extract_text(filename):
    with open(filename, 'r') as f:
        res = ""
        for jsonstr in f.readlines():
            j = json.dumps(eval(jsonstr))
            j = json.loads(j)
            res+=j["text"]
            res+=" "
    return res

def tokenization(text):
    tokens1 = nltk.word_tokenize(text)
    return tokens1

def frequency(tokens):
    print(collections.Counter([word.lower() for word in tokens]))

def POS(sentence):
    return  nltk.pos_tag(sentence)

def frequency_pair(tagged):
    res = []
    chunkGram = r"""Chunk: {<JJ><NN.*>}"""
    chunkGram1 = r"""Chunk1: {<NN.*><VB.*><RB>*<JJ>}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunkParser1 = nltk.RegexpParser(chunkGram1)
    chunked = chunkParser.parse(tagged)
    chunked1 = chunkParser1.parse(tagged)
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
        res.append(subtree.leaves()[0][0]+"-"+subtree.leaves()[1][0])
    for subtree in chunked1.subtrees(filter=lambda t: t.label() == 'Chunk1'):
        res.append(subtree.leaves()[len(subtree)-1][0] + "-" + subtree.leaves()[0][0])
    # print(res)
    return res
    # chunked.draw()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename1 = "yelp_academic_dataset_review.json"
    filename2 = "rate1.json"
    # choose_rate(1, filename1, filename2)
    str = extract_text(filename2)
    res = POS(tokenization(str))
    frequency(frequency_pair(res))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
