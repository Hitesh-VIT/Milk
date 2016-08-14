from django.shortcuts import render,redirect,render_to_response
from .forms import Missform,LoginForm,Milkform,Login_inForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from poll.models import Miss,Profile
from datetime import datetime

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
		
			
	return render(request,'poll/login.html',{
	'lo':lo
	})
	


@login_required
def update_date(request):
	if request.method == 'POST':
		user_form=Missform(request.POST )
		if user_form.is_valid():
			usr_form=user_form.save()
			usr_form.username=request.user.username		
			usr_form.save()
			
			
			return redirect('milk/index')
		else:
			messages.error(request,('Please correct the error below.'))
	else:
		user_form = Missform(instance=request.user)
	return render(request,'poll/miss.html',{'user_form':user_form})
@login_required
def update_milk(request):
	if request.method == 'POST':
		milk_form=Milkform(request.POST)
		if milk_form.is_valid():
			milk=milk_form.save()
			milk.username=request.user.username
			milk.save()
			return redirect('milk/index')
		else:
			messages.error(request,('Please correct the error below.'))
	else:
		milk_form = Milkform(instance=request.user)
	return render(request,'poll/milk_info.html',{'milk_form':milk_form})
def login_in(request):
	if request.method =='POST':
		milk_log=Login_inForm(request.POST)
		if  milk_log.is_valid():
			username=milk_log.username
			password=milk_log.password
			user = authenticate(username=username, password=password)
			if user is not none:
				login(request,user)
				return redirect('poll/miss')
			else:
				return redirect('/login')
	return render(request,'poll/milk_login.html',{'Login_inForm':Login_inForm})
		
def AdminMilk(request):
	l=[]
	m=Miss.objects.filter(date=datetime.now)
	for e in m:
		l.append(e.username)
	
	l1=[]
	m1=User.objects.all()
	for e in m1:
		l1.append(e.username)
	lew=set(l1)-set(l)
	final=list(lew)
	return render(request,'poll/Milk_admin.html',{'my_list':final})
			
			
	
	
	
	
		
	
