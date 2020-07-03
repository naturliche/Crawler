# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:57:22 2020

@author: natur
"""

import requests
import os
import random

def getHTMLText(url):
    try:
        r = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def getHTMLPic(url):
    try:
        r = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except:
        return ""
'''
#获取图片
def get_page(url):
    html = getHTMLText(url)
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)

    return html[a:b]
'''

def get_next_url(url):
    html = getHTMLText(url)
    a = html.find("previous-comment-page")-52
    b = html.find('"',a)
    return html[a:b]

def find_imgs(url):
    html = getHTMLText(url)
    
    img_addrs = [] #图片的地址
    a =  html.find('img src=')
    while a !=-1:
        b = html.find('.jpg',a,a+255)
        if b !=-1:
            img_addrs.append('http:'+ html[a+9:b+4])
        else:
            b = a +9

        a = html.find('img src=',b)

    return img_addrs

def save_imgs(img_addrs):
    
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open('./img/'+filename,'wb') as f:
            img = getHTMLPic(each)
            f.write(img)
            
def download(pages,url):
    #这个pages 的大小好像不影响爬的数量
    for i in range(pages):
        img_addrs = find_imgs(url)
        save_imgs(img_addrs)
        url = "http:"+get_next_url(url)
        
download(10,'http://jandan.net/ooxx/MjAyMDA3MDItMTA5#comments')