"""
Definition of urls for InfoVisProject.
"""

from datetime import datetime
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from VisualApp import forms, views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^canada_climate', views.climate, name='climate')]
