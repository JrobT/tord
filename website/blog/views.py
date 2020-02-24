from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from blog.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_url = reverse('post-list')

    def form_invalid(self, form):
        return JsonResponse({'error': True, 'response': form.errors})
