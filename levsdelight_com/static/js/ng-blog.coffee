blogApp = angular.module 'levs-blog', []

blogApp.controller('BlogCtrl', ['$scope', '$http', '$q', ($scope, $http, $q) ->
    posts = []
    $scope.commentName = ""
    $scope.commentMessage = ""

    $scope.addComment = ->
        $scope.commentMessage = $scope.commentName
        console.log "Commment"
        console.log "#{$scope.commentName}: #{$scope.commentMessage}"
        console.log $scope

    ##### Oh goodness we need promises here too
    q1 = $q.defer()
    q2 = $q.defer()
    p1 = q1.promise
    p2 = q2.promise

    $q.all([p1, p2])
        .then (promiseData) ->
            buildPosts(promiseData)

    buildPosts = (results) ->
        console.log "Bulid these combine the comments with the posts and add them to scope"
        console.log results

        # Insert the comments to the matched post
        posts = results[0]
        comments = results[1]

        for post in posts
            post.momentRelative = moment(post.fields.created_at).fromNow()
            post.momentDate = moment(post.fields.created_at).format("MMMM Do, YYYY")
            postId = post.pk
            for comment in comments
                if comment.fields.post is postId
                    comment.momentRelative = moment(comment.fields.created_at).fromNow()
                    if post.comments?
                        post.comments.push comment
                    else
                        post.comments = []
                        post.comments.push comment
                else

        console.log posts
        $scope.posts = posts


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


