from django.shortcuts import render


# Create your iviews here.
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello,World u are at the poll index page number ")
def home(request):
	return HttpResponse("This is the home page and is under development")
