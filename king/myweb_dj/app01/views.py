from django.shortcuts import render, HttpResponse
from django.urls import reverse
import os
# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

from django.shortcuts import HttpResponse
from app01 import models

sortDir1 = []
sortDir2 = []
sortDir3 = []
BASE_DIR = os.getcwd()
DATA_BASE = os.path.join(BASE_DIR, 'static', 'myData')

sortDir1 = os.listdir(DATA_BASE)
sortDir1.sort(key=lambda x: int(x[:2]))  # 按前两位数字排序


'''获取当前用户名'''
def getUserName(request):
    if models.UserInfo.objects.filter(username=request.session.get('username', None)):
        user_name = '欢迎，' + request.session.get('username', None)
    else:
        user_name = "游客，请登录"
    return user_name

'''登录'''
def login(request):
    error_msg = ''
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        if models.UserInfo.objects.filter(username=user, password=pwd):
            request.session.setdefault('username', user)
            request.session.setdefault('is_login', True)
            request.session.set_expiry(60*60*24*15)
            request.session['username'] = user
            return redirect('/index/')
        else:
            error_msg = "用户名或密码错误!"
    return render(request, 'login.html', {'error_msg': error_msg})

'''主页'''
def index(request):
    userName = getUserName(request)
    return render(request, 'index.html', {'user_head': userName})

'''后台用户管理'''
def user(request):
    mesinfo = ''
    userList = models.UserInfo.objects.all()
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        user_type = request.POST.get('user_type', None)
        if not user_type:
            user_type = 1
        if user and pwd:
            if models.UserInfo.objects.filter(username=user).first() == None:
                models.UserInfo.objects.create(username=user, password=pwd, user_type=user_type)
                mesinfo = '创建成功'
            else:
                mesinfo = '用户名重复'
        else:
            mesinfo = '请填写用户名和密码'
        return render(request, 'user.html', {"userList": userList, "mesinfo": mesinfo})
    else:
        # if 1:
        if models.UserInfo.objects.all().count() == 0:  # 数据库为空时直接返回创建用户界面
            return render(request, 'user.html', {"userList": userList, "mesinfo": mesinfo})
        else:
            if not request.session.get('username', None):
                return render(request, '404.html')
            else:
                if models.UserInfo.objects.filter(username=request.session.get('username', None))[0].user_type > 99:
                    return render(request, 'user.html', {"userList": userList, "mesinfo": mesinfo})
                else:
                    userName = getUserName(request)
                    return render(request, '404.html',{'user_head': userName})

'''删除用户'''
def userdel(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/')

'''错误返回'''
def error404(request):
    userName = getUserName(request)
    return render(request, '404.html', {'user_head': userName})

'''显示内容'''
def displayContent(request, nid, urlToView):
    userName = getUserName(request)
    title = ''
    list = urlToView.split('-')  # 注：最后'-'后也算一个空字符，占一个长度
    if len(list) == 3:  # 一层目录
        pathName1 = os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1])
        pathName_t = pathName1
    elif len(list) == 4:  # 二层目录
        sortDir2 = os.listdir(os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1]))
        sortDir2.sort()  # 按前两位数字排序
        pathName2 = os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1], sortDir2[int(list[2]) - 1])
        pathName_t = pathName2
    if os.path.exists(pathName_t):
        files = os.listdir(pathName_t)  # 文件夹下所有目录的列表
        files.sort()
        if urlToView[0:3] == 'pdf':
            title = files[int(nid)].replace('.pdf', '')
            return render(request, 'pdfDisplay.html', {"note_title": title, 'user_head': userName, 'nid': nid, 'urlToView': urlToView})
        elif urlToView[0:3] == 'txt':
            title = files[int(nid)].replace('.txt', '')
            return render(request, 'txtDisplay.html', {"note_title": title, 'user_head': userName, 'nid': nid, 'urlToView': urlToView})
    else:
        return HttpResponse('读取失败')


def videoDisplay(request):
    title = ""
    userName = getUserName(request)
    return render(request, 'videoDisplay.html', {"note_title": title, 'user_head': userName})



'''ajax生成目录'''
import json
def ajax_menu_dir(request):
    ret = request.GET.get('arg1')  # menu_01
    sortDir1 = ['',]
    sortDir2 = ['',]
    list = ret.split('_')
    if len(list) >= 2:  # menu_01
        sortDir1 = os.listdir(DATA_BASE) # menu_01
        sortDir1.sort()  # 按前两位数字排序
        sortDir2 = os.listdir(os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1]))
        sortDir2.sort()  # 按前两位数字排序
    return HttpResponse(json.dumps(sortDir2))

# def ajax_menu_files(request):
#     return HttpResponse('kkkkk')

def ajax_menu_files(request):
    arg = request.GET.get('arg1')  # menu_01
    tag = ""
    list = arg.split('_')
    if len(list) == 3:  # 一层目录
        pathName1 = os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1])
        pathName_t = pathName1
    elif len(list) == 4:  # 二层目录
        sortDir2 = os.listdir(os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1]))
        sortDir2.sort()  # 按前两位数字排序
        pathName2 = os.path.join(DATA_BASE, sortDir1[int(list[1]) - 1], sortDir2[int(list[2]) - 1])
        pathName_t = pathName2

    if arg[-1] == 'd':  # 末尾d代表课件，v代表视频
        if os.path.exists(pathName_t):
            files = os.listdir(pathName_t)  # 文件夹下所有目录的列表
            files.sort()
            for index in range(len(files)):
                if os.path.isfile(pathName_t + '/' + files[index]):  # 这里是绝对路径，该句判断目录是否是文件
                    if files[index][-4:] == '.pdf':
                        tag += '<li><a title="'+ files[index] + '"'+ ' style="cursor: pointer;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;" href="/pdf-' + arg.replace('_d', '').replace('menu_', '').replace('_',
                                                                                                         '-') + '-' + str(
                            index) + '"' + '>' + files[index] + '</a></li>'
                    if files[index][-4:] == '.txt':
                        tag += '<li><a title="'+ files[index] + '"'+ ' style="cursor: pointer;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;" href="/txt-' + arg.replace('_d', '').replace('menu_', '').replace('_',
                                                                                                         '-') + '-' + str(
                            index) + '"' + '>' + files[index] + '</a></li>'
        else:
            print(pathName_t, '路径错误')
    if arg[-1] == 'v':  # 末尾d代表课件，v代表视频
        videoPathName = os.path.join(pathName_t, 'video', 'video_json')
        if os.path.isfile(videoPathName):
            with open(videoPathName, 'r', encoding='utf-8') as f:
                jsonList = json.load(f)
            for list in jsonList:
                tag += '<li><a href="/videourl" style="cursor: pointer;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;" title=' + \
                       list[0] + '>' + list[0] + '</a></li>'
        else:
            print(videoPathName, '路径错误')

    return HttpResponse(tag)