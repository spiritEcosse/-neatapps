'use strict'

### Controllers ###

app_name = "neatapps"
app = angular.module "#{app_name}.controllers", []

app.controller 'MyFormCtrl', ['$http', '$scope', '$window', 'djangoForm', ($http, $scope, $window, djangoForm) ->
  $scope.submit = ->
    if $scope.feedback
      $http.post(".", $scope.feedback).success (data) ->
        if not djangoForm.setErrors($scope.form_comment, data.errors)
          $window.location.href = out_data.success_url
      .error ->
        console.error('An error occured during submission');
    return false
]