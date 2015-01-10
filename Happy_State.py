__author__ = 'meisami'
import sys
import json

def preprocess (tweet):
    decode=[]
    for x in tweet.readlines():
        y= json.loads(x)
        if y.has_key("place"):
            if y["place"] != None and y["place"]["country"] == "United States" and y["place"]["country_code"] == "US":
               state= (y["place"]["full_name"]).split(",")[1]
               text = y["text"].encode("utf-8")
               decode.append((text,state))
    return decode

def Dict(sample):
    x = []
    for s in sample.readlines():
            y = s.split("\t")
            x.append((y[0], y[1]))
    return x

def compare(Text, Dic):
    states={}
    for (tweet, st) in Text:
        val= 0.0
        for (x,y) in Dic:
            if ((x + " " )  or (" " + x)) in tweet:
                val= val + float(y)
                if st in states:
                    states[st] += val
                else:
                    states[st] = val
    x= 0.0
    finalState = ""
    for key, value in states.iteritems():
        if value > x:
            finalState = key
            x= value
    print finalState

def main():
    sent_file = open('AFINN.txt')
    tweet_file = open('samples.txt')
    x =preprocess(tweet_file)
    y= Dict(sent_file)
    compare(x,y)

if __name__ == '__main__':
    main()
