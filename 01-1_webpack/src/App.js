import React, { Component } from 'react';
import { ReactDOM } from 'react-dom';


export default class LikeButton extends React.Component {
      
  constructor(props) {
    super(props);
    this.state = { liked: false };
    this.likeClick = this.likeClick.bind(this);
  }
  
  likeClick() {
    this.setState(state => ({
      liked: !state.liked
    }));
  }

  render() {
    return (
      <button onClick={this.likeClick}>
        {this.state.liked ? 'Like!!!' : 'UnLike.'}
      </button>
    )
  }
}


// export default LikeButton;
// ReactDOM.render(
//   <LikeButton />,
//   document.getElementById('like_button')
// );
