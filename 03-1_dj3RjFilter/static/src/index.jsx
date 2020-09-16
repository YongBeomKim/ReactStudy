import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

// Django : "props" => to => React.js : ...props
window.renderApp = (props) =>
  ReactDOM.render(<App {...props} />, document.getElementById("root"));
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
