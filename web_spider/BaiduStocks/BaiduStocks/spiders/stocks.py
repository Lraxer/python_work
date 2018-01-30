# -*- coding: utf-8 -*-
import scrapy
import re

# 注意：此代码似乎会被反爬，造成爬取失败
class StocksSpider(scrapy.Spider):
    name = 'stocks'
    # allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():    #初步分析extract()返回的是字符串
            try:
                stock = re.findall(r"[s][hz]\d{6}", href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
            #有关上面一行代码：实际上得到的内容为>XX(该网页上是两个汉字)</dt>,[1,-5]代表的就是选取那两个汉字
            try:
                val = re.findall(r'\d+\.?.*</dd>', valueList[i])[0][0:-5]
            except:
                val = '--'
            infoDict[key] = val

        infoDict.update(
            {'股票名称':re.findall(r'\s.*\(', name)[0].split()[0] + \
            re.findall(r'\>.*\<', name)[0][1:-1]}   #尖括号似乎可以不转义
        )
        yield infoDict
