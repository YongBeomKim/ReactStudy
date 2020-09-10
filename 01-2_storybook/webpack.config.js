var path = require('path');
var HtmlWebpackPlugin = require('html-webpack-plugin');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = env => {
  return {
    watch: true,
    mode: 'development',
    devtool: 'source-map',
    entry : {
      index: './src/index.js',
    },
    output: {
      path: path.resolve(__dirname, './dist'),
      filename: '[name].bundle.js',        // '[name].[ext]?[hash]'
      // publicPath: 'http://localhost:3000/' 
    },
    plugins: [
      new BundleAnalyzerPlugin({
        analyzerMode: 'static'
      }),
      new HtmlWebpackPlugin({
        title: 'index',
        hash: true,
        template: './public/index.html', // 반영할 대상
        filename: 'index.html',         // .dist 에 생성할 파일 이름
        chunks: ['index'],  // 포함 js cf) excludeChunks: ['index'] 나머지..
        minify: {
          collapseWhitespace: true
        }
      }),
    ],
    devServer: {
      contentBase: path.join(__dirname, 'dist'),
      compress: true,
      port: 9000,         // webpack dev server 실행할 port
      historyApiFallback: true,
      contentBase: './',
      hot: true
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /(node_modules)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: [
                '@babel/preset-env',
                '@babel/preset-react'
              ]
            }
          }
        },
        {
          test: /\.css$/i,
          use: ['style-loader', 'css-loader'],
        }
      ]
    },
    resolve: {
      extensions: ['*', '.js', '.jsx']
    },
  };
}