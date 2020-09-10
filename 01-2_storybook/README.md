# Setting & Configuring the StoryBook

webpack 으로 설치한 React.js 에서 StoryBook 을 설치 및 실행하는 내용을 정리해 보겠습니다. 주요 내용은 **[StoryBook 공식문서](https://storybook.js.org/docs/guides/guide-react/)** 를 참고 하였습니다.

1. Install Storybook
2. Setting
3. Using Component in Storybook
4. Storybook Addon

<br />

# Setting & Start

## Installation

다음을 실행하면 StoryBook 과 관련된 부가 내용을 모두 설치 합니다. 

```r
$ yarn add -D @storybook/react
```

## package.json

StoryBook 실행 script 를 추가 합니다.

```javascript
  "scripts": {
    ..
    "storybook": "start-storybook -p 9001 -c .storybook",
  },
```

## .storybook/main.js

StoryBook 설정을 위한 폴더 `.storybook` 를 생성하고 공식문서에 따라서 설정 파일을 `.storybook/main.js` 추가 합니다. 내용에 따라서 `config.js` 를 사용하는 경우도 있다는 점을 참고 합니다.

```javascript
$ mkdir .storybook
$ touch main.js
  module.exports = {
    stories: ['../src/**/*.stories.[tj]s'],
  };
```

## StoryBook Start

위 설정을 마치고 나서, `package.json` 파일의 스토리북 스크립트를 실행 합니다.

```r
$ yarn storybook
......
webpack built dc067ffaa8b64b6dc454 in 3950ms
╭─────────────────────────────────────────────────────╮
│   Storybook 5.3.19 started                          │
│   4.53 s for manager and 4.27 s for preview         │
│    Local:            http://localhost:9001/         │
│    On your network:  http://192.168.11.106:9001/    │
╰─────────────────────────────────────────────────────╯
```

<br />

# Adding The StoryBook Pages

앞에서 설정 내용을 충실하게 따라했다면, 이번에는 스토리 북에서 실행되는 내용들을 작업해 보겠습니다.

## ./src/index.stories.js

스토리 북에서 보여질 내용을 다음과 같이 작성한 뒤 실행 합니다. 아래 내용을 실행하면 "Button" 내용 밑으로 "App", "with Text", "with Emoji" 내용이 단계적으로 보여지는 것을 알 수 있습니다.

```javascript
import React from 'react';
import { Button } from '@storybook/react/demo';
import App from '../src/App';

export const app = () => <App/>;
export const withText = () => <Button>Hello Button</Button>;
export const withEmoji = () => (
  <Button>
    <span role="img" aria-label="so cool">
      😀 😎 👍 💯
    </span>
  </Button>
);

export default { title: 'Button' };
```

<br />

# [StoryBook AddOns](https://storybook.js.org/addons/)

위 내용 만으로는 별다른 차이점을 알기 어렵습니다. 아래처럼 개별 동작에 따른 설정 및 내용을 추가하면 해당 컴포넌트에 따른 결과값을 텍스트 및 확인할 수 있습니다. 이번에 알아볼 내용은 `Action, Actions` 입니다.

[Github](https://github.com/storybookjs/storybook/tree/master/addons/actions)

## Install Addon

```r
$ yarn add -D @storybook/addon-actions
```

## ./.storybook/main.js

스토리북에서 실행할 Addon 을 배열의 형식으로 설정 파일에 추가 합니다.

```javascript
$ cat addons.js
module.exports = {
    addons: ['@storybook/addon-actions/register'],
    stories: ['../src/**/*.stories.[tj]s'],
};
```

## *.stories.js

main.js 에 추가한 `../src/**/*.stories.[tj]s'` 내용으로 `*.stories.js, *.stories.ts` 에 해당되는 파일들을 자동으로 읽어서 실행 합니다. 

문서 중에는 별도의 `stories/` 폴더를 만들고 여기에 스토리북 파일들을 작업하는 경우들이 있지만
1. 컴포넌트 상대경로를 일일히 작업해야 하고
2. 어떤 컴포넌트를 사용했는지를 직관적으로 알기 어렵다는 점
으로 인해 해당 파일에 추가로 스토리 파일을 작업하는 방식을 선호 합니다. 

<br />

# Conclusion

스토리북 자체가 매력적으로 다가오는 것은 사실입니다. 하지만 위와 같은 별도의 설정 없이 `Chrome 의 Plugin 과 개발자도구` 해서 개별 내용을 알 수 있기때문에 불필요한 작업으로 느껴지는 것 또한 사실 입니다.

결론적으로는 Refectoring 작업을 하면서 Style Guide 정리하는 차원으로 작업하는 방법으로 활용할 계획 입니다. 작업 중간은 Chrome 의 개발자 도구를 활용하는 방법이 더욱 유용할 것으로 보입니다.

## 참고 Sites
- [StoryBook 공식문서](https://storybook.js.org/docs/guides/guide-react/)
- [StoryBook Addons](https://storybook.js.org/addons/)
- [Velopert 스토리북 예제](https://velog.io/@velopert/start-storybook/)