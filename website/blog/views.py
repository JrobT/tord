import re
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from blog.models import Post, Comment, Email
from blog.forms import CommentForm
from blog.mixins import MailingListMixin


def post_view(request, slug):
    template_name = "blog/post_view.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(Q(active=True) & Q(parent__isnull=True))
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }

    return render(request, template_name, context)


class PostListView(MailingListMixin, TemplateView):
    template_name = "blog/post_list.html"

    def get(self, request, *args, **kwargs):
        # Show only active posts if not a staff/superuser.
        qs = Post.objects.filter(active=True)
        if request.user.is_staff or request.user.is_superuser:
            qs = Post.objects.all()

        # Get pinned Post and remove it from QuerySet.
        try:
            pinned = qs.get(pinned=True)
            qs = qs.exclude(pinned=True)
        except Exception:
            pinned = None

        # Set up dictionary for 'Archive' and 'Tags' menu.
        archive = dict()
        tags = dict()
        for post in qs:
            month_year_combo = "%s %s" % (post.posted.strftime("%B"), post.posted.year)
            if month_year_combo in archive:
                archive[month_year_combo] = archive[month_year_combo] + 1
            else:
                archive[month_year_combo] = 1

            for tag in post.tags.all():
                if tag.title in tags:
                    tags[tag.title] = tags[tag.title] + 1
                else:
                    tags[tag.title] = 1
        sortedTags = {
            key: value
            for key, value in sorted(
                tags.items(), key=lambda item: item[1], reverse=True
            )
        }

        text_filter = request.GET.get("text")
        if text_filter is not None or "":
            qs = qs.filter(
                Q(title__icontains=text_filter)
                | Q(tagline__icontains=text_filter)
                | Q(body__icontains=text_filter)
            )

        archive_filter = request.GET.get("archive")
        if archive_filter is not None or "":
            dt = datetime.strptime(archive_filter, "%B %Y")
            qs = qs.filter(Q(posted__month=dt.month) & Q(posted__year=dt.year))

        tag_filter = request.GET.get("tag")
        if tag_filter is not None or "":
            qs = qs.filter(tags__title__icontains=tag_filter)

        paginator = Paginator(qs, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "pinned": pinned,
            "page_obj": page_obj,
            "num_pages": range(1, page_obj.paginator.num_pages+1),
            "comments": Comment.objects.filter(active=True),
            "archive": archive,
            "tags": sortedTags,
        }

        return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "tagline", "body"]
    raise_exception = True


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "tagline", "body"]
    slug_url_kwarg = "blog_slug"
    slug_field = "slug"
    raise_exception = True
