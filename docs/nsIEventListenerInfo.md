---
layout: default
---

# nsIEventListenerInfo #

An instance of this interface describes how an event listener
was added to an event target.


## type ##

The type of the event for which the listener was added.
Null if the listener is for all the events.


## capturing ##

## allowsUntrusted ##

## inSystemEventGroup ##

## listenerObject ##

The underlying JS object of the event listener, if this listener
has one.  Null otherwise.


## toSource ##

Tries to serialize event listener to a string.
Returns null if serialization isn't possible
(for example with C++ listeners).

