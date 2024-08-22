from django.urls import path
from .views import *
urlpatterns=[
 path('seal/',seal,name='seal'),
 path('index/',index,name='index'),
 path('login/',login,name='login'),
 path('logging/',logging,name='logging')   
]