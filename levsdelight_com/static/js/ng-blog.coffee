blogApp = angular.module 'levs-blog', []

blogApp.controller('BlogCtrl', ['$scope', '$http', ($scope, $http) ->
    posts = []

    $http.get('/getTopBlogs')
        .success (data, status) ->
            console.log data
            $scope.posts = data
        .error (data, status) ->
            console.log data
            console.log status
])


blogApp.controller('BlogPreviewCtrl', ['$scope', '$http', ($scope, $http) ->
    posts = []

    $http.get('/getTopBlogs')
        .success (data, status) ->
            console.log data
            $scope.posts = data
        .error (data, status) ->
            console.log data
            console.log status
])


