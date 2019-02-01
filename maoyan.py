#pycharm

import json
import requests
from lxml import etree

def getOnePage(n):
    url = 'http://maoyan.com/board/4?offset={}'.format((n-1)*10)
    header = {'user=agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    #调用
    r = requests.get(url,headers=header)
    #输出 http 状态码
    #print(r)
    #打印文本 F12
    #print(r.text)
    return r.text         #返回文本

#data = getOnePage(20)

#print(data)

def parse(text):

    #初始化 标准化
    html = etree.HTML(text)
    #提取 需要些xpath语法
    #names是列表，xpath返回列表
    names = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')

    releasetimes = html.xpath('//p[@class="releasetime"]/text()')
    item = {}  # dict
    #zip是拉链函数
    for name,releasetime in zip(names,releasetimes):
        print(name,releasetime)
        #字典
        item['name'] = name
        item['releasetime'] = releasetime
        #生成器 循环迭代
        yield item
    #print(names)
    #print(releasetimes)

#保存数据
def save2File(data):
    with open('movie.json','a',encoding='utf-8') as f:
        #把字典 列表 转化成字符串
        data = json.dumps(data,ensure_ascii=False) + ',\n'
        f.write(data)

def run():
    for i in [1,2,3,4,5,6,7,8,9,10]:
        text = getOnePage(i)          #直接输入页码即可
        items = parse(text)
        for item in items:
            save2File(item)

if __name__ == '__main__':
    run()