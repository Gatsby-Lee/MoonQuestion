var path = require('path');
var webpack = require('webpack');

// Enviroment flag
var plugins = [];
var env = process.env.WEBPACK_ENV;

module.exports = {
    mode: env,
    // by default, entry is `./src/index.js`
    entry: './vuesrc/main.js',
    // by default, output is `./dist/main.js`
    output: {
        // filename: 'app.js',
        filename: '[name].js',
        path: path.resolve(__dirname, 'moonquestion/static/zdist'),
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel-loader',
                options: {
                    presets: ["@babel/preset-env"]
                },
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            }
        ]
    },
    plugins
};
