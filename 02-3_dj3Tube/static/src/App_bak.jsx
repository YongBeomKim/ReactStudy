import React, { Component } from "react";
// import listData from "raw-loader!./list.json";
// import listData from "../public/list.json";

class Nav extends Component {
  state = {
    list: [],
  };

  render() {
    var listTag = [];
    for (var i = 0; i < this.props.list.length; i++) {
      var li = this.props.list[i];
      var liId = li.id;
      listTag.push(
        <li key={li.id}>
          <a
            href={li.id}
            data-id={li.id} // Assign Unique Number in Data Parametor
            onClick={function (event) {
              event.preventDefault();
              console.log(event.target.dataset.id + "th clicked");
              this.props.onClick(event.target.dataset.id);
            }.bind(this)}
          >
            {li.title}
          </a>
        </li>
      );
    }

    return (
      <nav>
        <ul>{listTag}</ul>
      </nav>
    );
  }
}

class Article extends Component {
  render() {
    return (
      <article>
        <h2>{this.props.title}</h2>
        {this.props.desc}
      </article>
    );
  }
}

export default class App extends Component {
  // state 초기값 선언
  state = {
    article: {
      item: { title: "welcome", desc: "Hello, React & Ajax" },
    },
    list: [],
  };

  componentDidMount() {
    // fetch("../media/list.json")
    fetch("../static/public/list.json")
      .then(function (result) {
        return result.json();
      })
      .then(
        function (json) {
          console.log(json);
          this.setState({ list: json });
        }.bind(this)
      );
  }

  render() {
    return (
      <div className="App">
        <h1>WEB</h1>
        <Nav
          list={this.state.list}
          // 개별 1.json 파일에서 Json 객체 호출
          onClick={function (id) {
            // fetch("../media/" + id + ".json")
            fetch("../static/public/" + id + ".json")
              .then(function (result) {
                return result.json();
              })
              .then(
                function (json) {
                  console.log(json);
                  this.setState({
                    article: {
                      title: json.title,
                      desc: json.desc,
                    },
                  });
                }.bind(this)
              );
          }.bind(this)}
        ></Nav>

        {/* The Way of InLine Props Assignment
        <Article title={"Welcome"} desc={"Hello, React & Ajax"}>
        </Article>
         */}
        <Article
          title={this.state.article.title}
          desc={this.state.article.desc}
        />
      </div>
    );
  }
}
