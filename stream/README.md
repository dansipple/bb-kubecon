# Stream

Start it locally:

```
app.py
```

This will start on 8080. You can test it out by doing:

`curl http:///localhost:8080/get-quotes`

which should return some JSON:

```
[
  {
    "author": "Albert Einstein",
    "created_at": "2012-04-05",
    "text": "Imagine is more important than knowledge."
  },
  {
    "author": "Albert Einstein",
    "created_at": "2012-04-05",
    "text": "Imagine is more important than knowledgs."
  }
]
```

This represents two tweets.