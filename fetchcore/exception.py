#!/usr/bin/env python
#  -*- coding: UTF-8 -*-


class UrlError(Exception):
    """
    url不符合规定的异常
    """

    def __init__(self, var_str_error):
        super(UrlError, self).__init__()
        self.__var_str_error = var_str_error

    def __str__(self):
        # print self.__var_str_error
        return repr(self.__var_str_error)
