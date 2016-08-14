from django.conf.urls import *
from . import views
urlpatterns=patterns('',

url(r'^miss',views.update_date,name='update date'),
url(r'^register',views.login_for,name='login form'),
url(r'^milk',views.update_milk,name='Milk update'),
url(r'^milk/index',views.main_page,name='Milk_homepage'),
url(r'^login',views.login_in,name='login_milk'),
url(r'^adminview',views.AdminMilk,name='MilkUsername')
)
