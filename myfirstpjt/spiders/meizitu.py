# # -*- coding: utf-8 -*-
# 性感妹子

# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from ..items import MyfirstpjtItem
# import os
# import requests
# from scrapy.crawler import CrawlerProcess
#
# def mkdir(path):
#     a = path.strip()
#     # 去除尾部 \ 符号
#     a = path.rstrip("\\")
#     # 判断路径是否存在
#     # 存在     True
#     # 不存在   False
#     isExists = os.path.exists(a)
#     # 判断结果
#     if not isExists:
#         # 如果不存在则创建目录
#         # 创建目录操作函数
#         os.makedirs(a)
#         return True
#     else:
#         # 如果目录存在则不创建，并提示目录已存在
#         return False
#
#
# class MeizituSpider(scrapy.Spider):
#     name = 'meizitu'
#     allowed_domains = ['mzitu.com']
#     start_urls = ['http://mzitu.com/']
#     custom_settings = {
#      'LOG_LEVEL': 'DEBUG',
#     "DEFAULT_REQUEST_HEADERS": {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#         'Referer': 'http://www.mzitu.com'
#     }
#     }
#     def parse(self, response):
#         fnames = response.css('ul.menu')
#         # tjn = response.css('#pins')
#         # tujinames = tjn.xpath('.//li/span/a/text()').extract()
#         fenleiwenjianjias_name = fnames.xpath('./li/a/text()')[1:-3].extract()
#         for fenleiwenjianjia_name in fenleiwenjianjias_name:
#             global mkpath_1
#             mkpath_1 = "D:\\pycharm project\\myfirstpjt" + "\\" + fenleiwenjianjia_name
#             mkdir(mkpath_1)
#         # for tujiname in tujinames:
#         #     mkpath_2 = mkpath_1 + "\\" + tujiname
#         #     mkdir(mkpath_2)
#         sel = LinkExtractor(restrict_css='ul.menu>li>a')
#         # links = sel.extract_links(response)
#         # if links:
#         #     next_url = links[0].url
#         #     yield scrapy.Request(next_url,callback=self.parse)
#         for link in sel.extract_links(response)[1:-3]:
#             yield scrapy.Request(link.url,callback=self.parse_tupian_jihe)
#         pass
#
#     def parse_tupian_jihe(self,response):
#         # tp = MyfirstpjtItem()
#         tjn = response.css('#pins')
#         tujinames = tjn.xpath('.//li/span/a/text()').extract()
#         title_all = response.css('li.current-menu-item')
#         title = title_all.xpath('./a/@title').extract_first()
#         for tujiname in tujinames:
#             mkpath_2 = "D:\\pycharm project\\myfirstpjt" + "\\" + title + "\\" + tujiname
#             mkdir(mkpath_2)
#         sel = LinkExtractor(restrict_xpaths='//ul[@id="pins"]/li/span/a')
#
#         sel_next = response.css('div.nav-links a.next')
#         next_tj_url = sel_next.xpath('@href').extract_first()
#         page_next = response.css('div.nav-links a.next::text').extract_first()
#         if page_next == '下一页»':
#             yield scrapy.Request(next_tj_url,callback=self.parse_tupian_jihe)
#         for link in sel.extract_links(response):
#             yield scrapy.Request(link.url,callback=self.parse_tupian_dantao)
#         pass
#
#     def parse_tupian_dantao(self,response):
#         le = LinkExtractor(restrict_css='div.pagenavi>a')
#         link = le.extract_links(response)[-1]
#         if link.text == '下一页»':
#             next_url = link.url
#             # print(next_url)
#             yield scrapy.Request(next_url,callback=self.parse_tupian_danzhang)
#         else:
#             pass
#         pass
#
#     def parse_tupian_danzhang(self,response):
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#             'Referer': 'http://www.mzitu.com'
#         }
#         title_name = response.css('li.current-menu-parent a::text').extract_first()
#         tuji_name = response.css('div.currentpath::text').extract()[-1][3:]
#         num = response.css('h2.main-title::text').re_first('(\d+)')
#         sel_main = response.css('div.main-image>p>a>img')
#         img_url = sel_main.xpath('@src').extract_first()
#         sel_next = response.css('div.main-image>p>a')
#         next_img_url = sel_next.xpath('@href').extract_first()
#         if str(num) == 'None':
#             filename = "D:\\pycharm project\\myfirstpjt" + "\\" + title_name + "\\" + tuji_name + "\\" +"1.jpg"
#         else:
#             filename = "D:\\pycharm project\\myfirstpjt" + "\\" + title_name + "\\" + tuji_name + "\\" + "{0}.jpg".format(num)
#         r = requests.get(img_url,headers = headers)
#         with open(filename, 'wb') as f:
#             f.write(r.content)
#             print('已保存{0}'.format(filename))
#         yield scrapy.Request(next_img_url,callback=self.parse_tupian_danzhang)
#
#
#
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MyfirstpjtItem
import os
import requests
from scrapy.crawler import CrawlerProcess

