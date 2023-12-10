from . import views

from django.urls import path

urlpatterns = [
    path('run', views.insta_login),
]
