---
layout: default
---

# nsIJSON #

Don't use this!  Use JSON.parse and JSON.stringify directly.


## encode ##

New users should use JSON.stringify!
The encode() method is only present for backward compatibility.
encode() is not a conforming JSON stringify implementation!


## encodeToStream ##

New users should use JSON.stringify.
You may also want to have a look at nsIConverterOutputStream.

The encodeToStream() method is only present for backward compatibility.
encodeToStream() is not a conforming JSON stringify implementation!


## decode ##

New users should use JSON.parse!
The decode() method is only present for backward compatibility.


## decodeFromStream ##

## encodeFromJSVal ##

## decodeToJSVal ##
