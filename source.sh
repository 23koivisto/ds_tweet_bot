#!/usr/bin/env bash

curl -s https://mdsoar.org/feed/rss_2.0/site > ./tmp.xml

python tweet_store.py ./tmp.xml
