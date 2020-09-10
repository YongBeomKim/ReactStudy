import React from "react";
import "./TodoList.scss";
import TodoListItem from "./TodoListItem";

// { parametor.parent }
const TodoList = ({ todos, on_remove, on_toggle }) => {
  return (
    <div className="TodoList">
      {todos.map((todo) => (
        <TodoListItem
          todo={todo}
          key={todo.id}
          on_remove={on_remove}
          on_toggle={on_toggle}
        />
      ))}
    </div>
  );
};

export default TodoList;
