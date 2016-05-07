# Wikipedia Hashtags

A set of scripts to cache [Wikipedia Hashtag](http://blog.hatnote.com/post/112756032432/the-humble-hashtag-now-on-wikipedia). 

This script connects to the Wikipedia database replica on [Wikimedia Tool Labs](https://wikitech.wikimedia.org/wiki/Help:Tool_Labs), searches for hashtags, and then stores it in another database with nice indexes for searching. See [hashtag search](https://github.com/hatnote/hashtag-search). On Tool Labs, the database is kept up-to-date on 10-20 minute interval scheduled via crontab.

## Usage

```
$ python update.py --lang <two letter language code>
```

Options:

```
$ python update.py --help

  -h, --help     show this help message and exit
  --lang LANG
  --hours HOURS
  --debug
```

## TODOs

 - Add support for other Wikimedia projects
 - Add additional lanugages

## Notes

Connect to the hashtag database on Tool Labs:


```
mysql --defaults-file=${HOME}/replica.my.cnf -h s1.labsdb s52467__hashtags
```