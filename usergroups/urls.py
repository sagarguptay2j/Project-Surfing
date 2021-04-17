from django.contrib import admin
from django.urls import path
from . import views

app_name = 'usergroups'

urlpatterns = [
    path('',views.UsergroupList.as_view(),name='all'),
    path('new/',views.CreateUsergroup.as_view(),name='new'),
    path('projects/in/<slug:slug>/',views.UsergroupDetail.as_view(),name='single'),
    path('join/<slug:slug>/',views.JoinUsergroup.as_view(),name='join'),
    path('leave/<slug:slug>/',views.LeaveUsergroup.as_view(),name='leave'),
]
