import React from 'react'
import styles from "../scss/CSSModule.module.css";
import classNames from "classnames/bind";

const cx = classNames.bind(styles);

const CSSModule = () => {
    return (
        <>

        {/* template literal 문법을 활용한 style 추가 */}
        <div className={`${styles.wrapper} ${styles.inverted}`}>
            안녕하세요
            <span className="something"> 저는 Django! </span>
        </div>

        <br />

        {/* classNames 모듈을 사용한 스타일 추가 */}
        <div className={cx('wrapper', 'inverted')}>
            이번에는 classNames 를
            <span className="something"> 활용했습니다. </span>
        </div>
        </>
    );
};

export default CSSModule;