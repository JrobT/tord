from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from markdownx.models import MarkdownxField
from profanity.validators import validate_is_profane


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    tagline = models.TextField()
    body = MarkdownxField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    edited = models.DateField(db_index=True, auto_now=True)
    active = models.BooleanField("Is Active", default=False, help_text="Has this post been published?")

    # Blog posts are of a single category
    category = models.ForeignKey("blog.Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-view", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50, validators=[validate_is_profane])
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=500, validators=[validate_is_profane])
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Email(models.Model):
    email = models.EmailField(max_length=100)
    subbed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
