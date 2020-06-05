const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack')

module.exports = {
    mode: 'development',
    entry: './static/js/index.js',
    plugins: [new MiniCssExtractPlugin(), new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery'
    })],
    module: {
        rules: [{
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader, 'css-loader'],
            },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                        plugins: [
                            '@babel/plugin-proposal-class-properties'
                        ]
                    }
                }
            },
            {
                test: /\.svg$/,
                use: [{
                    loader: 'svg-url-loader',
                    options: {
                        limit: 10000,
                    },
                }, ],
            }
        ]
    }
}
