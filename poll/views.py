from django.shortcuts import render,redirect,render_to_response
from .forms import Missform,LoginForm,Milkform,LogForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from poll.models import Miss,Profile
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm


def main_page(request):
	return HttpResponse('poll/index.html')
def login_for(request):
	if request.method== 'POST':
		lo=LoginForm(request.POST)
		if lo.is_valid():
			lo.save()
			return redirect('login')
		else:
			messages.error(request,('Please correct the error below.'))
	else:
		lo = LoginForm(request.POST)
		
			
	return render(request,'poll/milk_login.html',{
	'lo':lo
	})
	


@login_required(login_url='login form')
def update(request):
	if request.method == 'POST':
		user_form=Missform(request.POST )
		if user_form.is_valid():
			usr_form=user_form.save()
			usr_form.username=request.user.username		
			usr_form.save()
	        return redirect('update date')
	else:
		user_form = Missform(instance=request.user)
	if request.method == 'POST':
		milk_form=Milkform(request.POST)
		if milk_form.is_valid():
			milk=milk_form.save()
			milk.username=request.user.username
			milk.save()
			return redirect('update date')
		else:
			messages.error(request,('Please correct the error below.'))
	else:
		milk_form = Milkform(instance=request.user)
	return render(request,'poll/milk.html',{'user_form':user_form,'milk_form':milk_form})
	
	
def main_site(request):
	if request.method== 'POST':
		login_form=LogForm(request.POST)
		
		lo=LoginForm(request.POST)
		
		if login_form.is_valid():
			username=login_form.cleaned_data['username']
			password=login_form.cleaned_data['password']
			user= authenticate(username=username, password=password)
			
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('update date')
		if lo.is_valid():

			user=lo.save()
			
			
			user= authenticate(username=lo.cleaned_data.get('username'),password=lo.cleaned_data.get('password1'))
			
			
			if user is not None:
				
				if user.is_active:
					login(request,user)
					return redirect('update date')
			
			
			else:
				messages.error(request,('Please correct the error below.'))
	else:
		lo = LoginForm(request.POST)
		login_form=LogForm(request.POST)
	return render(request,'poll/index.html',{'login_form':login_form,'lo':lo})
	
	
			
def AdminMilk(request):
	l=[]
	m=Miss.objects.filter(date=datetime.now())
	for e in m:
		l.append(e.username)
	
	l1=[]
	m1=User.objects.all()
	for e in m1:
		l1.append(e.username)
	lew=set(l1)-set(l)
	final=list(lew)
	return render(request,'poll/admin-view.html',{'my_list':final})
			
			
	
	
	
	
		
	
