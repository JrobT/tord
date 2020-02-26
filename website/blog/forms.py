from django import forms
from markdownx.fields import MarkdownxFormField


class PostForm(forms.Form):
    title = forms.CharField()
    body = MarkdownxFormField()
