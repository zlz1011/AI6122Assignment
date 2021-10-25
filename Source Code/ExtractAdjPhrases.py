import nltk
import json
import collections
import random
import math
import sys

def random_business(filename):
    a = random.randint(0, 8635402)
    business_id = 0
    with open(filename, 'rb') as f:
        count = 0
        for jsonstr in f.readlines():
            count+=1
            if count!= a: continue
            else:
                business_id = (eval(jsonstr))["business_id"]
    return business_id

def extra_review_randomly(filename):
    random_list=[]
    count = 0
    random_number = 1000
    while count<random_number:
        a = random.randint(0,8635402)
        if a not in random_list:
            random_list.append(a)
            count+=1
    random_list.sort()
    with open(filename, 'rb') as f:
        res = []
        count1=0
        iter = 0
        for jsonstr in f.readlines():
            if iter >random_number-1: break
            if count1==random_list[iter]:
            # j = json.dumps(eval(jsonstr))
            # j = json.loads(j)
                j=eval(jsonstr)
                res.append(j["text"])
                iter+=1
            count1+=1
    return res

def extra_business_review(business_id,filename1):
    res=[]
    with open(filename1, 'r', encoding="utf-8") as f:
        for jsonstr in f.readlines():
            j = json.loads(jsonstr)
            if(j["business_id"]==business_id):
                res.append(j["text"])
    return res

def tokenization(text):
    tokens1 = nltk.word_tokenize(text)
    return tokens1

def frequency(tokens):
    return collections.Counter([word.lower() for word in tokens])


def POS(sentence):
    return  nltk.pos_tag(sentence)

def extract_adjphrase(tagged):
    res = []
    chunkGram = r"""Chunk: {<RB.*>*<JJ.*>}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    # chunked.draw()
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
        j = 0
        tmp =''
        for i in range(len(subtree.leaves())):
            if j!=0:
                tmp+=" "
            tmp+=subtree.leaves()[i][0].lower()
            j+=1
        if tmp!='':
            if tmp not in res:
                res.append(tmp)
    return res

def str_to_dict(str):
    res = dict()
    for i in range(len(str)):
        res[str[i][0]]=str[i][1]
    return res

def reviews_adj_frequency(reviews):
    res_pos = []
    for review in reviews:
        tmp = POS(tokenization(review))
        res_pos.append(tmp)
    res_pair = []
    for item in res_pos:
        res_pair += extract_adjphrase(item)
    return frequency(res_pair).most_common()

if __name__ == '__main__':
    choice = '1'
    while choice!="4":
        choice = input("1.use random business\n2.use samplereview(business_id=RA4V8pr014UyUbDvI-LW2A)\n3.use a specified business_id\n4.exit\n")
        reviews = []
        if choice =="4": sys.exit()
        if choice =="1":
        # time_start = time.time()
            business_id = random_business("yelp_academic_dataset_review.json")
        else:
            if choice =="2": business_id='RA4V8pr014UyUbDvI-LW2A'
            else:
                if choice == "3": business_id = input("please input the business_id")
                else: print("wrong number!")
        print("the selected business_id is",business_id)
        print("------extracting reviews of the selected business...")
        try:
            reviews = extra_business_review(business_id,"yelp_academic_dataset_review.json")
            if len(reviews)==0:
                raise Exception("wrong business_id!\n")
        except Exception as e:
            print(e)
            sys.exit(0)
        # print("time:",time.time()-time_start)
        print("------extracting adjective phrases from reviews...")
        fre_str = reviews_adj_frequency(reviews)
        print("tf of top-10 phrases in selected business:\n",[fre[0]+':'+str(fre[1]/len(reviews)) for fre in fre_str[0:10]])
        print("------randomly extracting 10000 reviews from dataset...")
        reviews_random = extra_review_randomly("yelp_academic_dataset_review.json")
        # print("time:", time.time() - time_start)
        print("------extracting adjective phrases from reviews...")
        tmp = reviews_adj_frequency(reviews_random)
        fre_dict = str_to_dict(tmp)
        print("Top-10 phrases in random reviews:\n", tmp[0:10])
        indicate_adj = dict()
        iter = 20
        if len(fre_str)<20: iter = len(fre_str)
        print("------calculating tf-idf...")
        for i in range(iter):
            tf = fre_str[i][1]/len(reviews)
            fre = fre_dict.get(fre_str[i][0],0)
            idf = math.log10(len(reviews_random)/(fre+0.1))
            #print(fre_str[i][0],tf,idf)
            indicate_adj[fre_str[i][0]]=tf*idf
        indicate_adj = sorted(indicate_adj.items(),key=lambda d:d[1],reverse=True)
        # print("time:",time.time()-time_start)
        print("Top-10 tf-idf:\n",indicate_adj[0:10])
        print("-------the indicative adjective phrase is",indicate_adj[0][0],"------\n")
        tmp = input("input anything to continue")



