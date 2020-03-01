from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from blog.models import Post
from blog.forms import PostForm


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "body", "category"]
