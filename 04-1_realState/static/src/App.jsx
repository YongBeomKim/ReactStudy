import React, { Fragment } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NotFound from './components/NotFound';
import About from './containers/About';
import Contact from './containers/Contact';
import Home from './containers/Home';
import ListingDetail from './containers/ListingDetail';
import Listing from './containers/Listings';
import LogIn from './containers/LogIn';
import SingUp from './containers/SignUp';
import Layout from './hocs/Layout';

import './sass/main.scss';

const App = () => {
  return (
    <Router>
      <Layout>
        <Switch>
          <Route exact paht="/" component={Home} />
          <Route exact paht="/about" component={About} />
          <Route exact paht="/contact" component={Contact} />
          <Route exact paht="/listings" component={Listing} />
          <Route exact paht="/listings/:id" component={ListingDetail} />
          <Route exact paht="/login" component={LogIn} />
          <Route exact paht="/signup" component={SingUp} />
          <Route component={NotFound} />
        </Switch>
      </Layout>
    </Router>
  );
};

export default App;
