import React, { Fragment, useState, useRef, useCallback } from "react";
import ReactDOM from "react-dom";

// Based on 'App.jsx' folder
// import dinoImg from "../media/photo.jpg";
import dinoImg from "../media/photo.jpg";
import TodoTemplate from "./components/todo/TodoTemplate";
import TodoInsert from "./components/todo/TodoInsert";
import TodoList from "./components/todo/TodoList";

const Todo = () => {
  // json file load by Hard Coding
  fetch("../../static/public/list.json")
    .then((res) => {
      return res.json(); //Promise 반환
    })
    .then((json) => {
      console.log(json); // 서버에서 주는 json데이터가 출력 됨
    });

  const [todos, setTodos] = useState([
    {
      id: 1,
      text: "react.js basic",
      checked: true,
    },
    {
      id: 2,
      text: "styling the React Component",
      checked: false,
    },
    {
      id: 3,
      text: "build todo app",
      checked: false,
    },
  ]);

  const nextId = useRef(todos.length + 1);
  const on_insert = useCallback(
    (text) => {
      const todo = {
        id: nextId.current,
        text,
        checked: false,
      };
      setTodos(todos.concat(todo));
      nextId.current += 1;
    },
    [todos]
  );

  const on_remove = useCallback(
    (id) => {
      setTodos(todos.filter((todo) => todo.id !== id));
    },
    [todos]
  );

  const on_toggle = useCallback(
    (id) => {
      setTodos(
        todos.map((todo) =>
          todo.id == id ? { ...todo, checked: !todo.checked } : todo
        )
      );
    },
    [todos]
  );

  // Props data convert to json String
  const django_data = JSON.stringify(props);
  const todo_data = JSON.stringify(todos);

  return (
    <Fragment>
      <TodoTemplate>
        <TodoInsert on_insert={on_insert} />
        <TodoList todos={todos} on_remove={on_remove} on_toggle={on_toggle} />
        <span>
          <b>django3 </b> Passing the <b>Props:</b>
        </span>
        {nextId.current}
        <br />
        Raw : {django_data}
        <br />
        Raw.name : {props.name}
        <br />
        Raw more : {props.more}
        <br />
        {todo_data}
        {todos[0]["text"]}
        <p>Photo</p>
        <img width="500" height="500" src={dinoImg} />
      </TodoTemplate>
    </Fragment>
  );
};

export default Todo;
