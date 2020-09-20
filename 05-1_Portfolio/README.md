# Webpack Dj & React .. and SASS SCSS

<br/>

# Adding SCSS

[![SCSS Menu](https://raw.githubusercontent.com/YongBeomKim/react-study-seoul/master/07_dj_scss/static/index_youtube.jpeg)](https://youtu.be/mEtmJ2xk16g)

## Webpack Setting

### Install NPM Modules 

webpack 사이트의 **[sass-loader 설치 Guide](https://webpack.js.org/loaders/sass-loader/)** 를 참고 하였습니다.

```r
$ yarn add -D sass-loader node-sass
$ npm install sass-loader node-sass --save-dev
```

`style-loader` 는 style 내용을 JS 언어로 변환하는 기본 모듈이고, `css-loader`와 `sass-loader` 는 각각 `css`, `scss` 언어를 JS 로 변환합니다.

따라서 [공식문서](https://webpack.js.org/loaders/sass-loader/#implementation) 에 따르면 `sass-loader` 를 먼저 설치하고, 다음에 `node-sass` 를 설치 하도록 안내가 되어 있습니다. <strike>참고로 `sass` 모듈은 **Dart** 언어에서 sass 를 사용하도록 돕는 모듈로써 이번 작업에서는 `node-sass` 로 대체 합니다.</strike>

### package.json

위에서 설명한 모듈의 의존성 문제를 고려하여 `package.json` 의 내용도 다음과 같이 순서를 일치 시킵니다.

```json
{
  "devDependencies": {
    "sass-loader": "^7.2.0",
    "node-sass": "^4.0.0"
  }
}
```

### webpack.config.js

webpack 의 설정에서는 인식하는 파일의 확장자와, `sass-loader` 를 추가 합니다. <strike>`options` 설정으로 data 등을 추가하는 작업들을 시도 했지만 실패하여 아래에는 추가하지 않았습니다.</strike>

```javascript
module.exports = {
  module: {
    rules: [
        {
          test: [/\.css$/, /\.s[ac]ss$/i],
          use: ['style-loader','css-loader','sass-loader'],
        },
      }
    ],
  },
};
```

## TDD SCSS via Webpack

앞에서 설정한 내용이 제대로 작동하는지를 확인 합니다.

### scss/style.scss

스타일 내용을 추가 합니다.

```scss
$body-color: red;

h1 {
  color: $body-color;
}
```

### src/index.js

DOM 을 Rendering 하는 Javascript 파일에 스크립트 파일을 추가하면 해당 DOM 에 자동으로 스타일을 추가 합니다.

```javascript
import '../scss/style.scss';
```

<br/>

## Styled-Components

`SCSS`, `CSS` 파일을 활용하여 스타일을 추가하는 방법 이외에도 **[CSS in JS](https://github.com/MicheleBertoli/css-in-js)** 방식 중 하나를 적용합니다.

### Install

```r
$ yarn add -D styled-components
```

vscode-styled-components 이름을 갖는 Extendtion 이 2개인 것을 알 수 있습니다. 각각의 차이는 아래와 같습니다.

Type Script 를 사용하지 않는 경우에는 8,886 명이 설치한 [vscode-styled-components](https://marketplace.visualstudio.com/items?itemName=mf.vscode-styled-components) 모듈을 사용하고, TypeScript 를 사용 중이면 40만명이 설치한 [vscode-styled-components](https://github.com/styled-components/vscode-styled-components) 를 사용 합니다. <strike>React.js 사용자 상당수가 TypeScript 를 사용중인 듯...</strike>


<br/>

## 참고문서 
- **[Loading Images, webpack book](https://survivejs.com/webpack/loading/images/)**
- **[웹팩의 file-loader와 url-loade](http://jeonghwan-kim.github.io/js/2017/05/22/webpack-file-loader.html)**
- **[웹팩 입문: 2. sass, img, svg 사용하기]()**
- **[Webpack SCSS Loader](https://webpack.js.org/loaders/css-loader/)**
- **[CSS in JS](https://github.com/MicheleBertoli/css-in-js)**
- **[Styled Components](https://styled-components.com/docs/tooling)**