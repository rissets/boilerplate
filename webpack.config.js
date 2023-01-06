const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

// check if we are in production mode, make sure to set this in your environment
const isDevelopment = (process.env.DEBUG || "false").toLowerCase() === "true";


module.exports = {
    target: 'web',
    mode: 'development',
    entry: {
        // bootstrap_css: './static/css/bootstrap.min.css',
        index : './static/index/',
        base : './static/dashboard/base.js',
        extra : './static/dashboard/extra.js',
        authentication : './static/authentication/index.js',
    },
    plugins : [
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    'style-loader', 'css-loader',
                ]
            },
            {
                test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
                type: 'asset',
                generator: {
                    filename: 'fonts/en/[hash][ext][query]',
                },
            }
        ]
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, './static/bundles'),
    }
}