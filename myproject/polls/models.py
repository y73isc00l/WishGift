from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Personuser(models.Model):
	username=models.CharField(max_length=50,null=True)
	email=models.EmailField(max_length=254,null=True)
	firstname=models.CharField(max_length=20,default="foo")
	lastname=models.CharField(max_length=20,default="bar")
	address=models.CharField(max_length=100,blank=True)
	city=models.CharField(max_length=50,null=True)
	state_province=models.CharField(max_length=30,null=True)
	country=models.CharField(max_length=50,null=True)
class Wishes(models.Model):
	wishitem=models.CharField(max_length=100,null=True)
	occassion=models.CharField(max_length=100,null=True)
	occasion_date=models.DateField()
	descriptionwish=models.CharField(max_length=100,blank=True)
	user=models.ForeignKey(Personuser)
	
class Friend(models.Model):
	user=models.ForeignKey(Personuser)
	wishes=models.ManyToManyField(Wishes)
	username=models.CharField(max_length=50,null=True)
	email=models.EmailField(max_length=254,null=True)
