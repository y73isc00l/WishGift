from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
##from models import Personuser,Wishes,Friend
import hashlib
from models import Wishes,Friend
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import datetime
@login_required(login_url='/login')
def poolwelcome(request):
  return render(request,'poolwelcome.html')
def joinpool(request):
  return render(request,'joinpool.html')
def createpool(request):
  return render(request,'createpool.html')