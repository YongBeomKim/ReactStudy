import React, { Fragment, useState, useRef, useCallback } from "react";
import ReactDOM from "react-dom";

// Based on 'App.jsx' folder
import dinoImg from "../media/photo.jpg";

const Start = () => {
  // json file load by Hard Coding
  fetch("../../static/public/list.json")
    .then((res) => {
      return res.json(); //Promise 반환
    })
    .then((json) => {
      console.log(json); // 서버에서 주는 json데이터가 출력 됨
    });

  // Props data convert to json String
  const django_data = JSON.stringify(props);

  return (
    <Fragment>
      <br />
      Raw : {django_data}
      <br />
      Raw.name : {props.name}
      <br />
      Raw more : {props.more}
      <br />
      <h2>Photo</h2>
      <img width="500" height="500" src={dinoImg} />
    </Fragment>
  );
};

export default Start;
