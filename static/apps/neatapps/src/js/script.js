(function() {
  'use strict';

  /* Declare app level module which depends on filters, and services */
  var app, app_name;

  app_name = 'neatapps';

  app = angular.module(app_name, [app_name + ".controllers"]);

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

}).call(this);
