import React, { Component } from 'react';
import 'semantic-ui-css/semantic.min.css';
import './App.css';

import Header from './components/Header';
import Poller from './components/Poller';
import TweetStream from './components/TweetStream';

import blackbirdLogo from './images/blackbird-logo.svg';
import archImage from './images/arch-diagram.png';

class App extends Component {
  render() {
    return (
    <div className="app">
      <Header />
      <div className="blackbird-header">
        <div className="container">
          <div className="blackbird-logo">
            <img alt="Blackbird" src={blackbirdLogo} />
            <span>Datawire Reference Architecture</span>
          </div>
          <a href="/ambassador/" className="blue-button step3">Diagnostics</a>
        </div>
      </div>
      <div className="container">
        <h4 className="label">Architecture</h4>
           <img alt="architecture" src={archImage} />
        <h4 className="label">Trending Tweets</h4>
        <TweetStream />
      </div>
    </div>);
  }
}
export default App;
