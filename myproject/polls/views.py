from django.shortcuts import render
import datetime
# Create your iviews here.
from django.http import HttpResponse
from django.http import HttpRequest
import codecs
def welcome(request):
	c={'name':'User'}
	return render(request,'dashboard.html',c)
def index(request):
	return HttpResponse("Hello,World u are at the poll index page number ")
def home(request):
	return render(request,'home.html',{})
def timeafter(request,offset):
	now=datetime.datetime.now()
	try:
		offset=int(offset)
	except ValueError:
		raise Http404();
	after=now+datetime.timedelta(hours=offset)
	html="After %s hours it will be %s."%(offset,after)
	return HttpResponse(html+"\nThe time displayed  here is UTC")
def contactus(request):
	peoplelst=[]
	peoplelst.append(['Rachit','Developer',r'rachittibrewal@gmail.com','+918141633867'])
	peoplelst.append(['Jugal','Designer',r'choksi.jugal@gmail.com','+919940338082'])
	return render(request,'contact.html',{'people':peoplelst})
def display_meta(request):
	metadict=request.META.items()
	metadict.sort()
	return render(request,'display_meta.html',{'metadata':metadict})
def login(request):
	return render(request,'login.html',{})
	
