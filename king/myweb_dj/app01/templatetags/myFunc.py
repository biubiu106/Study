
import os
from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from app01 import models


register = template.Library()

BASE_DIR = os.getcwd()
DATA_BASE = os.path.join(BASE_DIR, 'static', 'myData')
TAG_BASE = '../static/myData/'


sortDir1 = []
sortDir2 = []
sortDir3 = []

sortDir1 = os.listdir(DATA_BASE)
sortDir1.sort()  # 按前两位数字排序


import json
@register.simple_tag
def func_left_menu(arg): # arg: menu_01_01_d/menu_01_01_v
    tag = ""
    list = arg.split('_')
    if len(list) == 3: # 一层目录
        pathName1 = os.path.join(DATA_BASE, sortDir1[int(list[1])-1])
        pathName_t = pathName1
    elif len(list) == 4: # 二层目录
        sortDir2 = os.listdir(os.path.join(DATA_BASE, sortDir1[int(list[1])-1]))
        sortDir2.sort()  # 按前两位数字排序
        pathName2 = os.path.join(DATA_BASE, sortDir1[int(list[1])-1], sortDir2[int(list[2])-1])
        pathName_t = pathName2

    if arg[-1] == 'd':  # 末尾d代表课件，v代表视频
        if os.path.exists(pathName_t):
            files = os.listdir(pathName_t)  # 文件夹下所有目录的列表
            files.sort()
            for index in range(len(files)):
                if os.path.isfile(pathName_t + '/' + files[index]):  # 这里是绝对路径，该句判断目录是否是文件
                    if files[index][-4:] == '.pdf':
                        tag += '<li><a href="/pdf-' + arg.replace('_d', '').replace('menu_', '').replace('_','-') + '-' + str(index) + '"' + '>' + files[index][:-4] + '</a></li>'
                    if files[index][-4:] == '.txt':
                        tag += '<li><a href="/txt-' + arg.replace('_d', '').replace('menu_', '').replace('_','-') + '-' + str(index) + '"' + '>' + files[index][:-4] + '</a></li>'
        else:
            print(pathName_t, '路径错误')
    if arg[-1] == 'v':  # 末尾d代表课件，v代表视频
        videoPathName = os.path.join(pathName_t, 'video', 'video_json')
        if os.path.isfile(videoPathName):
            with open(videoPathName, 'r', encoding='utf-8') as f:
                jsonList = json.load(f)
            for list in jsonList:
                tag += '<li><a href="/videourl" style="cursor: pointer;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;" title=' + list[0] + '>' + list[0] + '</a></li>'
        else:
            print(videoPathName, '路径错误')

    tag = mark_safe(tag)
    return tag


# 目前仅支持pdf和txt两种格式文件
@register.simple_tag
def contentDisplay(nid, urlToview): # urlToview: pdf-10-01-
    tag = ''
    fileName = ''
    list = urlToview.split('-') # 注：最后'-'后也算一个空字符，占一个长度
    if len(list) == 3:  # 一层目录
        pathName1 = os.path.join(DATA_BASE, sortDir1[int(list[1])-1])
        TagChar = TAG_BASE + sortDir1[int(list[1]) - 1] + '/'
        pathName_t = pathName1
    elif len(list) == 4:  # 二层目录
        sortDir2 = os.listdir(os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1]))
        sortDir2.sort()  # 按前两位数字排序

        pathName1 = os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1])
        pathName2 = os.path.join(DATA_BASE, sortDir1[int(list[1])-1], sortDir2[int(list[2]) - 1])
        sortDir3 = os.listdir(pathName1)
        sortDir3.sort()  # 按前两位数字排序
        TagChar = TAG_BASE + sortDir1[int(list[1])-1] + '/' + sortDir3[int(list[2])-1] + '/'
        pathName_t = pathName2

    if os.path.exists(pathName_t):
        files = os.listdir(pathName_t)  # 文件夹下所有目录的列表
        files.sort()  # 按前两位数字排序
        fileName = files[int(nid)] # 获取文件名
        if urlToview[0:3] == 'pdf':
            tag = '<embed id="pdfDiv" width="100%" src="'+ TagChar + fileName + '"'+ ' />'
        elif urlToview[0:3] == 'txt':
            with open(os.path.join(pathName_t, fileName), 'r', encoding='utf-8') as f:
                tag = f.read().replace("\n", '<br/>').replace("\r", '&nbsp').replace('	','&nbsp&nbsp&nbsp&nbsp')
    else:
        print(pathName_t, '路径错误')

    tag = mark_safe(tag)
    return tag


###第一层目录
@register.simple_tag
def left_menu_text(arg):
    # menu_01
    list = arg.split('_')
    name = sortDir1[int(list[1])-1]
    return name

