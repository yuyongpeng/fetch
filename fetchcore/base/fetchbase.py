#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty


class FetchBase(object):

    __metaclass__ = ABCMeta

    # def __init__(self, title, link, description, published):
    #     self.title = title
    #     self.link = link
    #     self.description = description
    #     self.published = published

    @abstractmethod
    def fetch_content(self, url):
        """
        获取url内容并解析出对应的数据. 是 rss和feedly抓取类的超类
        :return:
        """
        pass

    @abstractproperty
    def name(self): pass
