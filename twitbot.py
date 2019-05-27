#!/bin/python3

import os, math, time, tweepy

file_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
TWEET_LEN = 240

def login_to_twitter():
        with open(file_dir + "login") as f:
                try:
                        login_data = f.readlines()
                finally:
                        f.close()

        CONSUMER_KEY = login_data[0].strip('\n')
        CONSUMER_SECRET = login_data[1].strip('\n')
        ACCESS_KEY = login_data[2].strip('\n')
        ACCESS_SECRET = login_data[3].strip('\n')

        auth = tweepy.0AuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)

        return api


def split_quote(text, maxlen):
        tlen = len(text)
        twords = text.split()
        numtweets = math.ceil(tlen / maxlen)
        splitlen = math.ceil(tlen / numtweets)
        splits = []

        for i in range(numtweets):
                tweet = ""
                length = 0
                while length < splitlen and len(twords) > 0:
                        tweet = tweet + twords[0] + " "
                        length = length + len(twords[0])
                        del twords[0]

                splits.append(tweet)
        return splits

def post(msg, api):
        

def parse_data_file():
        
        with open(file_dir + "datafile") as f:
                try:
                        line = f.read().strip('\n')
                finally:
                        f.close()

        # datafile is colon delimited
        line = line.split(':')
        if len(line) != 3:
                print("Error reading datafile, quitting...")
                quit()

        textfile = line[0]
        currentLine = int(line[1])
        totalLines = int(line[2])

        info = (textfile, currentLine, totalLines)
        return info

def update_datafile(info):
        
        with open(file_dir + "datafile", 'w') as f:
                try:
                        f.write(info[0] + ":" + str(info[1]) + ":" + str(info[2]))
                finally:
                        f.close()


def get_quotes(filename):
        
        with open(file_dir + filename) as f:
                try:
                        lines = f.readlines()
                finally:
                        f.close()

        return lines

def tweet():

        textfile, curLine, numLines = parse_data_file()
        if curLine >= numLines:
                quit()          # all lines have been read

        quotes = get_quotes(textfile)
        tweets = split_quote(quotes[curLine], TWEET_LEN)
        numtweets = len(tweets)

        api = login_to_twitter()
        
        if numtweets == 1:
                post(tweets[0], api)
        else:
                for t in range(numtweets):
                        tweet = "" + str(t+1) + "/" + str(numtweets) + ":\n" + tweets[t]
                        post(tweet, api)
                        time.sleep(5)   # wait 5 seconds between multiple tweets

        # update data file for next tweet
        curLine = curLine + 1
        update_datafile((textfile, curLine, numLines))

tweet()