def mkdir(path):
    a = path.strip()
    # 去除尾部 \ 符号
    a = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(a)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(a)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']
    custom_settings = {
     'LOG_LEVEL': 'DEBUG',
    "DEFAULT_REQUEST_HEADERS": {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer': 'http://www.mzitu.com'
    }
    }
    def parse(self, response):
        fnames = response.css('ul.menu')
        # tjn = response.css('#pins')
        # tujinames = tjn.xpath('.//li/span/a/text()').extract()
        fenleiwenjianjia_name = fnames.xpath('./li/a/text()')[1].extract()
        global mkpath_1
        mkpath_1 = "D:\\pycharm project\\myfirstpjt" + "\\" + fenleiwenjianjia_name
        mkdir(mkpath_1)
        # for tujiname in tujinames:
        #     mkpath_2 = mkpath_1 + "\\" + tujiname
        #     mkdir(mkpath_2)
        sel = LinkExtractor(restrict_css='ul.menu>li>a')
        # links = sel.extract_links(response)
        # if links:
        #     next_url = links[0].url
        #     yield scrapy.Request(next_url,callback=self.parse)
        link = sel.extract_links(response)[1]
        yield scrapy.Request(link.url,callback=self.parse_tupian_jihe)
        pass

    def parse_tupian_jihe(self,response):
        # tp = MyfirstpjtItem()
        tjn = response.css('#pins')
        tujinames = tjn.xpath('.//li/span/a/text()').extract()
        title_all = response.css('li.current-menu-item')
        title = title_all.xpath('./a/@title').extract_first()
        for tujiname in tujinames:
            mkpath_2 = "D:\\pycharm project\\myfirstpjt" + "\\" + title + "\\" + tujiname
            mkdir(mkpath_2)
        sel = LinkExtractor(restrict_xpaths='//ul[@id="pins"]/li/span/a')

        sel_next = response.css('div.nav-links a.next')
        next_tj_url = sel_next.xpath('@href').extract_first()
        page_next = response.css('div.nav-links a.next::text').extract_first()
        if page_next == '下一页»':
            yield scrapy.Request(next_tj_url,callback=self.parse_tupian_jihe)
        for link in sel.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_tupian_dantao)
        pass

    def parse_tupian_dantao(self,response):
        le = LinkExtractor(restrict_css='div.pagenavi>a')
        link = le.extract_links(response)[-1]
        if link.text == '下一页»':
            next_url = link.url
            # print(next_url)
            yield scrapy.Request(next_url,callback=self.parse_tupian_danzhang)
        else:
            pass
        pass

    def parse_tupian_danzhang(self,response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': 'http://www.mzitu.com'
        }
        title_name = response.css('li.current-menu-parent a::text').extract_first()
        tuji_name = response.css('div.currentpath::text').extract()[-1][3:]
        num = response.css('h2.main-title::text').re_first('(\d+)')
        sel_main = response.css('div.main-image>p>a>img')
        img_url = sel_main.xpath('@src').extract_first()
        sel_next = response.css('div.main-image>p>a')
        next_img_url = sel_next.xpath('@href').extract_first()
        if str(num) == 'None':
            filename = "D:\\pycharm project\\myfirstpjt" + "\\" + title_name + "\\" + tuji_name + "\\" +"1.jpg"
        else:
            filename = "D:\\pycharm project\\myfirstpjt" + "\\" + title_name + "\\" + tuji_name + "\\" + "{0}.jpg".format(num)
        r = requests.get(img_url,headers = headers)
        with open(filename, 'wb') as f:
            f.write(r.content)
            print('已保存{0}'.format(filename))
        yield scrapy.Request(next_img_url,callback=self.parse_tupian_danzhang)



