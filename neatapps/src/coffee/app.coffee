'use strict'

### Declare app level module which depends on filters, and services ###

app_name = 'neatapps'
app = angular.module app_name, ["#{app_name}.controllers", 'ng.django.forms']

app.config ['$httpProvider', ($httpProvider) ->
  $httpProvider.defaults.xsrfCookieName = 'csrftoken'
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
]