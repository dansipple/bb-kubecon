# Demo notes

1


-> stream
   -> stream-stable 
   -> stream-dev (gdpr)


kubectl scale --replicas=0 deploy/tweeter-stable


1. tweet -> ambassador -> stream



2. create sandbox for development
   * git branch
   * forge deploy

Note:
* The tweets are being updated because it's in its own sandbox
  No prod traffic


3. now, let's make a change to streams
   * anonymize the data
   * make change
   * deploy
4. test in my sandbox with: (note that the date is in the future to insure it shows up)

curl -H "Content-Type: application/json" -d '{"author": "Albert Einstein", "created_at": "2018-05-25T07:06:34.127405", "text": "Genius."}' http://35.195.162.45/dev-rdl/stream/add-quotes/

   * look at the UI
5. OK, that works great, but what about real data?
   * forge deploy --shadow

stern to watch the logs; looks good

6. let's also look at metrics to see if it's impacted performance

7. let me clean up
   * forge list --> this gives you tracability
   * forge delete stream shadow

8. OK, I want to roll this into production ... but last minute request! We want to only display 2 tweets instead of 4.

9. Let's do some coding in our sandbox. Instead of just doing the deploy though, we're going to do some real-time coding.
   * telepresence --run-container 

7. now, change in requirements
   * telepresence
8. metrics/grafana


Things that shouldn't be part of the app:

* Ambassador
* GDPR
* Tweeter
* Monitoring








* writing a new service that processes the data stream (e.g., GDPR, analytics)
* updating a service (refactoring) -- change the data storage architecture
  * in both of these cases, you want to test correctness, not just a failure

* so we update a service and change from sqlite to cloud SQL
  * then we can query the databases and do a diff to make sure it's the same
* we want to update the service and add IP address?

* what are the use cases for diffy?


## Questions?

Join our [Gitter chat](https://gitter.im/datawire/users) or email hello@datawire.io.
