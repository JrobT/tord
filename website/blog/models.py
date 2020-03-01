from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = MarkdownxField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    edited = models.DateField(db_index=True, auto_now=True)

    # Blog posts are of a single category
    category = models.ForeignKey("blog.Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url():
        return reverse("post-list")


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title
