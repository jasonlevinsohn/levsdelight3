(function() {
  var blogApp;

  blogApp = angular.module('levs-blog', []);

  blogApp.controller('BlogCtrl', [
    '$scope', '$http', function($scope, $http) {
      var posts;
      posts = [];
      return $http.get('/getTopBlogs').success(function(data, status) {
        console.log(data);
        return $scope.posts = data;
      }).error(function(data, status) {
        console.log(data);
        return console.log(status);
      });
    }
  ]);

  blogApp.controller('BlogPreviewCtrl', [
    '$scope', '$http', function($scope, $http) {
      var posts;
      posts = [];
      return $http.get('/getTopBlogs').success(function(data, status) {
        console.log(data);
        return $scope.posts = data;
      }).error(function(data, status) {
        console.log(data);
        return console.log(status);
      });
    }
  ]);

}).call(this);
