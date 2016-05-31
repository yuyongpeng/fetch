#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

import unittest
import fetchcore.config.config as config


class YamlConfigParserTestCase(unittest.TestCase):

    def setUp(self):
        """
        每个测试函数运行前运行
        :return:
        """
        self.YamlConfigParser = config.YamlConfigParser()
        self.yamlFile = file("config.yml", 'r')
        self.url1 = "http://www.bloomberg.org:8080/page2/test/234-sdf32r-sdf.html?p1=a&p2=2#12345v"

    def tearDown(self):
        """
        每个测试函数运行完后执行
        :return:
        """
        pass

    @classmethod
    def setUpClass(cls):
        """
        必须使用@classmethod 装饰器,所有test运行前运行一次
        :param cls:
        :return:
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """
        必须使用@classmethod装饰器,所有test运行完后运行一次
        :return:
        """
        pass

    # @unittest.expectedFailure
    def test_yaml_load_domain(self):
        """
        具体的测试用例,一定要以test开头
        :return:
        """
        var = [{'procotol': 'http', 'content': {'search': 'div[id=storytext]', 'remove': [{'attribute': 'id', 'tag': 'div', 'reg': True, 'value': 'res[0-9]+'}, {'attribute': 'class', 'tag': 'div', 'reg': False, 'value': 'container'}]}, 'img': {'search': 'div[id=storytext]', 'tag': 'img', 'attribute': 'src', 'type': 'tag', 'remove': [{'attribute': 'id', 'tag': 'div', 'reg': True, 'value': 'res[0-9]+'}, {'attribute': 'class', 'tag': 'div', 'reg': False, 'value': 'container'}], 'subcontent': False}, 'path-reg': '/page2/*', 'example': 'http://123234.bloomberg.org/page2/1232-43212.html?sdf#fdfsdf', 'auth': {'search': 'div[id=kk]', 'subcontent': False}, 'domain-reg': '[0-9a-zA-Z]+.bloomberg.org'}, {'procotol': 'https', 'content': {'search': 'div[id=storytext]', 'remove': [{'attribute': 'id', 'tag': 'div', 'reg': True, 'value': 'res[0-9]+'}, {'attribute': 'class', 'tag': 'div', 'reg': False, 'value': 'container'}]}, 'img': {'search': 'div[id=storytext]', 'tag': 'img', 'attribute': 'src', 'type': 'tag', 'remove': [{'attribute': 'id', 'tag': 'div', 'reg': True, 'value': 'res[0-9]+'}, {'attribute': 'class', 'tag': 'div', 'reg': False, 'value': 'container'}], 'subcontent': False}, 'path-reg': '/page/*', 'example': 'https://sqwe42223.bloomberg.org/page/1232-43212.html', 'auth': {'search': 'div[id=kk]', 'subcontent': False}, 'domain-reg': '[a-zA-Z0-9]+.bloomberg.org'}]
        print self.YamlConfigParser.yaml_getconf_url(self.yamlFile, self.url1)
        self.assertDictEqual(self.YamlConfigParser.yaml_getconf_url(self.yamlFile, self.url1), var)
        self.assertEqual(3, 3)

    @unittest.skip("test_yaml_load_domain22222222222 这个测试方法没有完成,暂时跳过")
    def test_yaml_load_domain2(self):
        """
        具体的测试用例,一定要以test开头
        :return:
        """
        var = [{'procotol': 'http', 'content': {'search': 'div[id=storytext]', 'remove': [{'attribute': 'id', 'tag': 'div', 'reg': True, 'value': 'res[0-9]+'}, {'attribute': 'class', 'tag': 'div', 'reg': False, 'value': 'container'}]}, 'img': {'search': 'div[id=storytext]', 'tag': 'img', 'attribute': 'src', 'type': 'tag', 'remove': [{'attribute': 'id', 'tag': 'div', 'reg': True, 'value': 'res[0-9]+'}, {'attribute': 'class', 'tag': 'div', 'reg': False, 'value': 'container'}], 'subcontent': False}, 'path-reg': '/page2/*', 'example': 'http://123234.bloomberg.org/page2/1232-43212.html?sdf#fdfsdf', 'auth': {'search': 'div[id=kk]', 'subcontent': False}, 'domain-reg': '[0-9a-zA-Z]+.bloomberg.org'}, {'procotol': 'https', 'content': {'search': 'div[id=storytext]', 'remove': [{'attribute': 'id', 'tag': 'div', 'reg': True, 'value': 'res[0-9]+'}, {'attribute': 'class', 'tag': 'div', 'reg': False, 'value': 'container'}]}, 'img': {'search': 'div[id=storytext]', 'tag': 'img', 'attribute': 'src', 'type': 'tag', 'remove': [{'attribute': 'id', 'tag': 'div', 'reg': True, 'value': 'res[0-9]+'}, {'attribute': 'class', 'tag': 'div', 'reg': False, 'value': 'container'}], 'subcontent': False}, 'path-reg': '/page/*', 'example': 'https://sqwe42223.bloomberg.org/page/1232-43212.html', 'auth': {'search': 'div[id=kk]', 'subcontent': False}, 'domain-reg': '[a-zA-Z0-9]+.bloomberg.org'}]
        print self.YamlConfigParser.yaml_getconf_url(self.yamlFile, self.url1)
        self.assertDictEqual(self.YamlConfigParser.yaml_getconf_url(self.yamlFile, self.url1), var)
        self.assertEqual(3, 3)
if __name__ == "__main__":
    # unittest.main()

    unittest.TestLoader.loadTestsFromModule()

    # suite = unittest.TestLoader.loadTestsFromTestCase(YamlConfigParserTestCase)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # suite = unittest.TestSuite()
    # suite.addTest(YamlConfigParserTestCase('test_yaml_load_domain'))
    # suite.addTest(YamlConfigParserTestCase('test_yaml_load_domain2'))
    # unittest.TextTestRunner.run(suite)

    tests = ['test_yaml_load_domain', 'test_yaml_load_domain2']
    suite = unittest.TestSuite(map(YamlConfigParserTestCase, tests))
    unittest.TextTestRunner(verbosity=2).run(suite())

