from django.contrib import admin
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('',views.ProjectListView.as_view(),name='all'),
    path('new/',views.CreateProjectView.as_view(),name='new'),
    path('<slug:slug>/',views.ProjetDetailView.as_view(),name='single'),
    path('<slug:slug>/delete/',views.ProjectDeleteView.as_view(),name='delete'),
    path('<str:username>',views.UserProjectList.as_view(),name='user_all'),
]
