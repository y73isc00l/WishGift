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
#module to display the dashboard of authenticated user
def Dashboard01(request):
        if request.user.is_authenticated:
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
##module responsible for search results 
def Dashboard01search(request):
	q=request.GET['searchbar']
	userslst=User.objects.filter(username__icontains=q)
	message='Try searching for someone else.'
	return render(request,'search.html',{'searchresult':userslst,'message':message})
##module to addwish
@login_required(login_url='/login/')
def Dashboard01addwish(request):
	tmp=User.objects.get(username=request.user)
	try:
		wishcheck=tmp.wishes_set.get(wishitem=request.POST['wish'])
	except Wishes.DoesNotExist:
		m=hashlib.md5()
		tmp.wishes_set.create(wishitem=request.POST['wish'],occassion=request.POST['occassion'],occassion_date=datetime.date.today(),descriptionwish=request.POST['descriptionwish'],pub_date=datetime.date.today())
		w=tmp.wishes_set.get(wishitem=request.POST['wish'])
		m.update(w.wishitem)
		m.update(str(w.id))
		w.hashid=m.hexdigest()
		w.save()
	return render(request,'dashboard.html',{'user':tmp,'wishes':tmp.wishes_set.all(),'friend':tmp.friend_set.all()})

##module to delete a wish
@login_required(login_url='/login/')
def Dashboard01delwish(request,hashid):
	tmp=User.objects.get(username=request.user)
	try:
		wish=Wishes.objects.get(hashid=hashid)
		wish.delete()
	except Wishes.DoesNotExist:
		msg='The wish does not exist'
	return render(request,'dashboard.html',{'user':tmp,'wishes':tmp.wishes_set.all(),'friend':tmp.friend_set.all()})

##module to edit wish will be implemented only in later stages
@login_required(login_url='/login/')
def Dashboard01editwish(request,hashid):
	tmp=User.objects.get(username=request.user)
	#code to be filled
	return render(request,'dashboard.html',{'user':tmp,'wishes':tmp.wishes_set.all(),'friend':tmp.friend_set.all()})

##module to grant wish to person whose profile is being used
def Dashboard01grantwish(request,usrname,hashid):
	tmp=User.objects.get(username=request.user)
	try:
		p=User.objects.get(username=usrname)
	except User.DoesNotExist:
		return render(request,'person_view.html',{'personusername':'Sorry, try searching for someone in our records'})
	try:
		wish=Wishes.objects.get(hashid=hashid)
	except Wishes.DoesNotExist:
		return render(request,'person_view.html',{'personusername':'Sorry, the user does not have that wish'})
	if request.user.is_authenticated:
		try:
# 			userasfriend=p.friend_set.get(email=tmp.email)
# 			userasfriend.friend.add(wish)
			pisfriend=tmp.friend_set.get(email=p.email)
			pisfriend.wishes.add(wish)
			wish.isgranted=True
			wish.save()
# 			wish.update
			return render(request,'person_view.html',{'personusername':p.username,'wishes':p.wishes_set.all()})			
		except :
			return render(request,'person_view.html',{'personusername':p.username,'wishes':p.wishes_set.all(),'message':'You must be friends with user.'})
	else:
		return render(request,'person_view.html',{'personusername':p.username,'wishes':p.wishes_set.all(),'message':'You must login first.'})

##module to add friend	
def Dashboard01addfriend(request,usrname):
	try:
		p=User.objects.get(username=usrname)
	except User.DoesNotExist:
		return render(request,'person_view.html',{'personusername':'Sorry, try searching for someone in our records'})
	if request.user.is_authenticated:
		user=User.objects.get(username=request.user)
		try:
			user.friend_set.create(email=p.email)
			return render(request,'person_view.html',{'personusername':p.username,'wishes':p.wishes_set.all()})
		except IntegrityError:
			return render(request,'person_view.html',{'personusername':p.username,'wishes':p.wishes_set.all()})
	else:
		return render(request,'person_view.html',{'personusername':p.username,'wishes':p.wishes_set.all(),'message':'You must login first.'})
def logout_view(request):
	logout(request)
	return render(request,'logout.html')
def person_viewprofile(request,usrname):
	try:
		p=User.objects.get(username=usrname)
		return render(request,'person_view.html',{'personusername':p.username,'wishes':p.wishes_set.all()})	
	except User.DoesNotExist:
		return render(request,'person_view.html',{'personusername':'Sorry, try searching for someone in our records'})
		




