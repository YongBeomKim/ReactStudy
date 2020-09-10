import React, { Component, useState } from 'react';
import axios from 'axios';

const NewsViewer = () => {
  const url_link =
    'https://newsapi.org/v2/top-headlines?country=kr&apiKey=0a8c4202385d4ec1bb93b7e277b3c51f';

  const [data, setData] = useState(null);
  const on_click = async () => {
    try {
      const response = await axios.get(url_link);
      setData(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="">
      <div className="">
        <button onClick={on_click}>Loading..</button>
      </div>
      {data && (
        <textarea
          rows={7}
          readOnly={true}
          value={JSON.stringify(data, null, 2)}
        />
      )}
    </div>
  );
};

export default NewsViewer;
