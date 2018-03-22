# ds_tweet_bot

This repo is a homegrown twitter bot developed for the harvest and dissemination of resources published by a DSpace RSS feed. While it could feasibly be used to tweet out other RSS-type resource data, this program was designed with DSpace in mind (in particular, [MDSOAR](https://www.mdsoar.org)).

The primary workflow is as follows:

* source.sh set to run at a given time. Will check to see if database tables are appropriately created and will create if not. source.sh will harvest rss feed indicated in script will initiate tweet_store.py which will write out relevant tweet data to tweet.db if resource handle is not already present in archive (i.e. has not already passed through database).

* tweet_write.py set to run at a given time. Takes entered data from RSS feed and generates tweet text based on resource handle and title. This relies on the [tweepy library](https://github.com/tweepy/tweepy).

A few prerequisites & considerations:

* Download all libraries indicated in the python files.

* Existing database is titled tweet.db and is used running SQLITE3. tweet_store.py will create tables on first run.

* tweet_write.py will require you Twitter application keys. If you are not familiar with creating Twitter apps, check out the [following guide](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app).

The original vision for this program is that it should be run via crontab with commands to the effect of:

`30 4 * * * source /path/to/file/source.sh > dev/null`

`0 * * * * python /path/to/file/tweet_write.py > dev/null`

