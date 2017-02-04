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
def intelligiftsearch(request):
  return render(request,'giftsearch.html')