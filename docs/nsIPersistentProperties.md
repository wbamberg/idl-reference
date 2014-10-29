---
layout: default
---

# nsIPersistentProperties #

## load ##

load a set of name/value pairs from the input stream
names and values should be in UTF8


## save ##

output the values to the stream - results will be in UTF8


## subclass ##

call subclass() to make future calls to load() set the properties
in this "superclass" instead


## enumerate ##

get an enumeration of nsIPropertyElement objects,
which are read-only (i.e. setting properties on the element will
not make changes back into the source nsIPersistentProperties


## getStringProperty ##

shortcut to nsIProperty's get() which retrieves a string value
directly (and thus faster)


## setStringProperty ##

shortcut to nsIProperty's set() which sets a string value
directly (and thus faster). If the given property already exists,
then the old value will be returned

