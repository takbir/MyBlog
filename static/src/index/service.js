define(function(require, exports, module){
    var indexApp = require('./app');
    indexApp.service('dataService', ['$http', function($http){
        var apiUrl = '/api/blog/';
        return {
            'mget': mget,
            'create': create,
            'update': update
        }

        function mget(pageNum, itemPerPage){
            if (pageNum === null){
                pageNum = 1;
            }
            if (itemPerPage === null){
                itemPerPage = 10;
            }
            return $http({
                method: 'GET',
                url: apiUrl,
                data: JSON.stringify({
                    'page': pageNum,
                    'item_per_page': itemPerPage
                })
            });
        }

        function create(struct){
            return $http({
                method: 'POST',
                url: apiUrl,
                data: JSON.stringify(struct)
            });
        }

        function update(blogId, struct){
            return $http({
                method: 'PUT',
                url: apiUrl,
                data: JSON.stringify({'id': blogId, 'struct': struct})
            });
        }

    }])
});