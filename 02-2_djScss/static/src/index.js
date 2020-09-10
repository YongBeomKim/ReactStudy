// const x = 'this is a test';
// alert(x);

import React from 'react';
import ReactDOM  from 'react-dom';
import SassComponent from './SassComponent';
import CSSModule from "./CSSModule";

import '../scss/style.scss';

import styles from '../scss/CSSModule.module.css';

ReactDOM.render(
    <>
        {/* JSX 랜더링에서 주석처리 */}
        <div>JSX is Working... 머신러닝</div>
        <br />
        <CSSModule></CSSModule>
        <br/>
        <SassComponent></SassComponent>
    </>,
    document.getElementById('root')
);