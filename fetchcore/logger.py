#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

import logging
import logging.config
from fetchcore.exception import UrlError
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("single")

#u = UrlError(u"scheme cannot be empty ! 可能是提供的url规则不对. 请查看var_str_url='%s'的值")
#try:
#    raise u
#except:
#    logger.exception("")
# for i in xrange(50):
#     logger.debug('This is debug message')
#     logger.info('This is info message')
#     logger.warning('This is warning message')
#     import time
#     time.sleep(1)
