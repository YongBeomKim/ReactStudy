# Using Webpack with Django & React.js

Django 의 Template 에서 `jquery` 를 활용하던 내용들은 [vue.js delimiters](https://stackoverflow.com/questions/33628558/vue-js-change-tags) 설정을 활용하면 SPA 로 손쉽게 구현 가능합니다.

```javascript
Vue.config.delimiters = ['<%', '%>']
```

**React.js** 는 **curly brase** 충돌 등을 **[verbatim](https://www.djangotemplatetagsandfilters.com/tags/verbatim/)** 의 **Template filter** 를 활용하는 등 어렵지만, **React Native** 로 확장이 용이 합니다.

## Django Setting

### settings.py
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

### views.py
```python
from django.shortcuts import render

def  index(request):
    return render(request, "index.html")
```

### Template

```html
{% load static %}
<script src="{% static 'js/index.js' %}"></script>
```

<br/>

# Webpack Setting

[![React Django](https://i.ytimg.com/vi/WZiOV0_BPO0/hqdefault.jpg)](https://www.youtube.com/embed/Mx3ChaYA0Gw)

## Installation

### Install NPM Modules 

`./static/` 폴더에서 webpack 과 react.js 관련 모듈을 설치 합니다. 아래 작업을 마치고 나면  `./node_modules` 에 모듈이 설치되고 설정 내용은 `package.json` 로 저장 됩니다.

```r
$ yarn init
$ yarn add react react-dom

$ yarn add -D babel-loader 
$ yarn add -D @babel/core @babel/preset-react @babel/preset-env
$ yarn add -D webpack webpack-cli webpack-dev-server 
$ yarn add -D css-loader node-sass html-webpack-plugin 
```

### package.json

설정 파일에서 webpack 의 빌드 및 webpack server 실행 스크립트 내용을 추가 합니다.

```json
"scripts": {
  "start": "webpack-dev-server --mode development --open --hot",
  "build": "webpack --mode production"
},
```

### webpack.config.js

**React** 와 **Hot Reloaded Module** 설정 내용을 추가 합니다. 아래 내용을 추가한 뒤 `$ yarn start` 를 실행하면, **webpack dev server** 로 **Hot Reloaded Module** 이 실행 됩니다. bundle 된 javascript 파일은 `http://localhost:9000/index.bundle.js` 로 연결 됩니다.

```javascript
const path = require('path');

module.exports = env => {
  return {
    watch: true,
    mode: 'development',
    devtool: 'source-map',
    entry: {
      index: './src/index.js'
    },
    output: {
      filename: '[name].bundle.js',
      path: path.resolve(__dirname, 'dist')
    },
    devServer: {
      port: 9000,
      hot: true,
      compress: true,
      historyApiFallback: true
      contentBase: path.join(__dirname, 'dist'),
      publicPath: "/",
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
```

## Connect Webpack and Django

위 설정 뒤, `index.js` 에서 **React.js** 내용이 잘 작동 되는지를 확인 합니다.

- `$ yarn bundle` : webpack bundle (`dist/index.bundle.js`)
- `$ yarn start` : webpack dev server (`http://localhost:9000/index.bundle.js`)

```html
{% comment 'webpack bundle' %}
<!-- Production Mode JavaScript -->
<script src="{% static 'dist/index.bundle.js' %}"></script>
{% endcomment %}

<!-- webpack dev server Hot Reloaded Module -->
<script src="http://localhost:9000/index.bundle.js"></script>
{% endblock js %}
```

<br/>

## 참고문서 
- **[Using Webpack with Django: no plugins required!](https://pascalw.me/blog/2020/04/19/webpack-django.html)**
- **[Using webpack with Django: it's not easy as you think](https://www.valentinog.com/blog/webpack-django/)**
- **[React Form](https://ko.reactjs.org/docs/forms.html)**