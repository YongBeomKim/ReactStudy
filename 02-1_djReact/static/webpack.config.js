const path = require('path');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');
// const HtmlWebpackPlugin = require('html-webpack-plugin');
// const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;


module.exports = env => {
  return {
    watch: true,
    mode: 'development',
    // devtool: 'hidden-source-map',
    entry: {
      index: './src/index.jsx'
    },
    output: {
      filename: '[name].bundle.js',
      path: path.resolve(__dirname, 'dist')
    },
    devtool: 'source-map',
    plugins: [
      new CleanWebpackPlugin(),
      // source-map 오류발생원인 : https://github.com/webpack/webpack/issues/7616
      // new UglifyJsPlugin(), // bundle 파일 용량 최소화 모듈

      // new BundleAnalyzerPlugin({
      //   analyzerMode: 'static'
      // }),

      // new HtmlWebpackPlugin({
      //   title: 'index',
      //   hash: true,
      //   template: './public/index.html', // 반영할 대상
      //   filename: 'index.html',         // .dist 에 생성할 파일 이름
      //   chunks: ['index'],  // 포함 js cf) excludeChunks: ['index'] 나머지..
      //   minify: {
      //     collapseWhitespace: true
      //   }
      // }),
    ],
    devServer: {
      contentBase: path.join(__dirname, 'dist'),
      publicPath: "/",
      hot: true,
      port: 3000, // Port Number
      // compress: true,
      // historyApiFallback: true
    },
    module: {
      rules: [{
          test: /\.(js|jsx)$/,
          exclude: /(node_modules)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env', '@babel/preset-react'],
              plugins: ['@babel/plugin-proposal-class-properties']
            }
          }
        },

        {
          test: [/\.css$/, /\.s[ac]ss$/i],
          use: ['style-loader', 'css-loader', 'sass-loader'],
        },

        {
          test: /\.html$/,
          use: ["html-loader"]
        },
        // {
        //   test: /\.(png|gif|ico|svg)$/,
        //   use: {
        //     loader: 'url-loader',
        //     options: {
        //       name: '[name].[ext]?[hash]',
        //       publicPath: './dist/',
        //       limit: 10000 // 10kb 미만인 경우 build 파일에 함께 저장 
        //     }
        //   }
        // },

        {
          test: /\.(png|jp(e*)g|svg|gif|json)$/i,
          use: [{
            loader: 'file-loader',
            options: {
              name: '[name].[ext]?[hash]',
              outputPath: "media",
              publicPath: "media",
              emitfile: true,
              esmodule: false
              // publicPath: '/static/media',
            },
            // options: {
            //   url: false,
            //   // publicPath: ['/media/', '/static/public/'], // 브라우저 URL 주소
            //   name: '[name].[ext]', // '[name]-[hash].[ext]'
            // }
          }],
        }

      ]
    },
    resolve: {
      extensions: ['.js', '.jsx']
    },
  };
}