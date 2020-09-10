import React from 'react';
import { Button } from '@storybook/react/demo';
import App from '../src/App';
import { action, actions } from '@storybook/addon-actions';


export const withText = () => <Button>Hello Button</Button>;
export const withTextAction = () => <Button onClick={action('clicked')}>Hello Button</Button>;
export const withEmoji = () => (
  <Button>
    <span role="img" aria-label="so cool">
      😀 😎 👍 💯
    </span>
  </Button>
);

export const withEmojiAction = () => (
  <Button onClick={action('clicked')}>
    <span role="img" aria-label="so cool">
      😀 😎 👍 💯
    </span>
  </Button>
);

// This will lead to { onClick: action('onClick'), ... }
const eventsFromNames = actions('onClick', 'onMouseOver');
// This will lead to { onClick: action('clicked'), ... }
const eventsFromObject = actions({ onClick: 'clicked', onMouseOver: 'hovered' });
export const app = () => <App {...eventsFromNames}/>;
export const appAction = () => <App onClick={action('clicked')}></App>;



export default { title: 'Button' };
