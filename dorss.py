#!/usr/bin/python

import feedparser
import random
import sys

lines = open("main.feeds").read().splitlines()
random.shuffle(lines)

for url in lines:
    cur = feedparser.parse(url)
    print "<div id=\"rss\">"
    try:
#        print cur['feed']['title'].encode('utf-8') + " | " + cur['feed']['link'].encode('utf-8')
        print "<h4>{ <a href=\"" +cur['feed']['link'].encode('utf-8') + "\">" + cur['feed']['title'] + "</a> } </h4></br>"
    except:
        pass

    kt = 0
    for post in cur.entries:
        kt += 1
        if kt>10:
            break
        try:
            title = post.title.encode('utf-8')[:100]
#            print "<li><a href=\"" + post.link.encode('utf-8') + "\">" + post.title.encode('utf-8') + "</a></li>"
            print "<li><a href=\"" + post.link.encode('utf-8') + "\">" + title + "</a></li>"
        except:
            pass
#        try:
#            print  " (Published: " + post.published.encode('utf-8')
#        except:
#            pass
#        print "</li>"

    print "</p>"
    print "</div>"
