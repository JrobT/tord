from django.forms import CharField
from markdownx.fields import MarkdownxFormField

class CreatePostForm(forms.Form):
    title = CharField()
    body = MarkdownxFormField()