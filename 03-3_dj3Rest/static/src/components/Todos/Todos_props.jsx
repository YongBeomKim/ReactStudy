import React, { Fragment, Component } from "react";
import ReactDOM from "react-dom";
import axios from "axios";

class Todos extends Component {
  constructor(props) {
    super(props);
    this.state = { list };
  }
  render() {
    return (
      <Fragment>
        <h1>Testing Todo</h1>
        {this.state.list.map((item) => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
          </div>
        ))}
      </Fragment>
    );
  }
}

export default Todos;
