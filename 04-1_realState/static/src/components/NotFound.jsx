import React, { Component } from 'react';
import '../sass/components/_notfound.scss';

const NotFound = () => (
  <div className="notfound">
    <h1 className="notfound__heading">404 Not Found</h1>
    <p className="notfound__paragraph">
      The link you requested does not exist..
    </p>
  </div>
);

export default NotFound;
