(function() {
  var blogApp;

  blogApp = angular.module('levs-blog', []);

  blogApp.controller('BlogCtrl', [
    '$scope', '$http', '$q', function($scope, $http, $q) {
      var buildPosts, p1, p2, posts, q1, q2;
      posts = [];
      $scope.addComment = function() {
        var commentData;
        $scope.commentMessage = $scope.commentName;
        console.log("Commment");
        console.log("" + $scope.commentName + ": " + $scope.commentMessage);
        console.log($scope);
        commentData = {
          name: $scope.commentName,
          comment: $scope.commentMessage
        };
        console.log(commentData);
        $http.post('/postComment/', commentData).success(function(resp) {
          console.log(resp);
          return false;
        });
        return false;
      };
      q1 = $q.defer();
      q2 = $q.defer();
      p1 = q1.promise;
      p2 = q2.promise;
      $q.all([p1, p2]).then(function(promiseData) {
        return buildPosts(promiseData);
      });
      buildPosts = function(results) {
        var comment, comments, post, postId, _i, _j, _len, _len1;
        console.log("Bulid these combine the comments with the posts and add them to scope");
        console.log(results);
        posts = results[0];
        comments = results[1];
        for (_i = 0, _len = posts.length; _i < _len; _i++) {
          post = posts[_i];
          post.momentRelative = moment(post.fields.created_at).fromNow();
          post.momentDate = moment(post.fields.created_at).format("MMMM Do, YYYY");
          postId = post.pk;
          for (_j = 0, _len1 = comments.length; _j < _len1; _j++) {
            comment = comments[_j];
            if (comment.fields.post === postId) {
              comment.momentRelative = moment(comment.fields.created_at).fromNow();
              if (post.comments != null) {
                post.comments.push(comment);
              } else {
                post.comments = [];
                post.comments.push(comment);
              }
            } else {

            }
          }
        }
        console.log(posts);
        return $scope.posts = posts;
      };
      $http.get('/getComments').success((function(_this) {
        return function(data, status) {
          q2.resolve(data);
        };
      })(this)).error(function(data, status) {
        console.log(data);
        console.log(status);
      });
      return $http.get('/getTopBlogs').success(function(data, status) {
        q1.resolve(data);
      }).error(function(data, status) {
        console.log(data);
        console.log(status);
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
