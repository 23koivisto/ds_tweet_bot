#!/usr/bin/env bash

curl -s https://mdsoar.org/feed/rss_2.0/site > ./xml/tmp.xml

python tweet_store.py ./xml/tmp.xml
