import React, { Component } from 'react';
// https://stackoverflow.com/questions/54345824/convert-html-form-with-action-to-react-form-submit-with-logic
class DjangoForm extends React.Component {
  state = { username: '' };
  myChangeHandler = (event) => {
    this.setState({ username: event.target.value });
  };
  render() {
    return (
      <form>
        <h1>Hello {this.state.username}</h1>
        <p>Enter your name:</p>
        <input type="text" onChange={this.myChangeHandler} />
      </form>
    );
  }
}

export default AjaxDjango;
