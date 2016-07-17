define(function(require, exports, module){
    var indexApp = require('./app');

    indexApp.controller('blogCtrl', [
        '$scope', 'dataService',
        function($scope, $dataService){
            $scope.blogs = [];
            $scope.num = 1111;
            function activate(pageNum){
                if (pageNum === null){
                    pageNum = 1;
                }
                $dataService.mget(pageNum)
                    .then(function(response){
                        $scope.blogs = $scope.blogs.concat(response.data.blogs);
                    }, function(response){
                        alert('出错啦!');
                    });
            }
            activate(1);
    }]);
});