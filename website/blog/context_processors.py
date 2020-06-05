from blog.forms import EmailForm


def email_form(request):
    """
    Context processor that provides the mailing list subscribe mini-form
    """
    return {'email_form': EmailForm(request.POST or None)}
