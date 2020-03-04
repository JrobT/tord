from django.urls import path
from blog.views import PostListView, PostCreateView, PostDetailView, PostEditView


urlpatterns = [
    path("create", PostCreateView.as_view(), name="post-create"),
    path("update/<pk>", PostEditView.as_view(), name="post-edit"),
    # user access
    path("", PostListView.as_view(), name="post-list"),
    path("<slug:blog_slug>/", PostDetailView.as_view(), name="post-view"),
]
