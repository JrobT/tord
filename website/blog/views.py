from django.views.generic.list import ListView
from blog.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
