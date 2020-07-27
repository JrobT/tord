from django.views.generic import TemplateView
from blog.mixins import MailingListMixin


class AboutView(MailingListMixin, TemplateView):
    template_name = 'landing/about.html'
