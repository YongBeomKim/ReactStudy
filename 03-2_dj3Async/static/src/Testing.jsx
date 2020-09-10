import React, { Fragment, useState, useRef, useCallback } from "react";
import ReactDOM from "react-dom";

// Based on 'App.jsx' folder
import dinoImg from "../media/photo.jpg";

const Start = () => {
  // Django Props to Json String
  const django_data = JSON.stringify(props);

  // Loading Json file by Hard Coding
  fetch("../../static/public/list.json")
    .then((res) => {
      return res.json(); // Promise
    })
    .then((json) => {
      console.log(json);
    });

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
