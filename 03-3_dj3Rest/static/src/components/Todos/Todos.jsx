import React, { Fragment, Component } from "react";
import axios from "axios";

class Todos extends Component {
  state = {
    todos: [],
  };
  componentDidMount() {
    this.getTodos();
  }
  getTodos() {
    axios
      .get("http://localhost:8000/todos/api/")
      .then((response) => {
        this.setState({ todos: response.data });
      })
      .catch((error) => {
        console.log(error);
      });
  }
  render() {
    return (
      <Fragment>
        {this.state.todos.map((item) => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.body}</span>
          </div>
        ))}
      </Fragment>
    );
  }
}

export default Todos;
