from django.shortcuts import render
from django.template import Template,Context
import datetime
# Create your iviews here.
from django.http import HttpResponse
import codecs
def welcome(request,name):
	fp=open("/home/demo/myproject/polls/hello.html")
	fp.seek(0)
	t=Template(''.join(fp.read().splitlines()))
	fp.close()
	c=Context({'name':name})
	return HttpResponse(t.render(c))
def index(request):
	return HttpResponse("Hello,World u are at the poll index page number ")
def home(request):
	return HttpResponse("This is the home page and is under development")
def timeafter(request,offset):
	now=datetime.datetime.now()
	try:
		offset=int(offset)
	except ValueError:
		raise Http404();
	after=now+datetime.timedelta(hours=offset)
	html="After %s hours it will be %s."%(offset,after)
	return HttpResponse(html+"\nThe time displayed  here is UTC")
