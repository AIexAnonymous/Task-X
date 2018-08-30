# -*- coding: utf-8 -*-
from django.shortcuts import render
from pymongo import MongoClient
client = MongoClient()
db = client.ALEX
 
# 接收POST请求数据
def welcome(request):
    return render(request, "welcome.html")
def questionnaire(request):
    data={}
    if request.POST:
        data['姓名'] = request.POST.get('user')
        data['性别'] = request.POST.get('sex')
        data['Q1'] = request.POST.get('Q1')
        data['Q2'] = request.POST.get('Q2')
        data['Q3'] = request.POST.get('Q3')
        data['Q4'] = request.POST.get('Q4')
        db.info.insert(data)
        client.close()
    return render(request, "post.html", data)
def OK(request):
    data = {}
    if request.POST:
        data['姓名'] = request.POST.get('user')
        data['性别'] = request.POST.get('sex')
        data['Q1'] = request.POST.get('Q1')
        data['Q2'] = request.POST.get('Q2')
        data['Q3'] = request.POST.get('Q3')
        data['Q4'] = request.POST.get('Q4')
        db.info.insert(data)
        client.close()
    return render(request, "ok.html")
def test(request):
    data={}
    if request.POST:
        data['姓名'] = request.POST.get('user')
        data['性别'] = request.POST.get('sex')
        db.info.insert(data)
        client.close()
    return render(request, "test.html", data)
