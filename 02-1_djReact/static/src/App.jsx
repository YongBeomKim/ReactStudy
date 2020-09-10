import React, { Fragment } from "react";
import ReactDOM from "react-dom";

// Based on the folder area of 'App.jsx'
import dinoImg from "../media/photo.jpg";
// import dinoImg from "../../static/media/photo.jpg";

const App = (props) => (
  <Fragment>
    <h1>Hello World from React and Django</h1>
    <div>
      image loading...
      <span>Passed props:</span>
      {JSON.stringify(props)}
      {"http://localhost:3000/" + dinoImg}
    </div>
    <p>Testing Photo</p>
    <img src={"http://localhost:3000/" + dinoImg} />
  </Fragment>
);

export default App;
