from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect


def main_page(request):
	return redirect('login form')
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('login')
