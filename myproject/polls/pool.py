from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
##from models import Personuser,Wishes,Friend
import hashlib
from models import Wishes,Friend,Pool
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import datetime
@login_required(login_url='/login')
def poolwelcome(request):
  return render(request,'poolwelcome.html')
@login_required(login_url='/login/')
def joinpool(request):
  return render(request,'joinpool.html')
@login_required(login_url='/login/')
def pooldashboard(request):
  tmp=User.objects.get(username=request.user)
  try:
    pool=Pool.objects.get(poolname=request.POST['poolname'])
    return render(request,'createpool.html',{'message':'Try another name'})
  except:
    minamt=int(request.POST['minprice'])
    maxamt=int(request.POST['maxprice'])
    #poolsize=int(request.POST['poolsize'])
    Pool.objects.create(poolname=request.POST['poolname'],recipient=request.POST['recipient'],occassion=request.POST['occasion'],occassion_date=datetime.date.today(),minamt=minamt,maxamt=maxamt)
    pool=Pool.objects.get(poolname=request.POST['poolname'])
    if not request.POST['giftchoice01']:
      pool.giftopt01=request.POST['giftchoice01']
    if not request.POST['giftchoice02']:
      pool.giftopt02=request.POST['giftchoice02']
    if not request.POST['giftchoice03']:
      pool.giftopt03=request.POST['giftchoice03']
    tmp.pool_set.add(pool)
    tmp.save()
    pool.save()
    return render(request,'pooldashboard.html',{})
def dashboardview(request,poolname):
  return render(request,'<html></html>')
def createpool(request):
  return render(request,'createpool.html')