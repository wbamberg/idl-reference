---
layout: default
---

# nsIUpdateTimerManager #

An interface describing a global application service that allows long
duration (e.g. 1-7 or more days, weeks or months) timers to be registered
and then fired.


## registerTimer ##

Register an interval with the timer manager. The timer manager
periodically checks to see if the interval has expired and if it has
calls the specified callback. This is persistent across application
restarts and can handle intervals of long durations.
@param   id
         An id that identifies the interval, used for persistence
@param   callback
         A nsITimerCallback object that is notified when the interval
         expires
@param   interval
         The length of time, in seconds, of the interval

Note: to avoid having to instantiate a component to call registerTimer
the component can intead register an update-timer category with comma
separated values as a single string representing the timer as follows.

_xpcom_categories: [{ category: "update-timer",
                      value: "contractID," +
                             "method," +
                             "id," +
                             "preference," +
                             "interval" }],
the values are as follows
  contractID : the contract ID for the component.
  method     : the method used to instantiate the interface. This should be
               either getService or createInstance depending on your
               component.
  id         : the id that identifies the interval, used for persistence.
  preference : the preference to for timer interval. This value can be
               optional by specifying an empty string for the value.
  interval   : the default interval in seconds for the timer.

