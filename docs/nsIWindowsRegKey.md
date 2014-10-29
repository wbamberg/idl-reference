---
layout: default
---

# nsIWindowsRegKey #

This interface is designed to provide scriptable access to the Windows
registry system ("With Great Power Comes Great Responsibility").  The
interface represents a single key in the registry.

This interface is highly Win32 specific.


## ROOT_KEY_CLASSES_ROOT ##

Root keys.  The values for these keys correspond to the values from
WinReg.h in the MS Platform SDK.  The ROOT_KEY_ prefix corresponds to the
HKEY_ prefix in the MS Platform SDK.

This interface is not restricted to using only these root keys.


## ROOT_KEY_CURRENT_USER ##

## ROOT_KEY_LOCAL_MACHINE ##

## ACCESS_BASIC ##

Values for the mode parameter passed to the open and create methods.
The values defined here correspond to the REGSAM values defined in
WinNT.h in the MS Platform SDK, where ACCESS_ is replaced with KEY_.

This interface is not restricted to using only these access types.


## ACCESS_QUERY_VALUE ##

## ACCESS_SET_VALUE ##

## ACCESS_CREATE_SUB_KEY ##

## ACCESS_ENUMERATE_SUB_KEYS ##

## ACCESS_NOTIFY ##

## ACCESS_READ ##

## ACCESS_WRITE ##

## ACCESS_ALL ##

## WOW64_32 ##

## WOW64_64 ##

## TYPE_NONE ##

Values for the type of a registry value.  The numeric values of these
constants are taken directly from WinNT.h in the MS Platform SDK.
The Microsoft documentation should be consulted for the exact meaning of
these value types.

This interface is somewhat restricted to using only these value types.
There is no method that is directly equivalent to RegQueryValueEx or
RegSetValueEx.  In particular, this interface does not support the
REG_MULTI_SZ and REG_EXPAND_SZ value types.  It is still possible to
enumerate values that have other types (i.e., getValueType may return a
type not defined below).


## TYPE_STRING ##

## TYPE_BINARY ##

## TYPE_INT ##

## TYPE_INT64 ##

## key ##

This attribute exposes the native HKEY and is available to provide C++
consumers with the flexibility of making other Windows registry API calls
that are not exposed via this interface.

It is possible to initialize this object by setting an HKEY on it.  In
that case, it is the responsibility of the consumer setting the HKEY to
ensure that it is a valid HKEY.

WARNING: Setting the key does not close the old key.


## close ##

This method closes the key.  If the key is already closed, then this
method does nothing.


## open ##

This method opens an existing key.  This method fails if the key
does not exist.

NOTE: On 32-bit Windows, it is valid to pass any HKEY as the rootKey
parameter of this function.  However, for compatibility with 64-bit
Windows, that usage should probably be avoided in favor of openChild.

@param rootKey
       A root key defined above or any valid HKEY on 32-bit Windows.
@param relPath
       A relative path from the given root key.
@param mode
       Access mode, which is a bit-wise OR of the ACCESS_ values defined
       above.


## create ##

This method opens an existing key or creates a new key.

NOTE: On 32-bit Windows, it is valid to pass any HKEY as the rootKey
parameter of this function.  However, for compatibility with 64-bit
Windows, that usage should probably be avoided in favor of createChild.

@param rootKey
       A root key defined above or any valid HKEY on 32-bit Windows.
@param relPath
       A relative path from the given root key.
@param mode
       Access mode, which is a bit-wise OR of the ACCESS_ values defined
       above.


## openChild ##

This method opens a subkey relative to this key.  This method fails if the
key does not exist.

@return nsIWindowsRegKey for the newly opened subkey.


## createChild ##

This method opens or creates a subkey relative to this key.

@return nsIWindowsRegKey for the newly opened or created subkey.


## childCount ##

This attribute returns the number of child keys.


## getChildName ##

This method returns the name of the n'th child key.

@param index
       The index of the requested child key.


## hasChild ##

This method checks to see if the key has a child by the given name.

@param name
       The name of the requested child key.


## valueCount ##

This attribute returns the number of values under this key.


## getValueName ##

This method returns the name of the n'th value under this key.

@param index
       The index of the requested value.


## hasValue ##

This method checks to see if the key has a value by the given name.

@param name
       The name of the requested value.


## removeChild ##

This method removes a child key and all of its values.  This method will
fail if the key has any children of its own. 

@param relPath
       The relative path from this key to the key to be removed.


## removeValue ##

This method removes the value with the given name.

@param name
       The name of the value to be removed.


## getValueType ##

This method returns the type of the value with the given name.  The return
value is one of the "TYPE_" constants defined above.

@param name
       The name of the value to query.


## readStringValue ##

This method reads the string contents of the named value as a Unicode
string.

@param name
       The name of the value to query.  This parameter can be the empty
       string to request the key's default value.


## readIntValue ##

This method reads the integer contents of the named value.

@param name
       The name of the value to query.


## readInt64Value ##

This method reads the 64-bit integer contents of the named value.

@param name
       The name of the value to query.


## readBinaryValue ##

This method reads the binary contents of the named value under this key.

JavaScript callers should take care with the result of this method since
it will be byte-expanded to form a JS string.  (The binary data will be
treated as an ISO-Latin-1 character string, which it is not).

@param name
       The name of the value to query.


## writeStringValue ##

This method writes the unicode string contents of the named value.  The
value will be created if it does not already exist.

@param name
       The name of the value to modify.  This parameter can be the empty
       string to modify the key's default value.
@param data
       The data for the value to modify.


## writeIntValue ##

This method writes the integer contents of the named value.  The value
will be created if it does not already exist.

@param name
       The name of the value to modify.
@param data
       The data for the value to modify.


## writeInt64Value ##

This method writes the 64-bit integer contents of the named value.  The
value will be created if it does not already exist.

@param name
       The name of the value to modify.
@param data
       The data for the value to modify.


## writeBinaryValue ##

This method writes the binary contents of the named value.  The value will
be created if it does not already exist.

JavaScript callers should take care with the value passed to this method
since it will be truncated from a JS string (unicode) to a ISO-Latin-1
string.  (The binary data will be treated as an ISO-Latin-1 character
string, which it is not).  So, JavaScript callers should only pass
character values in the range \u0000 to \u00FF, or else data loss will
occur.

@param name
       The name of the value to modify.
@param data
       The data for the value to modify.


## startWatching ##

This method starts watching the key to see if any of its values have
changed.  The key must have been opened with mode including ACCESS_NOTIFY.
If recurse is true, then this key and any of its descendant keys are
watched.  Otherwise, only this key is watched.

@param recurse
       Indicates whether or not to also watch child keys.


## stopWatching ##

This method stops any watching of the key initiated by a call to
startWatching.  This method does nothing if the key is not being watched.


## isWatching ##

This method returns true if the key is being watched for changes (i.e.,
if startWatching() was called).


## hasChanged ##

This method returns true if the key has changed and false otherwise.
This method will always return false if startWatching was not called.

