#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '
import mysql.connector
import re, time, json, logging, hashlib, base64, asyncio
import urllib
from urllib import request
from aiohttp import web
import json
from coroweb import get, post
@get('/')
def register():
    return {
        '__template__': 'register.html'
    }

@post('/api/users')
def api_register_user(*,name):
    conn = mysql.connector.connect(user='root', password='root', port='3305', database='awesome')
    cursor = conn.cursor()
    cursor.execute('truncate table urllist ')
    name='https://www.liaoxuefeng.com/wiki/'+name
    cursor.execute('insert into urllist (id,url) values (%s, %s)', [2,name])
    conn.commit()
    cursor.close()
    savevalue()
    return


def getHtml(url):
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Referer': r'https://www.liaoxuefeng.com/',
        'Connection': 'keep-alive'
    }
    req = request.Request(url, headers=headers)
    html = urllib.request.urlopen(url ,proxies={'http':'http://183.190.26.154'}).read()
    print(html)
getHtml('https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000')

def getURL(html):
    reg = r'/wiki/\w+/\w+'
    URLre = re.compile(reg)
    html = html.decode('utf-8')  # python3
    URLlist = URLre.findall(html)
    URL = URLlist[:123]
    return URL


def getNumber(html):
    reg = r'<span>Reads: (\d+)</span>'
    Numbere = re.compile(reg)
    html = html.decode('utf-8')  # python3
    Numberlist = Numbere.findall(html)
    return Numberlist

def testUrl(x): #抓取测试网址
    htmlx = getHtml(x)
    contentA = getURL(htmlx)
    x=0
    ListNumber = []
    while x<123 :
        contentA[x]='https://www.liaoxuefeng.com'+contentA[x]
        contentB = getHtml(contentA[x])
        Number=getNumber(contentB)
        ListNumber.append(Number[0])
        x=x+1
    xvalue = list(range(122))
    yvalue = ListNumber

def savevalue():
    conn = mysql.connector.connect(user='root', password='root',port='3305', database='awesome')
    cursor = conn.cursor()
    cursor.execute('select url from urllist where id = %s', ('2',))
    waiteurl=cursor.fetchall()
    wurl=waiteurl[0][0]
    print(wurl)
    htmlx = getHtml(wurl)
    contentA = getURL(htmlx)
    x = 1
    ListNumber = []
    cursor.execute('truncate table ech ')
    while x<123:
        contentA[x]='https://www.liaoxuefeng.com'+contentA[x]
        contentB = getHtml(contentA[x])
        Number=getNumber(contentB)
        cursor.execute('insert into ech (id,yvalue) values (%s, %s)', [ x, Number[0]])
        x=x+1
    cursor.execute('truncate table urllist ')
    conn.commit()
    cursor.close()
    print('svaeSuccess')

@get('/api/create')
def create_x_y():
    conn = mysql.connector.connect(user='root', password='root', port='3305', database='awesome')
    cursor = conn.cursor()
    cursor.execute('select yvalue from ech')
    listyvalue=cursor.fetchall()
    yvalue = []
    x=0
    Jresult=[]
    while x<len(listyvalue):
        yvalue.append(listyvalue[x][0])
        x=x+1
    xvalue=list(range(1, len(listyvalue)))
    conn.commit()
    cursor.close()
    jresult=[xvalue,yvalue]
    return  jresult

