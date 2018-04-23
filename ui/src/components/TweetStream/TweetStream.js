import React, { Component } from 'react';
import Tweet from '../Tweet';

class TweetStream extends Component {
  constructor(props) {
    super(props);
    this.state = { tweets: [] };
    this.active = false;
  }

  componentDidMount() {
    this.active = true;
    this.fetchTweets();
  }

  componentWillUnmount() {
    this.active = false;
  }

  fetchTweets() {
    fetch('/stream/get-quotes/', { credentials: 'same-origin' })
      .then(response => response.json())
      .then((tweets) => {
        this.setState({
          tweets: this.state.tweets.concat(tweets)
        });
        if (this.active) {
          setTimeout(() => this.fetchTweets(), 3000);
        }
      }).catch(err => console.log(err));
  }

  render() {
    return (
      <div className="TweetStream">
        { this.state.tweets.map(tweet => <Tweet tweet={tweet}/>) }
      </div>
    );
  }
}

export default TweetStream;
