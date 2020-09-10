import React, { Fragment, useState, useRef, useCallback } from 'react';
import ReactDOM from 'react-dom';
import NewsViewer from './components/NewsViewer/NewsViewer';
import AjaxDjango from './components/Practice/AjaxDjango';

const App = () => {
  return (
    <Fragment>
      <AjaxDjango />
      <h2>React Form</h2>
      <NewsViewer />
    </Fragment>
  );
};

export default App;

// import AjaxTest from './components/Practice/AjaxTest';
// import NameForm from './components/Practice/NameForm';
{
  /* <h2>Axios API Test</h2>
<AjaxTest />
<br />
<h2>React Form</h2>
<NameForm />
<br /> */
}
