import React, { PureComponent, Component, useState } from 'react';
import axios from 'axios';

const AjaxTest = () => {
  const [data, setData] = useState(null);
  const on_click = () => {
    axios
      .get('https://jsonplaceholder.typicode.com/todos/1')
      .then((response) => {
        setData(response.data);
      });
  };

  return (
    <div>
      <div className="">
        <button onClick={on_click}>불러오기</button>
      </div>
      {data && (
        <textarea
          row={7}
          value={JSON.stringify(data, null, 2)}
          readOnly={true}
        />
      )}
    </div>
  );
};

export default AjaxTest;
