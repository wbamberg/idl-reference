---
layout: default
---

# nsIDirectoryEnumerator #

This interface provides a means for enumerating the contents of a directory.
It is similar to nsISimpleEnumerator except the retrieved entries are QI'ed 
to nsIFile, and there is a mechanism for closing the directory when the 
enumeration is complete.


## Methods ##

### close ###

Closes the directory being enumerated, releasing the system resource.
@throws NS_OK if the call succeeded and the directory was closed.
        NS_ERROR_FAILURE if the directory close failed. 
        It is safe to call this function many times. 


## Attributes ##

### nextFile ###

Retrieves the next file in the sequence. The "nextFile" element is the 
first element upon the first call. This attribute is null if there is no 
next element.

