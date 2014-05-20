var blogApp = angular.module('levs-blog', []);

blogApp.controller('BlogPreviewCtrl', ['$scope', '$http', function($scope, $http) {

    var posts = [];

    $http.get('/getTopBlogs')
        .success(function(data, status) {
            console.log(data);
            $scope.posts = data;
        })
        .error(function(data, status) {
            console.log(data);
            console.log(status);
        })
}]);
