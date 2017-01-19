from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
##from models import Personuser,Wishes,Friend
from models import Wishes,Friend
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
'''def Dashboard(request):
        emailform=''
        passwdform=''
        personcreated=False
        if 'email' in request.POST and 'passwd' in request.POST:
                emailform=request.POST['email']
                passwdform=request.POST['passwd']               
                try:
                        p=Personuser.objects.get(email=emailform,passwd=passwdform)
                except Personuser.DoesNotExist:
                        message_failure="The details are incorrect"
                        return render(request,'login.html',{'message':message_failure})
        personcreated=True
        return render(request,'dashboard.html',{'user':p,'wishes':p.wishes_set.all(),'friends':p.friend_set.all()})'''
def Dashboard01(request):
        if request.user.is_authenticated():
                tmp=User.objects.get(username=request.user)
        	return render(request,'dashboard.html',{'user':tmp,'wishes':tmp.wishes_set.all(),'friend':tmp.friend_set.all()})
        else:
                mail=request.POST['email']
                password=request.POST['passwd']
                try:
                        tmp=User.objects.get(email=mail)
                        username=tmp.username
                except User.DoesNotExist:
                        return render(request,'login.html',{'message':'The details are incorrect'})
                user=authenticate(username=username,password=password)
                if user is not None:
                        if user.is_active:
                                login(request,user)
                                return render(request,'dashboard.html',{'user':tmp,'wishes':tmp.wishes_set.all(),'friend':tmp.friend_set.all()})
                        else:
                                return render(request,'login.html',{'message':'You must log in'})
                else:
                        return render(request,'login.html',{'message':'The password entered is incorrect'})
@login_required(login_url='/login/')
def Dashboard01addwish(request):
	tmp=User.objects.get(username=request.user)
	try:
		wishcheck=tmp.wishes_set.get(wishitem=request.POST['wish'])
	except Wishes.DoesNotExist:
		tmp.wishes_set.create(wishitem=request.POST['wish'],occassion=request.POST['occassion'],occassion_date=datetime.date.today(),descriptionwish=request.POST['descriptionwish'],pub_date=datetime.date.today())
	return render(request,'dashboard.html',{'user':tmp,'wishes':tmp.wishes_set.all(),'friend':tmp.friend_set.all()})

def logout_view(request):
	logout(request)
	return render(request,'logout.html')
