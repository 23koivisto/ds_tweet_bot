#!/usr/bin/env python3

import sys
import os
import sqlite3
import tweepy


#define count to see if any entries in DB
conn = sqlite3.connect('tweet.db')
c = conn.cursor()
c.execute('select count(id) from tweet')
count = c.fetchall()

#if/then for yes data/no data
if str(count) == "[(0,)]":
    print ('Nothing new to tweet...')
    conn.close()
else:
    c.execute('select url from tweet where id = (select min(id) from tweet)')
    url = c.fetchall()[0][0]
    c.execute('select title from tweet where id = (select min(id) from tweet)')
    title = c.fetchall()[0][0]
    conn.close()
    tweet = url + ' - ' + title[:280]

    consumer_key = "##### your consumer key #####"
    consumer_secret = "##### your consumer secret #####"
    access_key = "##### your access key #####"
    access_secret = "##### your access secret #####"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    api.update_status(tweet)
    
    conn = sqlite3.connect('tweet.db')
    c = conn.cursor()
    c.execute('delete from tweet where id = (select min(id) from tweet)')
    conn.commit()
    conn.close()
