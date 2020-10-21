import React, { Fragment } from 'react'
import { Link } from 'react-router-dom'

const Home = () => (
  <Fragment className="">
    <div className="jumbotron container mt-5">
      <h1 className="display-4">Welcome to Blog life.</h1>
      <p className="lead">We makr all kinds of awecone blog about varius topics.</p>
      <hr className="my-4" />
      <p>Click the button blow to check out our awecome blog.</p>
      <Link className="btn btn-primary btn-lg" to="/blog/" role="button">Check out Our Blog</Link>
    </div>
  </Fragment>
)

export default Home;