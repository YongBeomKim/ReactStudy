const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');


module.exports = env => {
  return {
    watch: true,
    mode: 'development',
    devtool: '#eval-source-map', //'source-map',
    entry: {
      index: './src/index.jsx',
    },
    output: {
      filename: '[name].bundle.js',
      path: path.resolve(__dirname, 'dist')
    },
    plugins: [
      new CleanWebpackPlugin(),

      // new BundleAnalyzerPlugin({
      //   analyzerMode: 'static'
      // }),

      // new HtmlWebpackPlugin({
      //   title: 'index',
      //   hash: true,
      //   template: './public/index.html', // target template
      //   filename: 'index.html',  // build file in .dist folder 
      //   chunks: ['index'],  // output js Key word 
      //   excludeChunks: ['index'],  // output js Exclde Key word
      //   minify: {
      //     collapseWhitespace: true
      //   }
      // }),

    ],
    devServer: {
      contentBase: path.join(__dirname, 'dist'),
      publicPath: "/",
      port: 3000, // dev server port number
      hot: true,
      overlay: true,
      disableHostCheck: true,
      // overlay: {
      //   errors: true,
      //   warnings: true
      // }, // Console Error Overlay to Browser
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

        {
          test: /\.(png|jp(e*)g|svg|gif|json)$/i,
          use: [{
            loader: 'file-loader',
            options: {
              name: '[name].[ext]?[hash]',
              outputPath: "media", // relative folder 
              publicPath: "media", // url (path is matched with Django3)
              emitfile: true,
              esmodule: false
            }
          }],
        }
      ]
    },

    resolve: {
      extensions: ['.js', '.jsx']
    },

  };
}