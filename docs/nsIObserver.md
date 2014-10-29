---
layout: default
---

# nsIObserver #

This interface is implemented by an object that wants
to observe an event corresponding to a topic.


## observe ##

Observe will be called when there is a notification for the
topic |aTopic|.  This assumes that the object implementing
this interface has been registered with an observer service
such as the nsIObserverService. 

If you expect multiple topics/subjects, the impl is 
responsible for filtering.

You should not modify, add, remove, or enumerate 
notifications in the implemention of observe. 

@param aSubject : Notification specific interface pointer.
@param aTopic   : The notification topic or subject.
@param aData    : Notification specific wide string.
                   subject event.

