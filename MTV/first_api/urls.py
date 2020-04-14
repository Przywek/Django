from django.contrib import admin
from django.urls import path
from first_api import views
urlpatterns = [
  path('',views.users, name='index'),
]