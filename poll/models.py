from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Milk_Exclude(models.Manager):
	def get_queryset(self):
		return super(Milk_Exclude,self).get_queryset().exclude(date=datetime.today())
class Milk_Include(models.Manager):
	def get_queryset(self):
		return super(Milk_Include,self).get_queryset().include(date=datetime.today())	
class Bill_Milk(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	date=models.DateField(blank=True)
	objects=models.Manager()
	M_today=Milk_Include
	
class Miss(models.Model):
	username=models.CharField(max_length=250,default=0)
	date=models.DateField()
	
class Missed(models.Model):
	user=models.ForeignKey(User,unique=False,on_delete=models.CASCADE)
	date=models.DateField(blank=True)
	
class Profile(models.Model):
	username=models.CharField(max_length=250,default=0,primary_key=True)
	milk=models.IntegerField(default=0)



	
