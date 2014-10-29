---
layout: default
---

# nsIPrefLocalizedString #

The nsIPrefLocalizedString interface is simply a wrapper interface for
nsISupportsString so the preferences service can have a unique identifier
to distinguish between requests for normal wide strings (nsISupportsString)
and "localized" wide strings, which get their default values from properites
files.

@see nsIPrefBranch
@see nsISupportsString


## data ##

Provides access to string data stored in this property.

@throws Error An error occurred.


## toString ##

Used to retrieve the contents of this object into a wide string.

@return wstring The string containing the data stored within this object.


## setDataWithLength ##

Used to set the contents of this object.

@param length The length of the string. This value should not include
              space for the null terminator, nor should it account for the
              size of a character. It should  only be the number of
              characters for which there is space in the string.
@param data   The string data to be stored.

@note
This makes a copy of the string argument passed in.

