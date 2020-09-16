const path = require('path');
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');


module.exports = env => {

  return {
    watch: true,
    mode: 'development',
    devtool: 'cheap-module-source-map', //'#eval-source-map', //'source-map',
    entry: {
      index: './src/index.jsx',
    },

    output: {
      filename: '[name].bundle.js',
      path: path.resolve(__dirname, 'dist')
    },

    plugins: [
      new CleanWebpackPlugin(),
    ],

    devServer: {
      contentBase: path.join(__dirname, 'dist'),
      publicPath: "/", // dev server root url
      port: 3000, // dev server port number
      hot: true,
      overlay: true, // Debug Message to Browser
      disableHostCheck: true,
    },

    module: {
      rules: [{
          test: /\.(js|jsx)$/,
          exclude: /(node_modules)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env', '@babel/preset-react'],
              plugins: [
                '@babel/plugin-proposal-class-properties',
                '@babel/plugin-transform-runtime',
              ]
            }
          }
        },

        {
          test: [/\.css$/, /\.s[ac]ss$/i],
          use: ['style-loader', 'css-loader', 'sass-loader'],
        },


        { // for `HtmlWebPackPlugin` to Encoding Html
          test: /\.html$/,
          use: [{
            loader: "html-loader",
            options: {
              minimize: true
            }
          }],
        },

        { // https://stackoverflow.com/questions/48563461/webpack-file-loader-publicpath
          test: /\.(png|jp(e*)g|svg|gif|json)$/i,
          use: [{
            loader: 'file-loader',
            options: {
              name: '[name].[ext]?[hash]',
              publicPath: "../media/", // url path Starting Root (match with Django3)
              // outputPath: "./media/", // relative folder 
              // emitfile: true,
              // esmodule: false
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