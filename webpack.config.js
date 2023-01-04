const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode: 'development',
    entry: {
        index : './static/index/',
        base : './static/dashboard/base.js',
        extra : './static/dashboard/extra.js',
    },
    plugins : [
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    'style-loader', 'css-loader'
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