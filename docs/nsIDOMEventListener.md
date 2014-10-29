---
layout: default
---

# nsIDOMEventListener #

The nsIDOMEventListener interface is a callback interface for
listening to events in the Document Object Model.

For more information on this interface please see 
http://www.w3.org/TR/DOM-Level-2-Events/


## Methods ##

### handleEvent ###

This method is called whenever an event occurs of the type for which 
the EventListener interface was registered.

@param   evt The Event contains contextual information about the 
             event. It also contains the stopPropagation and 
             preventDefault methods which are used in determining the 
             event's flow and default action.

