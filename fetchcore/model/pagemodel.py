#!/usr/bin/env python
#  -*- coding: UTF-8 -*-


class PageModel:
    _url = ""
    _title = ""
    _imgs = []
    _videos = []
    _audios = []
    _content = ""
    _tag = []
    _pubdate = ""
    _auth = []
    _colum = ""
    _group = 1      # 默认是英文来源
    _id = 0         # sourse_list 表的id字段
    _name = ""      # sourse_list 表的name字段
    _appid = "0"    # sourse_list 表的appid字段

    def __init__(self, url, title, imgs, content):
         self._url = url
         self._title = title
         self._imgs = imgs
         self._content = content

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        self._group = group

    @group.deleter
    def group(self):
        del self._group

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self,url):
        self._url = url

    @url.deleter
    def url(self):
        del self._url

    @property
    def imgs(self):
        return self._imgs

    @imgs.setter
    def imgs(self,imgs):
        self._imgs = imgs

    @imgs.deleter
    def imgs(self):
        del self._imgs

    def addImg(self,img):
        self._imgs.extend(img)

    @property
    def videos(self):
        return self._videos

    @videos.setter
    def videos(self,videos):
        self._videos = videos

    @videos.deleter
    def videos(self):
        del self._videos

    def addVideos(self,videos):
        self._videos.extend(videos)

    @property
    def audios(self):
        return self._audios

    @audios.setter
    def audios(self,audios):
        self._audios = audios

    @audios.deleter
    def audios(self):
        del self._audios

    def addAudios(self,audios):
        self._audios.extends(audios)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    @title.deleter
    def title(self):
        del self._title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self,content):
        self._content = content

    @content.deleter
    def content(self):
        del self._content

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self,tag):
        self._tag = tag

    @tag.deleter
    def tag(self):
        del self._tag

    def addTag(self,tag):
        self._tag.extend(tag)

    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self,auth):
        self._auth = auth

    @auth.deleter
    def auth(self):
        del self._auth

    def addAuth(self,auth):
        self._auth.extend(auth)

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self,column):
        self._column = column

    @column.deleter
    def column(self):
        del self._column

    @property
    def pubdate(self):
        return self._pubdate

    @pubdate.setter
    def pubdate(self,pubdate):
        self._pubdate = pubdate

    @pubdate.deleter
    def pubdate(self):
        del self._pubdate

    @property
    def id(self):
        return self._id

    @id.deleter
    def id(self):
        del self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, appid):
        self._appid = appid

    @appid.deleter
    def appid(self):
        del self._appid


    def __str__(self):
        print self._title
        print self._content
        print self._imgs
        return ""

