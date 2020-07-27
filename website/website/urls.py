from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),

    path("markdownx/", include("markdownx.urls")),
    
    path("", include("landing.urls")),
    path("blog/", include("blog.urls"))
]
