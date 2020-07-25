from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from blog.forms import EmailForm


class MailingListMixin():
    """Process POST as a request to be added to the mailing list."""

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            email_form = EmailForm(data=request.POST)
            if email_form.is_valid():
                email_form.save()
                messages.success(request, _("Thank you!"))
        else:
            email_form = EmailForm()
        context = self.get_context_data()
        context["form"] = email_form
        return self.render_to_response(context)
