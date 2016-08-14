from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from poll.models import Miss,Profile
class LoginForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email']
class Missform(forms.ModelForm):
	class Meta:
		exclude=['username']
		model=Miss
class Milkform(forms.ModelForm):
	class Meta:
		model=Profile
		fields='__all__'
		exclude=['username']
class Login_inForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password']

	
