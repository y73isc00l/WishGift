from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpRequest
from django.contrib.auth import authenticate, login,logout

##from models import Personuser
def login(request):
	if request.user.is_authenticated:
		logout(request)
	mlst=[]
	passwdmatch=False
	usernameunique=False
	if request.POST:
		try:
		#	p=Personuser.objects.get(email=request.POST['email'])
			user=User.objects.get(email=request.POST['email'])
			return render(request,'signup.html',{'message':('The account already exists',)})
		except User.DoesNotExist:
			try:
				tmp=User.objects.get(username=request.POST['username'])
			except User.DoesNotExist:
				tmp=None	
			if request.POST['passwd']==request.POST['confirmpasswd']:passwdmatch=True
			else:mlst.append('The passwords do not match.')
			if not tmp:usernameunique=True
			else:mlst.append('The username is already in use.')
			#	p=Personuser.objects.create(email=request.POST['email'],passwd=request.POST['passwd'],
			#									username=request.POST['username'])
			if usernameunique and passwdmatch:
				user=User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['passwd'])
				return render(request,'login.html',{'message':'The account was successfully created'})
			else:
				return render(request,'signup.html',{'message':mlst}) 
	elif not request.POST:
		return render(request,'login.html')
def fblogin(request):
	
	return render(request,'facebooklogin.html')
def signup(request):
	return render(request,'signup.html')
