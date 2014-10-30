---
layout: default
---

# nsITimer #
  
nsITimer instances must be initialized by calling one of the "init" methods  
documented below.  You may also re-initialize (using one of the init()  
methods) an existing instance to avoid the overhead of destroying and  
creating a timer.  It is not necessary to cancel the timer in that case.  
  
By default a timer will fire on the thread that created it.  Set the .target  
attribute to fire on a different thread.  Once you have set a timer's .target  
and called one of its init functions, any further interactions with the timer  
(calling cancel(), changing member fields, etc) should only be done by the  
target thread, or races may occur with bad results like timers firing after  
they've been canceled, and/or not firing after re-initiatization.  
  

## Methods ##

### init ###
  
Initialize a timer that will fire after the said delay.  
A user must keep a reference to this timer till it is   
is no longer needed or has been cancelled.  
  
@param aObserver   the callback object that observes the   
                   ``timer-callback'' topic with the subject being  
                   the timer itself when the timer fires:  
  
                   observe(nsISupports aSubject, => nsITimer  
                           string aTopic,        => ``timer-callback''  
                           wstring data          =>  null  
  
@param aDelay      delay in milliseconds for timer to fire  
@param aType       timer type per TYPE* consts defined above  
  

### initWithFuncCallback ###
  
Initialize a timer to fire after the given millisecond interval.  
This version takes a function to call and a closure to pass to  
that function.  
  
@param aFunc      The function to invoke  
@param aClosure   An opaque pointer to pass to that function  
@param aDelay     The millisecond interval  
@param aType      Timer type per TYPE* consts defined above  
  

### initWithCallback ###
  
Initialize a timer to fire after the given millisecond interval.  
This version takes a function to call.  
  
@param aFunc      nsITimerCallback interface to call when timer expires  
@param aDelay     The millisecond interval  
@param aType      Timer type per TYPE* consts defined above  
  

### cancel ###
  
Cancel the timer.  This method works on all types, not just on repeating  
timers -- you might want to cancel a TYPE_ONE_SHOT timer, and even reuse  
it by re-initializing it (to avoid object destruction and creation costs  
by conserving one timer instance).  
  

## Attributes ##

### delay ###
  
The millisecond delay of the timeout.  
  
NOTE: Re-setting the delay on a one-shot timer that has already fired  
doesn't restart the timer. Call one of the init() methods to restart  
a one-shot timer.  
  

### type ###
  
The timer type - one of the above TYPE_* constants.  
  

### closure ###
  
The opaque pointer pass to initWithFuncCallback.  
  

### callback ###
  
The nsITimerCallback object passed to initWithCallback.  
  

### target ###
  
The nsIEventTarget where the callback will be dispatched. Note that this  
target may only be set before the call to one of the init methods above.  
  
By default the target is the thread that created the timer.  
  

## Constants ##

### TYPE_ONE_SHOT ###
  
Type of a timer that fires once only.  
  

### TYPE_REPEATING_SLACK ###
  
After firing, a TYPE_REPEATING_SLACK timer is stopped and not restarted  
until its callback completes.  Specified timer period will be at least  
the time between when processing for last firing the callback completes  
and when the next firing occurs.  
  
This is the preferable repeating type for most situations.  
  

### TYPE_REPEATING_PRECISE ###
  
An TYPE_REPEATING_PRECISE repeating timer aims to have constant period  
between firings.  The processing time for each timer callback should not  
influence the timer period.  However, if the processing for the last  
timer firing could not be completed until just before the next firing  
occurs, then you could have two timer notification routines being  
executed in quick succession.  Furthermore, if your callback processing  
time is longer than the timer period, then the timer will post more  
notifications while your callback is running.  For example, if a  
REPEATING_PRECISE timer has a 10ms period and a callback takes 50ms,  
then by the time the callback is done there will be 5 events to run the  
timer callback in the event queue.  Furthermore, the next scheduled time  
will always advance by exactly the delay every time the timer fires.  
This means that if the clock increments without the timer thread running  
(e.g. the computer is asleep) when the timer thread gets to run again it  
will post all the events that it "missed" while it wasn't running.  Use  
this timer type with extreme caution.  Chances are, this is not what you  
want.  
  

### TYPE_REPEATING_PRECISE_CAN_SKIP ###
  
A TYPE_REPEATING_PRECISE_CAN_SKIP repeating timer aims to have constant  
period between firings.  The processing time for each timer callback  
should not influence the timer period.  However this timer type  
guarantees that it will not queue up new events to fire the callback  
until the previous callback event finishes firing.  If the callback  
takes a long time, then the next callback will be scheduled immediately  
afterward, but only once, unlike TYPE_REPEATING_PRECISE.  If you want a  
non-slack timer, you probably want this one.  
  
