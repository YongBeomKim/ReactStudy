import React from 'react';
import ReactDOM  from 'react-dom';
import '../scss/home.scss';


// DOM element Adding the Event
// Adding JavaScript Native Code
const header = document.querySelector('.main-header');

window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY;
    if(scrollPos > 10){
        header.classList.add('scrolled');
        console.log('scrolling')
    } else {
        header.classList.remove('scrolled');
    }
});

ReactDOM.render(
    <>
        {/* JSX 랜더링에서 주석처리 */}
        <div>JSX is Working... 머신러닝</div>
    </>,
    document.getElementById('root')
);