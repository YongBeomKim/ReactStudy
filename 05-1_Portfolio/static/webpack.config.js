const path = require('path');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');


module.exports = env => {
  return {
    watch: true,
    mode: 'development',
    devtool: 'hidden-source-map',
    entry: {
      index: './src/index.jsx',
      home: './src/home.jsx'
    },
    output: {
      filename: '[name].bundle.js',
      path: path.resolve(__dirname, 'dist')
    },
    plugins: [
      new UglifyJsPlugin(), // bundle 파일 용량 최소화 모듈
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
      // contentBase: './',
      hot: true,
      port: 9000, // dev server port number
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
              presets: ['@babel/preset-env', '@babel/preset-react']
            }
          }
        },

        {
          test: [/\.css$/, /\.s[ac]ss$/i],
          use: ['style-loader', 'css-loader', 'sass-loader'],
        },

        {
          test: /\.(png|gif|ico|svg)$/,
          use: {
            loader: 'url-loader',
            options: {
              name: '[name].[ext]?[hash]',
              publicPath: './dist/',
              limit: 10000 // 10kb 미만인 경우 build 파일에 함께 저장 
            }
          }
        },

        {
          test: /\.(png|jp(e*)g|svg|gif)$/i,
          use: [{
            loader: 'file-loader',
            options: {
              url: false,
              publicPath: '/media/', // 브라우저 URL 주소
              name: '[name].[ext]',
              limit: 8000
              //   emitFile: true,
              //   esModule: false
              // outputPath: '../media/', // dist 를 기준으로 build 저장 경로
              // name: '[name]-[hash].[ext]'
            }
          }],
        }

      ]
    },
    resolve: {
      extensions: ['*', '.js', '.jsx']
    },
  };
}