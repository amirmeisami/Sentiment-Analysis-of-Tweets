__author__ = 'meisami'
import sys
import json

def preprocess (tweet):
    uncode= []
    decode=[]
    for x in tweet.readlines():
        y= json.loads(x)
        if y.has_key("text"):
            uncode.append(y["text"])
    for x in uncode:
        decode.append((x.encode("utf-8")))

    return decode
def Dict(sample):
    x = []
    for s in sample.readlines():
            y = s .split("\t")
            x.append((y[0], y[1]))
    return x
def compare(Text, Dic):
    for z in Text:
        val= 0.0
        for (x,y) in Dic:
            if ((x + " " )  or (" " + x)) in z:
                val= val + float(y)
        print z + "  : " + str(val)

def main():
    sent_file = open('AFINN.txt')
    tweet_file = open('samples.txt')
    x =preprocess(tweet_file)
    y= Dict(sent_file)
    compare(x,y)

if __name__ == '__main__':
    main()
