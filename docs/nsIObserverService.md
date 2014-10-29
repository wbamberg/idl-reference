---
layout: default
---

# nsIObserverService #

nsIObserverService

Service allows a client listener (nsIObserver) to register and unregister for 
notifications of specific string referenced topic. Service also provides a 
way to notify registered listeners and a way to enumerate registered client 
listeners.


## addObserver ##

AddObserver

Registers a given listener for a notifications regarding the specified
topic.

@param anObserve : The interface pointer which will receive notifications.
@param aTopic    : The notification topic or subject.
@param ownsWeak  : If set to false, the nsIObserverService will hold a 
                   strong reference to |anObserver|.  If set to true and 
                   |anObserver| supports the nsIWeakReference interface,
                   a weak reference will be held.  Otherwise an error will be
                   returned.


## removeObserver ##

removeObserver

Unregisters a given listener from notifications regarding the specified
topic.

@param anObserver : The interface pointer which will stop recieving
                    notifications.
@param aTopic     : The notification topic or subject.


## notifyObservers ##

notifyObservers

Notifies all registered listeners of the given topic.

@param aSubject : Notification specific interface pointer.
@param aTopic   : The notification topic or subject.
@param someData : Notification specific wide string.


## enumerateObservers ##

enumerateObservers

Returns an enumeration of all registered listeners.

@param aTopic   : The notification topic or subject.

