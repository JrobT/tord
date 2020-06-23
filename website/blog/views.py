import re
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from blog.models import Post, Comment, Email
from blog.forms import CommentForm, EmailForm


class AboutView(TemplateView):
    template_name = 'about.html'


def post_detail(request, slug):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
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
        "comment_form": comment_form
    }

    return render(request, template_name, context)


def post_list(request):
    template_name = "blog/post_list.html"

    if request.method == 'POST':
        email_form = EmailForm(data=request.POST)
        if email_form.is_valid():
            # Record email address in DB.
            email_form.save()
            messages.success(request, _("Thank you!"))
    else:
        email_form = EmailForm()

    # Show only active posts if not a staff/superuser.
    qs = Post.objects.filter(active=True)
    if request.user.is_staff or request.user.is_superuser:
        qs = Post.objects.all()

    # Set up dictionary for 'Archive' and 'Tags' menu.
    archive = dict()
    tags = dict()
    for post in reversed(qs):
        month_year_combo = "%s %s" % (post.posted.strftime('%B'), post.posted.year)
        if month_year_combo in archive:
            archive[month_year_combo] = archive[month_year_combo] + 1
        else:
            archive[month_year_combo] = 1

        for tag in post.tags.all():
            if tag.title in tags:
                tags[tag.title] = tags[tag.title] + 1
            else:
                tags[tag.title] = 1
    # Sort tags by their count.
    sortedTags = {key: value for key, value in sorted(
        tags.items(), key=lambda item: item[1], reverse=True)}

    # Filter posts by tags.
    # tag_filter = request.GET.get("tags")
    # if tag_filter is not None or "":
    #     qs = qs.filter(tag__icontains=tag_filter)

    # Filter posts by posted date.
    archive_filter = request.GET.get("archive")
    if archive_filter is not None or "":
        dt = datetime.strptime(archive_filter, "%B %Y")
        qs = qs.filter(Q(posted__month=dt.month) & Q(posted__year=dt.year))

    # Filter Posts by title, tagline, body.
    text_filter = request.GET.get("text")
    if text_filter is not None or "":
        qs = qs.filter(Q(title__icontains=text_filter) |
                       Q(tagline__icontains=text_filter) |
                       Q(body__icontains=text_filter))

    paginator = Paginator(qs.order_by('-posted'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "form": email_form,
        "page_obj": page_obj,
        "comments": Comment.objects.filter(active=True),
        "archive": archive,
        "tags": sortedTags
    }

    return render(request, template_name, context)


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
