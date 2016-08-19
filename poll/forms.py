from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from poll.models import Miss,Profile
class LoginForm(UserCreationForm):
	email=forms.EmailField(required=True)
	class Meta:
		model=User
		fields=['username','email','password1','password2']
	def save(self,commit=True):
		user=super(LoginForm,self).save(commit=False)
		user.email=self.cleaned_data['email']
		if commit:
			user.save()
		return user
class LogForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		fields = ['username', 'password'] 
class Missform(forms.ModelForm):
	class Meta:
		exclude=['username']
		model=Miss
class Milkform(forms.ModelForm):
	class Meta:
		model=Profile
		fields='__all__'
		exclude=['username']


	
