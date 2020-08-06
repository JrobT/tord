from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from markdownx.fields import MarkdownxFormField
from blog.models import Post, Comment, Email


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "comment", "post", "active", "parent")

    def clean_parent(self):
        parent = self.cleaned_data["parent"]
        post = self.cleaned_data["post"]
        # Check parent comment is attached to the same post
        if parent is not None:
            if parent.post != post:
                raise ValidationError(_('A reply must be attached to the same post ' +
                                      'as its parent comment.'))
        return parent


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data["email"]
        # Check for duplicate
        if Email.objects.filter(email__iexact=email):
            raise ValidationError(_("You're already subscribed."))
        return email
