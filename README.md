# Demo notes

1. General architecture overview (Ambassador, tweeter, stream).
2. Create a sandbox for deployment.
   * `git branch`, `forge deploy` from top level app directory
   * Note: the tweeter doesn't go to the sandbox because it's development
3. Now, let's make a change to streams to anonymize the data.
   * We add the GDPR filter.
   * The filter has a sleep to simulate latency, and it anonymizes names.
4. We're going to test the change out by sending a curl with a tweet.

   ```
   curl -H "Content-Type: application/json" -d '{"author": "Albert Einstein", "created_at": "2018-05-25T07:06:34.127405", "text": "Genius."}' http://35.195.162.45/dev-rdl/stream/add-quotes/
   ```

   Note that the date is in the future so it shows up at the top of the trending tweets.

5. Look at the UI, it works.
6. So the change works with my test, but what about real production data? This is an important feature. We're going to deploy in shadow mode.
   * `forge --profile shadow deploy`
   * Two terminal windows:
     * `stern stream-stable` and `stern stream-shadow`
     * Note the anonymized data being logged
7. Let's take a look at metrics.
   * Grafana dashboard
   * You might want to set to last 15 minutes (upper right hand side) and hit refresh as well.
   * Oops, latency is high. We should fix that.
8. Let's clean up the shadow first.
   * `forge list`
   * `forge delete stream shadow`
9. Let's go back to our sandbox, and we also have a last minute feature request to only display 2 tweets.
   * `telepresence --swap-deployment stream-dev-rdl --docker-run --rm -it -v $(pwd):/service stream-dev:latest`
   * Let's change the SQL query from 4 to 2, and fix the sleep

# Configuration notes

The latency metrics used in the Grafana dashboard:

```
envoy_cluster_cluster_shadow_stream_shadow_datawire_svc_cluster_local_upstream_rq_time
envoy_cluster_cluster_stream_stable_datawire_svc_cluster_local_upstream_rq_time
```

Prometheus is available at:

```
kubectl port-forward prometheus-prometheus-0 9090
```

You can scale the tweeter like so:

```
kubectl scale --replicas=0 deploy/tweeter-stable
```

The tweeter, Ambassador, and monitoring directories are *not* deployed by default when creating a sandbox. 