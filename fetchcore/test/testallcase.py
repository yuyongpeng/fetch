#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

import unittest
import sys
import os


def run_all_test_case():
    """
    调用当前项目中的所有 "test_" 开头的python测试文件进行测试
    """
    # 项目的根目录
    program_path = '/Users/yuyongpeng/PycharmProjects/fetch/'
    test_modules = []
    for root, dirs, files in os.walk(program_path):
        test_modules.extend([root.replace(program_path, '').replace('/', '.') + '.' + filename.replace('.py', '')
                             for filename in files if filename.endswith('.py') and filename.startswith('test_')])
    print test_modules
    map(__import__, test_modules)
    suite = unittest.TestSuite()
    for mod in [sys.modules[modname] for modname in test_modules]:
        suite.addTest(unittest.TestLoader().loadTestsFromModule(mod))
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_all_test_case()
