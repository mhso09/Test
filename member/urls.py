from django.urls import path
from . import views

urlpatterns = [
    path('member_register', views.member_register, name='member_register'), 
    path('member_idcheck', views.member_idcheck, name='member_idcheck'), #아이디 중복체크
    path('member_insert', views.member_insert, name='member_insert'),
]
