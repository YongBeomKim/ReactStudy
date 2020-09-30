import React from "react";
import ReactDOM from "react-dom";
import AppIndex from "./components/Index/AppIndex";

// Django : "props" => to => React.js : ...props
// window.renderApp = (props) =>
window.onload = (props) =>
  ReactDOM.render(<AppIndex {...props} />, document.getElementById("root"));
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
