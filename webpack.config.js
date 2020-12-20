const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'static'),
    },
    module: {
        rules: [
            { test: /\.css$/i ,use: ['style-loader', 'css-loader'] },
            { test: /\.vue$/,loader: 'vue-loader'}, 
            {test: /\.(png|svg|jpg|jpeg|gif)$/i,type: 'asset/resource'},
            { test: /\.(woff|woff2|eot|ttf|otf)$/i, type: 'asset/resource'},
            {test: /\.js$/,loader: 'babel-loader'},
        ],
    },
     plugins: [
    new VueLoaderPlugin()
  ]
};