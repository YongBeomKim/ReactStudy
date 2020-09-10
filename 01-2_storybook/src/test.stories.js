import React from 'react';
import { action } from "@storybook/addon-actions";

export const test = () => (
    <textarea onClick={action("clicked")}>
        React.js test in TextArea in StoryBook
    </textarea>
);

export default {
    title: "TextArea Test"
};