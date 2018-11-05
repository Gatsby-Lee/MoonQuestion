const path = require('path');
const webpack = require('webpack');
const { VueLoaderPlugin } = require('vue-loader');


// Enviroment flag
var plugins = [
    new VueLoaderPlugin(),
];
var env = process.env.WEBPACK_ENV;

module.exports = {
    mode: env,
    // by default, entry is `./src/index.js`
    entry: {
        home_build_client_compiler: './vuesrc/home_build_client_compiler.js',
        home_build: './vuesrc/Home.js',
    },
    // by default, output is `./dist/main.js`
    output: {
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
    // https://vuejs.org/v2/guide/installation.html#Explanation-of-Different-Builds
    // if wish to use `full build` ( runtime + complier ), add alias.
    // runtime-only build is 30% smaller.
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' for webpack 1
        }
    },
    plugins
};
