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
    "text": "Imagine is more important than knowledge.",
    "created_at": "2018-04-18T08:53:38.755218"
  }
  {
    "author": "Albert Einstein",
    "text": "Imagine is more important than knowledge.",
    "created_at": "2018-04-18T08:53:38.755218"
}
]
```

This represents two tweets.