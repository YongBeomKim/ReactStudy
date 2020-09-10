import React, { Fragment, useState, useRef, useCallback } from "react";
import ReactDOM from "react-dom";
import AjaxTest from "../Practice/AjaxTest";
import NameForm from "../Practice/NameForm";

const AppIndex = () => {
  return (
    <Fragment>
      <h2>Fetch API Test</h2>
      <AjaxTest />
      <br />
      <h2>React Form</h2>
      <NameForm />
    </Fragment>
  );
};

export default AppIndex;
