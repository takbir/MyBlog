var webpack = require("webpack");

module.exports = {
    entry: {
        index: [
            "./src/index/app",
            "./src/index/service",
            "./src/index/controller",
            "./src/index/main",
            ],
        vendor: ["angular"]
    },
    output: {
        path: "./build/",
        filename: "[name]/[name].bundle.js"
    },
    plugins: [
        new webpack.optimize.CommonsChunkPlugin("vendor", "vendor/vendor.bundle.js")
    ]
};