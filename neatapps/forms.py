__author__ = 'igor'

from djangular.styling.bootstrap3.forms import Bootstrap3Form
from django import forms
from django.utils.translation import ugettext_lazy as _


class Feedback(Bootstrap3Form):
    name = forms.CharField(max_length=30, label=_('Name'), required=False)
    email = forms.EmailField(required=True, label=_('Email'), error_messages={'required': _('Please enter your email.')})
    comment = forms.CharField(label=_('Message'), required=True, widget=forms.Textarea(), min_length=1, max_length=3000,
                              error_messages={'required': _('Please enter your message.')})