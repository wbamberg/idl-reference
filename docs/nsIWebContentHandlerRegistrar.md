---
layout: default
---

# nsIWebContentHandlerRegistrar #

nsIWebContentHandlerRegistrar

Applications wishing to use web content handlers need to implement this
interface. Typically they will prompt the user to confirm adding an entry
to the local list. 

The component must have the contract id defined below so that nsNavigator
can invoke it. 


## registerContentHandler ##

See documentation in Navigator.webidl
The additional contentWindow param for both methods represents the dom
content window from which the method has been called.


## registerProtocolHandler ##
