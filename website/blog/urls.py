from django.urls import path
from blog import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("create", views.PostCreateView.as_view(), name="post-create"),
    path("update/<pk>", views.PostEditView.as_view(), name="post-edit"),
    path("<slug:slug>/", views.post_detail, name="post-detail"),
]
