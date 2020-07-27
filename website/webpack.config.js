const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const path = require('path')
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    mode: 'development',
    entry: './static/js/index.js',
    devtool: 'inline-source-map',
    devServer: {
        contentBase: './static/dist',
        compress: true
    },
    output: {
        path: path.resolve(__dirname, 'static/dist'),
        filename: "[name].js"
    },
    plugins: [
        new MiniCssExtractPlugin({
            path: path.resolve(__dirname, 'static/dist'),
            filename: "[name].css",
        }),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery'
        }),
        new BundleTracker({
            filename: './static/dist/webpack-stats.json'
        })
    ],
    module: {
        rules: [
            {
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
