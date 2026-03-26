## Java behaves differently in Kubernetes than it does on your laptop.
I recently explored a few subtle JVM traps that can cause:
Unexpected latency spikes
Silent OOMKills
JVM silently choosing the wrong garbage collector
All without a single error in your logs.
It turns out JVM ergonomics and container limits don't always align the way we expect.
Wrote a short article breaking down what's happening under the hood — and the flags that fixed it.