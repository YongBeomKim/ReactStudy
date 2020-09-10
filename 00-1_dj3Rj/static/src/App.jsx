import React, { Fragment, useState, useRef, useCallback } from "react";
import ReactDOM from "react-dom";
import Start from "./Start";
import AjaxTest from "./components/Practice/AjaxTest";
import NameForm from "./components/Practice/NameForm";

const App = () => {
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

export default App;
