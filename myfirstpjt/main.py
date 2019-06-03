# auther:aiyishiqu time:2019/6/1
from scrapy import cmdline

cmdline.execute("scrapy mycrawl --nolog".split())
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
# if __name__ == '__main__':
#     process = CrawlerProcess(get_project_settings())
#     process.crawl('meizitu')    #  你需要将此处的spider_name替换为你自己的爬虫名称
#     process.start()