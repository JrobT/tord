from django.urls import path
from django.contrib import admin
from landing import views


urlpatterns = [path("", views.AboutView.as_view(), name="landing")]
