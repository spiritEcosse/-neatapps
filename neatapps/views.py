__author__ = 'igor'
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from neatapps.settings import EMAIL_COMPANY
from django.views.generic import FormView
from forms import Feedback
from django.utils.translation import ugettext_lazy as _
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from django.http import HttpResponse
import json
from django.utils.encoding import force_text


class FeedbackForm(NgModelFormMixin, NgFormValidationMixin, Feedback):
    scope_prefix = 'feedback'
    form_name = 'form_comment'
    success_url = '/'


class IndexView(FormView):
    template_name = 'base.html'
    form_class = FeedbackForm
    success_url = '/'

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #
    #     if form.is_valid():
    #         send_mail(_('You received a letter from the site %s') % (request.META['HTTP_HOST'],),
    #                   form.cleaned_data['comment'], form.cleaned_data['email'], [EMAIL_COMPANY],
    #                   fail_silently=False)
    #         return self.form_valid(form)
    #     return self.form_invalid(form=form)
    #
    def post(self, request, **kwargs):
        if request.is_ajax():
            return self.ajax(request)
        return super(IndexView, self).post(request, **kwargs)

    def ajax(self, request):
        form = self.form_class(data=json.loads(request.body))
        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
