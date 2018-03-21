#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET
from shutil import copyfile
import os
import sqlite3

rss_save='xml/rss_out.xml'

#database check
conn = sqlite3.connect('tweet.db')
c = conn.cursor()
c.execute('select name from sqlite_master where type = ? and name = ?', ('table','tweet'))
check=c.fetchone()
if check is None:
    print('No TWEET table. Creating...')
    c.execute('create table tweet (id INTEGER PRIMARY KEY, url TEXT, title TEXT)')
    conn.commit()
else:
    print('TWEET table exists...')
    
c.execute('select name from sqlite_master where type = ? and name = ?', ('table','archive'))
check=c.fetchone()
if check is None:
    print('No ARCHIVE table. Creating...')
    c.execute('create table archive (url TEXT)')
    conn.commit()
else:
    print('ARCHIVE table exists...')

conn.close()

#function to write tweets to database
def tweet_write(db, url_in, title_in):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('insert into tweet(url, title) values(?,?)', (url_in,title_in,))
    c.execute('insert into archive(url) values(?)', (url_in,))
    conn.commit()
    conn.close()
    
#function to check resource handle in archive database    
def tweet_check(db, url_in):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('select url from archive where url = ?', (url_in,))
    data=c.fetchone()
    if data is None:
        return False
    else:
        return True
    
print('Retrieving most recent RSS feed...')
r = open('xml/tmp.xml','r')
t = ET.parse(r)

print('Writing tweets to database...')

for item in t.getroot().findall('channel/item'):
    url=item.find('link').text
    title=item.find('title').text
    if tweet_check('tweet.db', url) == False:
        tweet_write('tweet.db', url, title)
        print('Adding ' + url + ' - ' + title + ' to database...')
    else:
        print('Record already in archive. Skipping...')

print('Removing temp RSS file...')
os.remove('xml/tmp.xml')

