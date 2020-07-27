from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from markdownx.models import MarkdownxField
from profanity.validators import validate_is_profane
from .validators import validate_is_color_string


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    tagline = models.TextField()
    body = MarkdownxField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    edited = models.DateField(db_index=True, auto_now=True)
    active = models.BooleanField(
        "Is Active", default=False, help_text="Has this post been published?"
    )
    pinned = models.BooleanField(
        "Is Pinned", default=False, help_text="Has this post been pinned?"
    )

    class Meta:
        ordering = ["-posted__year", "-posted__month"]

    @property
    def active_comments(self):
        return self.comments.filter(active=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-view", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.pinned:
            try:
                temp = Post.objects.get(pinned=True)
                if self != temp:
                    temp.pinned = False
                    temp.save()
            except Post.DoesNotExist:
                pass
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50, validators=[validate_is_profane])
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=500, validators=[validate_is_profane])
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return "Comment {} by {}".format(self.comment, self.name)


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    background = models.CharField(
        max_length=7, db_index=True, validators=[validate_is_color_string]
    )

    post = models.ManyToManyField(to=Post, related_name="tags")

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Email(models.Model):
    email = models.EmailField(max_length=100)
    subbed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
