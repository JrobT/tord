from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from markdownx.fields import MarkdownxFormField
from blog.models import Comment, Email


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ("name", "email", "comment")


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
