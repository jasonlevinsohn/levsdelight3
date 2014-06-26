blogApp = angular.module 'levs-blog', []

blogApp.controller('BlogCtrl', ['$scope', '$http', '$q', ($scope, $http, $q) ->
    posts = []

    ##### Oh goodness we need promisses here too
    q1 = $q.defer()
    q2 = $q.defer()
    p1 = q1.promise
    p2 = q2.promise

    $q.all([p1, p2])
        .then (promiseData) ->
            buildPosts(promiseData)

    buildPosts = (results)->
        console.log "Bulid these combine the comments with the posts and add them to scope"
        console.log results

    # getComments = ->

    #     console.log "Let's get those comments"
    #     ####### Figure out how to do a LIST COMPREHENSION HERE #######
    #     ####### Oh goodness, we are going to need Promises here too
    #     postIds = []
    #     commentData = {}
    #     for post in posts
    #         postIds.push(post.pk)
    #     console.log postIds

    $http.get('/getComments')
        .success (data, status) =>
            q2.resolve(data)
            return
        .error (data, status) ->
            console.log data
            console.log status
            return

    $http.get('/getTopBlogs')
        .success (data, status) ->
            q1.resolve(data)
            return
        .error (data, status) ->
            console.log data
            console.log status
            return
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


