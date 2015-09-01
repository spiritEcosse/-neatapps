__author__ = 'igor'
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from forms import Feedback
from django.core.mail import send_mail
from neatapps.settings import EMAIL_COMPANY
from django.utils.translation import ugettext_lazy as _


class IndexView(FormView):
    template_name = 'base.html'
    form_class = Feedback
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            send_mail(_('You received a letter from the site %s') % (request.META['HTTP_HOST'],),
                      form.cleaned_data['comment'], form.cleaned_data['email'], [EMAIL_COMPANY],
                      fail_silently=False)
            self.success_url = '%s%s' % (request.META['HTTP_HOST'], self.success_url)
            return self.form_valid(form)
        return self.form_invalid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'