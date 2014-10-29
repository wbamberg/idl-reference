---
layout: default
---

# nsIAppShell #

Interface for the native event system layer.  This interface is designed
to be used on the main application thread only.


## Methods ##

### run ###

Enter an event loop.  Don't leave until exit() is called.


### exit ###

Exit the handle event loop


### favorPerformanceHint ###

Give hint to native event queue notification mechanism. If the native
platform needs to tradeoff performance vs. native event starvation this
hint tells the native dispatch code which to favor.  The default is to
prevent native event starvation.

Calls to this function may be nested. When the number of calls that pass
PR_TRUE is subtracted from the number of calls that pass PR_FALSE is
greater than 0, performance is given precedence over preventing event
starvation.

The starvationDelay arg is only used when favorPerfOverStarvation is
PR_FALSE. It is the amount of time in milliseconds to wait before the
PR_FALSE actually takes effect.


### suspendNative ###

Suspends the use of additional platform-specific methods (besides the
nsIAppShell->run() event loop) to run Gecko events on the main
application thread.  Under some circumstances these "additional methods"
can cause Gecko event handlers to be re-entered, sometimes leading to
hangs and crashes.  Calls to suspendNative() and resumeNative() may be
nested.  On some platforms (those that don't use any "additional
methods") this will be a no-op.  Does not (in itself) stop Gecko events
from being processed on the main application thread.  But if the
nsIAppShell->run() event loop is blocked when this call is made, Gecko
events will stop being processed until resumeNative() is called (even
if a plugin or library is temporarily processing events on a nested
event loop).


### resumeNative ###

Resumes the use of additional platform-specific methods to run Gecko
events on the main application thread.  Calls to suspendNative() and
resumeNative() may be nested.  On some platforms this will be a no-op.


### runInStableState ###

Allows running of a "synchronous section", in the form of an nsIRunnable
once the event loop has reached a "stable state". We've reached a stable
state when the currently executing task/event has finished, see:
http://www.whatwg.org/specs/web-apps/current-work/multipage/webappapis.html#synchronous-section
In practice this runs aRunnable once the currently executing event
finishes. If called multiple times per task/event, all the runnables will
be executed, in the order in which runInStableState() was called.


### runBeforeNextEvent ###

Run the given runnable before the next iteration of the event loop (this
includes native events too). If a nested loop is spawned within the current
event then the runnable will not be run until that loop has terminated.


## Attributes ##

### eventloopNestingLevel ###

The current event loop nesting level.

