---
layout: default
---

# nsIProcess #

## Methods ##

### init ###

Initialises the process with an executable to be run. Call the run method
to run the executable.
@param executable The executable to run.


### kill ###

Kills the running process. After exiting the process will either have
been killed or a failure will have been returned.


### run ###

Executes the file this object was initialized with
@param blocking   Whether to wait until the process terminates before
returning or not.
@param args       An array of arguments to pass to the process in the
                  native character set.
@param count      The length of the args array.


### runAsync ###

Executes the file this object was initialized with optionally calling
an observer after the process has finished running.
@param args       An array of arguments to pass to the process in the
                  native character set.
@param count      The length of the args array.
@param observer   An observer to notify when the process has completed. It
                  will receive this process instance as the subject and
                  "process-finished" or "process-failed" as the topic. The
                  observer will be notified on the main thread.
@param holdWeak   Whether to use a weak reference to hold the observer.


### runw ###

Executes the file this object was initialized with
@param blocking   Whether to wait until the process terminates before
returning or not.
@param args       An array of arguments to pass to the process in UTF-16
@param count      The length of the args array.


### runwAsync ###

Executes the file this object was initialized with optionally calling
an observer after the process has finished running.
@param args       An array of arguments to pass to the process in UTF-16
@param count      The length of the args array.
@param observer   An observer to notify when the process has completed. It
                  will receive this process instance as the subject and
                  "process-finished" or "process-failed" as the topic. The
                  observer will be notified on the main thread.
@param holdWeak   Whether to use a weak reference to hold the observer.


## Attributes ##

### pid ###

The process identifier of the currently running process. This will only
be available after the process has started and may not be available on
some platforms.


### exitValue ###

The exit value of the process. This is only valid after the process has
exited.


### isRunning ###

Returns whether the process is currently running or not.

