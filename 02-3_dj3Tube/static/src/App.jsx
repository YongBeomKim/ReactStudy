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

class NowLoading extends Component {
  render() {
    return <div>Now is Loading.....</div>;
  }
}

export default class App extends Component {
  // state 초기값 선언
  state = {
    article: {
      item: { title: "welcome", desc: "Hello, React & Ajax" },
      isLoading: false,
    },
    list: {
      items: [],
      isLoading: false,
    },
  };

  componentDidMount() {
    var newList = Object.assign({}, this.state.list, { isLoading: true });
    this.setState({
      list: newList,
    });

    // fetch("../media/list.json")
    // fetch("public/list.json")
    fetch("../static/public/list.json")
      .then(function (result) {
        return result.json();
      })
      .then(
        function (json) {
          console.log(json);
          this.setState({ list: { items: json, isLoading: false } });
        }.bind(this)
      );
  }

  render() {
    var NavTag = null;
    if (this.state.list.isLoading) {
      NavTag = <NowLoading></NowLoading>;
    } else {
      NavTag = (
        <Nav
          list={this.state.list.items}
          // 개별 1.json 파일에서 Json 객체 호출
          onClick={function (id) {
            var newArticle = Object.assign({}, this.state.article, {
              isLoading: true,
            });
            this.setState({
              article: newArticle,
            });
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
                      item: {
                        title: json.title,
                        desc: json.desc,
                      },
                    },
                  });
                }.bind(this)
              );
          }.bind(this)}
        ></Nav>
      );
    }

    var ArticleTag = null;
    if (this.state.article.isLoading) {
      ArticleTag = <NowLoading></NowLoading>;
    } else {
      ArticleTag = (
        <Article
          title={this.state.article.item.title}
          desc={this.state.article.item.desc}
        />
      );
    }

    return (
      <div className="App">
        <h1>WEB</h1>

        {NavTag}

        {/* The Way of InLine Props Assignment
        <Article title={"Welcome"} desc={"Hello, React & Ajax"}>
        </Article>
         */}

        {ArticleTag}
      </div>
    );
  }
}
