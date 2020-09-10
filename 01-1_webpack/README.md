# Fundamental of JavaScript & React Webpack

<br/>

## **JavaScript 의 [Hosting](https://asfirstalways.tistory.com/197) (끌어올리기)**

### 1 (함수)선언(Declaration)과 (객체)할당(Assignment)
- 선언문은 JavaScript 엔진 구동시 최우선으로 해석
- 할당 구문은 RunTime 과정에서 Hosting 된다
- 때문에, 함수 선언 내용이 맨처음 끌어올리므로, 실행문 보다 뒤에 있어서 실행된다

```javascript
function get() {
  console.log(x);   // undefined 값을 출력
  var x = 100;     
}
```

### 2 var, let, const [차이점](https://gist.github.com/LeoHeo/7c2a2a6dbcf80becaaa1e61e90091e5d) 은?

**var**는 **function-scoped** 이고, **let, const** 는 **block-scoped** 입니다.

### 01 Var 의 한계 (조상님)

javascipt에는 그동안 **var** 만 존재했기 때문에 아래와 같은 문제가 있었다.

```javascript
// 이미 만들어진 변수이름으로 재선언했는데 아무런 문제가 발생하지 않는다.
var a = 'test'
var a = 'test2'

// hoisting으로 인해 ReferenceError에러가 안난다.
c = 'test'
var 
```

### 02 new Type 의 등장 

**let, const** 를 사용하면 var를 사용할때보다 상당히 이점이 많다.
- 두개의 공통점은 var와 다르게 **변수 재선언 불가능** 하다.
- let과 const의 차이점은 **변수의 immutable** 여부이다.
- let 은 변수에 **재할당이 가능** 하지만, **const 는 변수 재선언, 재할당 모두 불가능**

```javascript

// let : Uncaught SyntaxError
let a = 'test'
let a = 'test2'  // Uncaught SyntaxError: Identifier 'a' has already been declared
a = 'test3'


// let : ReferenceError
c = 'test' // ReferenceError: c is not defined
let c

// const : Uncaught SyntaxErro, TypeError
const b = 'test'
const b = 'test2' // Uncaught SyntaxError: Identifier 'a' has already been declared
b = 'test3'       // Uncaught TypeError:Assignment to constant variable.
```

### 03 block-scoped 의 tdz(temporal dead zone)

**var** 가 **function-scoped** 단위로 hoisting 이 되었다면 **let, const** 는 **block-scoped** 단위로 hoisting이 일어나서 **tdz(temporal dead zone)** 문제가 발생한다

```javascript
// let : ReferenceError
c = 'test' // ReferenceError: c is not defined
let c
```

const도 마찬가지 문제가 발생하는데, let 보다 좀 더 엄격하다.

```javascript
// let 선언하고 나중에 값 할당이 가능
let dd
dd = 'test'

// const : Missing initializer
// 선언과 동시에 값을 할당 해야한다.
const aa  // Missing initializer in const declaration
```

## **Instade of `npx create-react-app .`**

webpack 을 활용한 React.js 시작

**[https://create-react-app.dev/](https://create-react-app.dev/)**

### 1 HTML 페이지에서 React.js 실행하기

**[웹 사이트에 React.js 추가](https://ko.reactjs.org/docs/add-react-to-a-website.html)**

### 2 WebPack 을 활용한 React.js 실행

**[React webpack 밑바닥에서 부터 설정하기](https://velog.io/@pop8682/%EB%B2%88%EC%97%AD-React-webpack-%EC%84%A4%EC%A0%95-%EC%B2%98%EC%9D%8C%EB%B6%80%ED%84%B0-%ED%95%B4%EB%B3%B4%EA%B8%B0)**

<br/>

## **Webpack Plugins**

### 1 webpack-bundle-analyzer

webpack 에서 bundle 작업을 할때, 압축 내용을 [시각화](https://www.npmjs.com/package/webpack-bundle-analyzer) 로 보여주는 모듈 입니다.

```javascript
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
 
module.exports = {
  plugins: [
    new BundleAnalyzerPlugin()
  ]
}
```

### 2 UglifyjsWebpackPlugin

책에서는 저작권 표시용 모듈이라고 되어 있었지만, [실제로는](https://beomi.github.io/2017/11/29/JS-TreeShaking-with-Webpack/) Bundle 파일의 [압축 효율](https://webpack.js.org/plugins/uglifyjs-webpack-plugin/) 을 높여주는 모듈로써 활용

```javascript
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
    module: {
      // 2. plugins를 새로 만들고, new UglifyJsPlugin() 을 통해
      // UglifyJS를 빌드 과정에 합쳐주세요.
      plugins: [
          new UglifyJsPlugin()
      ]
```

<br/>

## **Issues**

1. **[Cross Header Error, devServer 에서 Host설정 추가](https://velog.io/@adam2/webpack-dev-server-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0%EC%82%BD%EC%A7%88%ED%9B%84%EA%B8%B0)**
2. Target container is not a DOM element. [HtmlWebpackPlugin](https://webpack.js.org/plugins/html-webpack-plugin/)

## 참고 사이트

- **[나만의 Webpack 만들기](https://kdydesign.github.io/2017/11/04/webpack-tutorial/)**
- **[webpack complete guide](https://medium.com/better-programming/webpack-4-the-complete-guide-af1b1e2e3f7a)**
- **[김정환 웹팩 강의자료](http://jeonghwan-kim.github.io/series/2019/12/10/frontend-dev-env-webpack-basic.html#63-htmlwebpackplugin)**
- **[HtmlWebpackPlugin 다중파일 설정](https://choiyb2.tistory.com/96)**
- **[HtmlWebpackPlugin Options](https://github.com/jantimon/html-webpack-plugin#options)**
- **[React.js WebPack 설정](https://pro-self-studier.tistory.com/128)**
