from django.urls import path
from django.contrib import admin
from blog import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.AboutView.as_view(), name="about"),
    path("blog", views.post_list, name="post-list"),
    path("create", views.PostCreateView.as_view(), name="post-create"),
    path("update/<pk>", views.PostEditView.as_view(), name="post-edit"),
    path("<slug:slug>/", views.post_detail, name="post-detail")
]
