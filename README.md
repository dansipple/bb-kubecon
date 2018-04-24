# Demo notes

1


-> stream
   -> stream-stable 
   -> stream-dev (gdpr)


1. tweet -> ambassador -> stream
2. create sandbox for development
   * git branch
   * forge deploy
3. now, let's make a change to streams
   * anonymize the data
   * make change
   * deploy
4. test in my sandbox with curl -X
   * look at the UI
5. now I leave my sandbox, and shadow with prod traffic
   * forge deploy --shadow
6. now, I deploy to canary
7. now, change in requirements
   * telepresence






* writing a new service that processes the data stream (e.g., GDPR, analytics)
* updating a service (refactoring) -- change the data storage architecture
  * in both of these cases, you want to test correctness, not just a failure

* so we update a service and change from sqlite to cloud SQL
  * then we can query the databases and do a diff to make sure it's the same
* we want to update the service and add IP address?

* what are the use cases for diffy?


## Questions?

Join our [Gitter chat](https://gitter.im/datawire/users) or email hello@datawire.io.
