__author__ = 'igor'
from django.core.mail import send_mail
from neatapps.settings import EMAIL_COMPANY
from django.views.generic import FormView
from forms import Feedback
from django.utils.translation import ugettext_lazy as _
from djangular.forms import NgModelFormMixin
from django.http import HttpResponse
import json
from django.views.generic.base import ContextMixin
from django.utils import translation


class FeedbackForm(NgModelFormMixin, Feedback):
    scope_prefix = 'feedback'
    form_name = 'form_comment'


class IndexView(FormView, ContextMixin):
    template_name = 'base.html'
    form_class = FeedbackForm

    def post(self, request, **kwargs):
        if request.is_ajax():
            return self.ajax(request)
        return super(IndexView, self).post(request, **kwargs)

    def ajax(self, request):
        form = self.form_class(data=json.loads(request.body))
        response_data = {'errors': form.errors}

        if not form.errors:
            send_mail(_('You received a letter from the site %s') % request.META['HTTP_HOST'],
                      'Email: %s .\nComment: %s' % (form.cleaned_data['email'], form.cleaned_data['comment']),
                      form.cleaned_data['email'], [EMAIL_COMPANY],
                      fail_silently=False)
            response_data['msg'] = unicode(_('Your message sent!'))
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        cur_language = translation.get_language()
        context['class'] = ''

        if cur_language == 'ru':
            context['class'] = 'class=lang_ru'
        return context
