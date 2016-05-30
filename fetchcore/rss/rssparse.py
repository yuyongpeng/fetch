#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
    使用feedparser解析rss
"""

import feedparser
from fetchcore.base.fetchbase import FetchBase


class RssParse(FetchBase):

    name = ""
    
    # def __init__(self, title, link, description, published):
    #     super(RssParse, self).__init__(title, link, description, published)

    def fetch_content(self, url):
        """
        解析rss页面获得对应的内容
        :param url:
        :return:
        """
        d = feedparser.parse(url)
        print d.version
        for entry in d.entries:
            print entry.title
            print entry.link
            print entry.description
            print entry.published
            print entry.published_parsed
        # print d.feed.title
        # print d.feed.link
        # print d.feed.description
        # print d.feed.published

if __name__ == "__main__":
    url = "http://www.guardian.co.uk/rssfeed/0,,40,00.xml"
    rssParse = RssParse()
    rssParse.fetch_content(url)
