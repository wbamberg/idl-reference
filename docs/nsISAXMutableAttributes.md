---
layout: default
---

# nsISAXMutableAttributes #

This interface extends the nsISAXAttributes interface with
manipulators so that the list can be modified or reused.


## Methods ##

### addAttribute ###

Add an attribute to the end of the list.

For the sake of speed, this method does no checking
to see if the attribute is already in the list: that is
the responsibility of the application.

@param uri The Namespace URI, or the empty string if
       none is available or Namespace processing is not
       being performed.
@param localName The local name, or the empty string if
       Namespace processing is not being performed.
@param qName The qualified (prefixed) name, or the empty string
       if qualified names are not available.
@param type The attribute type as a string.
@param value The attribute value.


### clear ###

Clear the attribute list for reuse.


### removeAttribute ###

Remove an attribute from the list.

@param index The index of the attribute (zero-based).


### setAttributes ###

Set the attributes list. This method will clear any attributes in
the list before adding the attributes from the argument.

@param attributes The attributes object to replace populate the
                  list with.


### setAttribute ###

Set an attribute in the list.

For the sake of speed, this method does no checking for name
conflicts or well-formedness: such checks are the responsibility
of the application.

@param index The index of the attribute (zero-based).
@param uri The Namespace URI, or the empty string if
       none is available or Namespace processing is not
       being performed.
@param localName The local name, or the empty string if
       Namespace processing is not being performed.
@param qName The qualified name, or the empty string
       if qualified names are not available.
@param type The attribute type as a string.
@param value The attribute value.


### setLocalName ###

Set the local name of a specific attribute.

@param index The index of the attribute (zero-based).
@param localName The attribute's local name, or the empty
       string for none.


### setQName ###

Set the qualified name of a specific attribute.

@param index The index of the attribute (zero-based).
@param qName The attribute's qualified name, or the empty
       string for none.


### setType ###

Set the type of a specific attribute.

@param index The index of the attribute (zero-based).
@param type The attribute's type.


### setURI ###

Set the Namespace URI of a specific attribute.

@param index The index of the attribute (zero-based).
@param uri The attribute's Namespace URI, or the empty
       string for none.


### setValue ###

Set the value of a specific attribute.

@param index The index of the attribute (zero-based).
@param value The attribute's value.

