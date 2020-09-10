import React, { useState, useCallback } from "react";
import { MdAdd } from "react-icons/md";
import "./TodoInsert.scss";

const TodoInsert = ({ on_insert }) => {
  const [value, setValue] = useState("");

  const on_change = useCallback((e) => {
    setValue(e.target.value);
  }, []);

  const on_submit = useCallback(
    (e) => {
      on_insert(value);
      setValue(""); // value initialized
      e.preventDefault(); // Prevented refresh page for Submit event
    },
    [on_insert, value]
  );

  return (
    <form className="TodoInsert" onSubmit={on_submit}>
      <input placeholder="Insert To do" value={value} onChange={on_change} />
      <button type="submit">
        <MdAdd />
      </button>
    </form>
  );
};

export default TodoInsert;
