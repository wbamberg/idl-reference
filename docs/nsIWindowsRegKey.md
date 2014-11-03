---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIWindowsRegKey.idl">Source file</a>
</div>

# nsIWindowsRegKey #
<code>  
This interface is designed to provide scriptable access to the Windows  
registry system ("With Great Power Comes Great Responsibility").  The  
interface represents a single key in the registry.  
  
This interface is highly Win32 specific.  
  
</code>
## Methods ##

### close() ###
<code>  
This method closes the key.  If the key is already closed, then this  
method does nothing.  
  
</code>
### open(rootKey, relPath, mode) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>rootKey</td>
<td>       A root key defined above or any valid HKEY on 32-bit Windows.  
</td>
</tr>

<tr>
<td>relPath</td>
<td>       A relative path from the given root key.  
</td>
</tr>

<tr>
<td>mode</td>
<td>       Access mode, which is a bit-wise OR of the ACCESS_ values defined  
       above.  
</td>
</tr>

</table>

### create(rootKey, relPath, mode) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>rootKey</td>
<td>       A root key defined above or any valid HKEY on 32-bit Windows.  
</td>
</tr>

<tr>
<td>relPath</td>
<td>       A relative path from the given root key.  
</td>
</tr>

<tr>
<td>mode</td>
<td>       Access mode, which is a bit-wise OR of the ACCESS_ values defined  
       above.  
</td>
</tr>

</table>

### openChild(relPath, mode) ###
<code>  
This method opens a subkey relative to this key.  This method fails if the  
key does not exist.  
  
@return nsIWindowsRegKey for the newly opened subkey.  
  
</code>
#### Returns ####

<table>

<tr>
<td>nsIWindowsRegKey for the newly opened subkey.  
</td>
</tr>

</table>

### createChild(relPath, mode) ###
<code>  
This method opens or creates a subkey relative to this key.  
  
@return nsIWindowsRegKey for the newly opened or created subkey.  
  
</code>
#### Returns ####

<table>

<tr>
<td>nsIWindowsRegKey for the newly opened or created subkey.  
</td>
</tr>

</table>

### getChildName(index) ###
<code>  
This method returns the name of the n'th child key.  
  
@param index  
       The index of the requested child key.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>index</td>
<td>       The index of the requested child key.  
</td>
</tr>

</table>

### hasChild(name) ###
<code>  
This method checks to see if the key has a child by the given name.  
  
@param name  
       The name of the requested child key.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the requested child key.  
</td>
</tr>

</table>

### getValueName(index) ###
<code>  
This method returns the name of the n'th value under this key.  
  
@param index  
       The index of the requested value.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>index</td>
<td>       The index of the requested value.  
</td>
</tr>

</table>

### hasValue(name) ###
<code>  
This method checks to see if the key has a value by the given name.  
  
@param name  
       The name of the requested value.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the requested value.  
</td>
</tr>

</table>

### removeChild(relPath) ###
<code>  
This method removes a child key and all of its values.  This method will  
fail if the key has any children of its own.   
  
@param relPath  
       The relative path from this key to the key to be removed.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>relPath</td>
<td>       The relative path from this key to the key to be removed.  
</td>
</tr>

</table>

### removeValue(name) ###
<code>  
This method removes the value with the given name.  
  
@param name  
       The name of the value to be removed.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to be removed.  
</td>
</tr>

</table>

### getValueType(name) ###
<code>  
This method returns the type of the value with the given name.  The return  
value is one of the "TYPE_" constants defined above.  
  
@param name  
       The name of the value to query.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to query.  
</td>
</tr>

</table>

### readStringValue(name) ###
<code>  
This method reads the string contents of the named value as a Unicode  
string.  
  
@param name  
       The name of the value to query.  This parameter can be the empty  
       string to request the key's default value.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to query.  This parameter can be the empty  
       string to request the key's default value.  
</td>
</tr>

</table>

### readIntValue(name) ###
<code>  
This method reads the integer contents of the named value.  
  
@param name  
       The name of the value to query.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to query.  
</td>
</tr>

</table>

### readInt64Value(name) ###
<code>  
This method reads the 64-bit integer contents of the named value.  
  
@param name  
       The name of the value to query.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to query.  
</td>
</tr>

</table>

### readBinaryValue(name) ###
<code>  
This method reads the binary contents of the named value under this key.  
  
