# HTML & CSS (Cascading Style Sheets) Web Style Guide

**30일 레슨으로 배우는 HTML5 & CSS3 디자인 강좌** 도서 내용을 정리 하였습니다.

<br/>

# Chapter 1 - HTML Tags

> header
> nav
> footer

> div : 문서의 구분
> section : content 본문의 영역

**[Material Color Tool](https://material.io/resources/color/#!/?view.left=0&view.right=0)** 에서 조화로운 Color 배열을 찾아서 적용 합니다.

<br/>

# Chapter 2 - flex box

속성값은 Container 와 Item 에 적용하는 내용이 구분되어 있습니다.
1. Container 에서는 `display`, `flex-flow`, `justity-content` 를
1. Item 에는 `order`, `flex`, `align-self` 를 사용 합니다.

## Container 
Container 에서는 `display`, `flex-flow`, `justity-content` 등을 사용 합니다.

```css
.container {
    /* 1 flex 활성화*/
    display: flex;        
    /* 2 flex 정렬 : row, column, row-reverse, column-reverse */
    flex-direction: row; 
    /* 3 flex 화면 접힐때(wrap) Box 비율유지 여부 */
    /* nowrap(접힐때 왜곡), wrap(고유비율 유지), wrap-reverse */
    flex-wrap: nowrap;
    /* 2, 3번 설정을 한꺼번에 정의 */
    flex-flow: flex-direction flex-wrap;
}
```

다음은 Container **내부의 Item** 을 어떻게 배치할지 정의 합니다.

`align-item` 은 **flex-box** 를 기준으로 `justify-content` 는 **main axis** 를 기준으로 정렬을 합니다. 이와 관련된 자세한 설명은 [stackoverflow](https://stackoverflow.com/questions/27539262/whats-the-difference-between-align-content-and-align-items) 를 참고 합니다.

```css
.container {
    /* main axis : 
    flex-start, flex-end, center, 
    space-between, space-around, space-evenly */
    justify-content: flex-start; 

    /* opposite side axis : 
    flex-start, flex-end, center, 
    space-between, space-around */
    align-content: center; 

    /* opposite side axis : 
    flex-start, flex-end, center, stretch, */
    align-items: stretch;

}
```

## Item
Item 에는 `order`, `flex`, `align-self` 등을 사용 합니다.

```css
item {
    /* flex item area ratio */
    flex: 2;

    /* item blank space ratio when strenth */
    flex-grow: 1;   /* grow : 화면이 늘었을 때 여백비율 */
    
    /* item blank space ratio when pressed */
    flex-shrink: 1; /* shrink : 화면이 줄었을 때 여백비율 */
    
    /* item width ratio */
    flex-basis: 100%;  /* basis: Item 객체의 공간비율 auto */

    /* align the item above the container box*/
    align-self: center; 
}
```

<br/>

# Chapter 6 - 문서 장식하기 

CSS 에서 객체를 선택할때 유용한 **가상 클래스, 가상 요소** 에 대해 살펴보겠습니다. 이와 관련된 실습 내용은 **[코남 - 형광펜 효과 만들기](https://youtu.be/nvdgIsqEegQ)** 를 참고하면 확실하게 알 수 있습니다.

## Link 가상 클래스 (Pseudo-Class in CSS : `:` ) 

property 는 **자산/ 재산** 의 의미를 갖는 단어로, React.js 에서는 `props` 를 생각하면 됩니다.

|  선택자  |       내 용        |
| :------: | :----------------: |
|  :link   |    미 방문 Link    |
| :visited |     방문 link      |
|  :hover  | Pointer 올렸을 때  |
| :active  | Pointer 눌렀을 때  |
|  :focus  | Focusing 되었을 때 |

## Style 가상 요소 (Pseudo-Elements : `::` ) 

|     Pseudo     |               내 용               |
| :------------: | :-------------------------------: |
|    ::before    |         Content 시작 부분         |
|    ::after     |          Content 끝 부분          |
|  ::selection   |   사용자가 선택(드래그) 된 영역   |
| ::placeholder  |    Input 필드의 Hit Text Style    |
|  ::first-line  |    텍스트 첫 줄에 스타일 적용     |
| ::first-letter | 텍스트 첫 번째 글자에 스타일 적용 |

## 참고 Site 목록

- **[BEM CSS 활용법](https://nykim.work/15)**
- **[Material Color Tool](https://material.io/resources/color/#!/?view.left=0&view.right=0)**
-**[CSS Flex(Flexible Box) 완벽 가이드](https://heropy.blog/2018/11/24/css-flexible-box/)**
- **[Sass 강좌 – 한 눈에 보기](https://velopert.com/1712)**
- **[sass의 기본 문법 6가지](https://grace-go.tistory.com/57)**
- **[BEM 으로 사고하고 분석하기](https://mytory.net/html-css-js/2015/05/07/mindbemding-getting-your-head-round-bem-syntax.html)**


![책표지](https://image.kyobobook.co.kr/images/book/xlarge/434/x9788931455434.jpg)
