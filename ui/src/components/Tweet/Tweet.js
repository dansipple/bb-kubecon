import React from 'react';
import moment from 'moment';

const Tweet = ({ tweet }) => (
  <div className="Tweet">
    <div className="top">
      <span className="author">{tweet.author}</span> · <span className="time">{moment(tweet.created_at).fromNow()}</span>
    </div>
    <div className="body">{tweet.text}</div>
    <div className="actions">
      <i className="fa fa-comment-o" />
      <i className="fa fa-retweet" />
      <i className="fa fa-heart-o" />
    </div>
  </div>
);

export default Tweet;
