from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''class Personuser(models.Model):
	username=models.CharField(max_length=50,null=True)
	passwd=models.CharField(max_length=64,null=True)
	email=models.EmailField(max_length=254,null=True)
	firstname=models.CharField(max_length=20,default="foo")
	lastname=models.CharField(max_length=20,default="bar")
	address=models.CharField(max_length=100,blank=True)
	city_county=models.CharField(max_length=50,blank=True)
	state=models.CharField(max_length=30,blank=True)
	country_residence=models.CharField(max_length=50,blank=True)
'''	
class Wishes(models.Model):
	wishitem=models.CharField(max_length=100,null=True)
	occassion=models.CharField(max_length=100,null=True)
	occassion_date=models.DateField(null=True)
	descriptionwish=models.CharField(max_length=100,blank=True)
	user=models.ForeignKey(User)
	pub_date=models.DateField(null=True)	
class Friend(models.Model):
	email=models.EmailField(null=True)
	wishes=models.ManyToManyField(Wishes)
	user=models.ForeignKey(User)
class Extradetails(models.Model):
	firstname=models.CharField(max_length=64,blank=True)
	lastname=models.CharField(max_length=64,blank=True)
	address=models.CharField(max_length=128,blank=True)
	city=models.CharField(max_length=128,blank=True)
	state=models.CharField(max_length=128,blank=True)
	country=models.CharField(max_length=128,blank=True)
	DOB=models.DateField(null=True)
	user=models.OneToOneField(User)
