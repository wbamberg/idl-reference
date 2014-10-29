---
layout: default
---

# nsIConsoleMessage #

This is intended as a base interface; implementations may want to
provide an object that can be qi'ed to provide more specific
message information.


## debug ##
 Log level constants. */

## info ##

## warn ##

## error ##

## logLevel ##

The log level of this message.


## timeStamp ##

The time (in milliseconds from the Epoch) that the message instance
was initialised.
The timestamp is initialized as JS_now/1000 so that it can be
compared to Date.now in Javascript.


## message ##

## toString ##
