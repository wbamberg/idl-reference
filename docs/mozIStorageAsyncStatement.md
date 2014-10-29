---
layout: default
---

# mozIStorageAsyncStatement #

An asynchronous SQL statement.  This differs from mozIStorageStatement by
only being usable for asynchronous execution.  (mozIStorageStatement can
be used for both synchronous and asynchronous purposes.)  This specialization
for asynchronous operation allows us to avoid needing to acquire
synchronization primitives also used by the asynchronous execution thread.
In contrast, mozIStorageStatement may need to acquire the primitives and
consequently can cause the main thread to lock for extended intervals while
the asynchronous thread performs some long-running operation.

