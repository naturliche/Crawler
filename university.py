# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 17:35:20 2020

@author: natur
"""


#输出排版问题，中英文空格不同，默认为英文空格，所以采用chr(12288)作为设置中文空格
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

#将url的html页面放入一个list列表
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    #每一个tr为一所大学对应的信息
    for tr in soup.find('tbody').children:
        #可能出现字符串类型，tr为标签类型，过滤掉为非标签类型
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')  #存为列表
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
            

#将ulist中的多少个元素进行打印
def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学习名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
        
    

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo,20)
main()
