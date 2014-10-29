---
layout: default
---

# nsIAsyncShutdownService #

A service that allows registering shutdown-time dependencies.


## makeBarrier ##

Create a new barrier.

By convention, the name should respect the following format:
"MyModuleName: Doing something while it's time"
e.g.
"OS.File: Waiting for clients to flush before shutting down"

This attribute is uploaded as part of crash reports.


## profileBeforeChange ##

Barrier for notification profile-before-change.


## profileChangeTeardown ##

Barrier for notification profile-change-teardown.


## sendTelemetry ##

Barrier for notification profile-before-change2.


## webWorkersShutdown ##

Barrier for notification web-workers-shutdown.


## xpcomThreadsShutdown ##

Barrier for notification xpcom-threads-shutdown.

