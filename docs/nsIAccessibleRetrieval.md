---
layout: default
---

# nsIAccessibleRetrieval #

An interface for in-process accessibility clients wishing to get an
nsIAccessible for a given DOM node.  More documentation at:
  http://www.mozilla.org/projects/ui/accessibility


## Methods ##

### getApplicationAccessible ###

Return application accessible.


### getAccessibleFor ###

Return an nsIAccessible for a DOM node in pres shell 0.
Create a new accessible of the appropriate type if necessary,
or use one from the accessibility cache if it already exists.
@param aNode The DOM node to get an accessible for.
@return The nsIAccessible for the given DOM node.


### getStringRole ###

Returns accessible role as a string.

@param aRole - the accessible role constants.


### getStringStates ###

Returns list which contains accessible states as a strings.

@param aStates - accessible states.
@param aExtraStates - accessible extra states.


### getStringEventType ###

Get the type of accessible event as a string.

@param aEventType - the accessible event type constant
@return - accessible event type presented as human readable string


### getStringRelationType ###

Get the type of accessible relation as a string.

@param aRelationType - the accessible relation type constant
@return - accessible relation type presented as human readable string


### getAccessibleFromCache ###

Return an accessible for the given DOM node from the cache.
@note  the method is intended for testing purposes

@param aNode  [in] the DOM node to get an accessible for

@return       cached accessible for the given DOM node if any


### createAccessiblePivot ###

Create a new pivot for tracking a position and traversing a subtree.

@param aRoot [in] the accessible root for the pivot
@return a new pivot


### setLogging ###

Enable logging for the given modules, all other modules aren't logged.

@param aModules [in] list of modules, format is comma separated list
                     like 'docload,doccreate'.
@note Works on debug build only.
@see Logging.cpp for list of possible values.


### isLogged ###

Return true if the given module is logged.

