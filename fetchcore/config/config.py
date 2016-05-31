#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
import urlparse

from yaml import load
import re
from fetchcore.exception import UrlError
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

"""
"""
# 配置文件的变量, 便于程序的修改
pageparse = "pageparse"
website = "website"


class YamlConfigParser:
    """
    配置文件的解析类
    解析yaml格式的配置信息
    """

    def __init__(self): pass

    @staticmethod
    def yaml_load(var_str_yaml):
        """
        加载yaml格式的配置文件为python的对象
        :param var_str_yaml: yaml 格式的字符串
        :return:
        """
        return load(var_str_yaml)

    @staticmethod
    def yaml_load_domain(var_str_yaml, domain, procotol = "http"):
        yml = load(var_str_yaml)
        yml[pageparse][website][domain]

    @staticmethod
    def yaml_getconf_url(var_str_yaml, var_str_url):
        """
        分析url获取配置文件中对应规则
        :param var_star_yaml:   yaml格式的字符串
        :param var_str_url:     需要解析的url
        :return:
        """
        yml = load(var_str_yaml)
        uparse = urlparse.urlparse(var_str_url)
        scheme = uparse.scheme
        hostname = uparse.hostname
        port = uparse.port
        path = uparse.path
        query = uparse.query
        fragment = uparse.fragment
        if scheme == "":
            raise UrlError(u"scheme cannot be empty ! 可能是提供的url规则不对. 请查看var_str_url='%s'的值" % var_str_url)
        if hostname == "":
            raise UrlError(u"hostname cannot be empty ! 可能是提供的url规则不对. 请查看var_str_url='%s'的值" % var_str_url)
        if path == "":
            raise UrlError(u"path cannot be empty ! 可能是提供的url规则不对. 请查看var_str_url='%s'的值" % var_str_url)
        sp_list = hostname.split(".")
        if len(sp_list) <= 1:
            raise UrlError(u"[ %s ] 不是正确的域名,正确的域名使用 '.' 切割后>=2" % hostname)
        first_level_domain = sp_list[-2] + "." + sp_list[-1]
        domain_analytical_rules = yml[pageparse][website][first_level_domain]
        for rule in domain_analytical_rules:
            procotol_reg_compile = re.compile(rule['procotol'])
            if procotol_reg_compile.match(scheme) == None:
                continue
            domain_reg_compile = re.compile(rule['domain-reg'])
            if domain_reg_compile.match(hostname) == None:
                continue
            path_reg_compile = re.compile(rule['path-reg'])
            if path_reg_compile.match(path) == None:
                continue
            return domain_analytical_rules

if __name__ == "__main__":
    stream = file('config.yml', 'r')
    #x = load(stream)
    #print x['pageparse']['website']['bloomberg.org']
    url = "http://www.bloomberg.org:8080/page2/test/234-sdf32r-sdf.html?p1=a&p2=2#12345v"
    print YamlConfigParser.yaml_getconf_url(stream, url)

