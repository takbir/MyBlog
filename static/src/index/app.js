define(function(require, exports, module){
    var ng = require('angular');
    var app = ng.module('indexApp', []);
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('${');
        $interpolateProvider.endSymbol('}');
    });
    module.exports = app;
});