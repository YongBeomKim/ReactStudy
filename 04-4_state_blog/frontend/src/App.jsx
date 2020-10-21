import React from 'react';
import {Route, Switch, BrowserRouter as Router} from 'react-router-dom'
import Blog from './components/Blog';
import BlogDetail from './components/BlogDetail';
import Category from './components/Categoty';
import Home from './components/Home';
import Layout from './hocs/Layout';

const App = () => (
    <Router>
      <Layout>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/blog" component={Blog} />
          <Route exact path="/blog/:id" component={BlogDetail} />
          <Route exact path="/category/:id" component={Category} />
        </Switch>
      </Layout>    
    </Router>

);

export default App;
