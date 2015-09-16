(function() {
  'use strict';

  /* Declare app level module which depends on filters, and services */
  var app, app_name;

  app_name = 'neatapps';

  app = angular.module(app_name, [app_name + ".controllers", 'ng.django.forms']);

  app.config([
    '$httpProvider', function($httpProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      return $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
  ]);

}).call(this);

(function() {
  'use strict';

  /* Controllers */
  var app, app_name;

  app_name = "neatapps";

  app = angular.module(app_name + ".controllers", []);

  app.controller('MyFormCtrl', [
    '$http', '$scope', '$window', 'djangoForm', function($http, $scope, $window, djangoForm) {
      return $scope.submit = function() {
        if ($scope.feedback) {
          $http.post(".", $scope.feedback).success(function(data) {
            if (!djangoForm.setErrors($scope.form_comment, data.errors)) {
              return $window.location.href = out_data.success_url;
            }
          }).error(function() {
            return console.error('An error occured during submission');
          });
        }
        return false;
      };
    }
  ]);

}).call(this);
