from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Package urls
    path("markdownx/", include("markdownx.urls")),
    path("", include("blog.urls")),
]
