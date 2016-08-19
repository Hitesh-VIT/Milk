from django.conf.urls import *
from . import views
urlpatterns=patterns('',
url(r'^miss',views.update,name='update date'),
url(r'^register',views.main_site,name='login form'),
url(r'^milk/index',views.main_page,name='Milk_homepage'),
url(r'^adminview',views.AdminMilk,name='MilkUsername'),
url(r'^login',views.main_site)
)
