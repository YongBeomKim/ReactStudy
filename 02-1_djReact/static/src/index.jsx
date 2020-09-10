// const x = 'this is a test';
// alert(x);

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

window.renderApp = (props) =>
  ReactDOM.render(<App {...props} />, document.getElementById("root"));