JavaScript callers should take care with the result of this method since  
it will be byte-expanded to form a JS string.  (The binary data will be  
treated as an ISO-Latin-1 character string, which it is not).  
  
@param name  
       The name of the value to query.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to query.  
</td>
</tr>

</table>

### writeStringValue(name, data) ###
<code>  
This method writes the unicode string contents of the named value.  The  
value will be created if it does not already exist.  
  
@param name  
       The name of the value to modify.  This parameter can be the empty  
       string to modify the key's default value.  
@param data  
       The data for the value to modify.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to modify.  This parameter can be the empty  
       string to modify the key's default value.  
</td>
</tr>

<tr>
<td>data</td>
<td>       The data for the value to modify.  
</td>
</tr>

</table>

### writeIntValue(name, data) ###
<code>  
This method writes the integer contents of the named value.  The value  
will be created if it does not already exist.  
  
@param name  
       The name of the value to modify.  
@param data  
       The data for the value to modify.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to modify.  
</td>
</tr>

<tr>
<td>data</td>
<td>       The data for the value to modify.  
</td>
</tr>

</table>

### writeInt64Value(name, data) ###
<code>  
This method writes the 64-bit integer contents of the named value.  The  
value will be created if it does not already exist.  
  
@param name  
       The name of the value to modify.  
@param data  
       The data for the value to modify.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to modify.  
</td>
</tr>

<tr>
<td>data</td>
<td>       The data for the value to modify.  
</td>
</tr>

</table>

### writeBinaryValue(name, data) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The name of the value to modify.  
</td>
</tr>

<tr>
<td>data</td>
<td>       The data for the value to modify.  
</td>
</tr>

</table>

### startWatching(recurse) ###
<code>  
This method starts watching the key to see if any of its values have  
changed.  The key must have been opened with mode including ACCESS_NOTIFY.  
If recurse is true, then this key and any of its descendant keys are  
watched.  Otherwise, only this key is watched.  
  
@param recurse  
       Indicates whether or not to also watch child keys.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>recurse</td>
<td>       Indicates whether or not to also watch child keys.  
</td>
</tr>

</table>

### stopWatching() ###
<code>  
This method stops any watching of the key initiated by a call to  
startWatching.  This method does nothing if the key is not being watched.  
  
</code>
### isWatching() ###
<code>  
This method returns true if the key is being watched for changes (i.e.,  
if startWatching() was called).  
  
</code>
### hasChanged() ###
<code>  
This method returns true if the key has changed and false otherwise.  
This method will always return false if startWatching was not called.  
  
</code>
## Attributes ##

### key ###
  
This attribute exposes the native HKEY and is available to provide C++  
consumers with the flexibility of making other Windows registry API calls  
that are not exposed via this interface.  
  
It is possible to initialize this object by setting an HKEY on it.  In  
that case, it is the responsibility of the consumer setting the HKEY to  
ensure that it is a valid HKEY.  
  
WARNING: Setting the key does not close the old key.  
  

### childCount ###
  
This attribute returns the number of child keys.  
  

### valueCount ###
  
This attribute returns the number of values under this key.  
  

## Constants ##

### ROOT_KEY_CLASSES_ROOT ###
  
Root keys.  The values for these keys correspond to the values from  
WinReg.h in the MS Platform SDK.  The ROOT_KEY_ prefix corresponds to the  
HKEY_ prefix in the MS Platform SDK.  
  
This interface is not restricted to using only these root keys.  
  

### ROOT_KEY_CURRENT_USER ###

### ROOT_KEY_LOCAL_MACHINE ###

### ACCESS_BASIC ###
  
Values for the mode parameter passed to the open and create methods.  
The values defined here correspond to the REGSAM values defined in  
WinNT.h in the MS Platform SDK, where ACCESS_ is replaced with KEY_.  
  
This interface is not restricted to using only these access types.  
  

### ACCESS_QUERY_VALUE ###

### ACCESS_SET_VALUE ###

### ACCESS_CREATE_SUB_KEY ###

### ACCESS_ENUMERATE_SUB_KEYS ###

### ACCESS_NOTIFY ###

### ACCESS_READ ###

### ACCESS_WRITE ###

### ACCESS_ALL ###

### WOW64_32 ###

### WOW64_64 ###

### TYPE_NONE ###
  
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
  

### TYPE_STRING ###

### TYPE_BINARY ###

### TYPE_INT ###

### TYPE_INT64 ###
