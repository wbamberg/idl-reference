---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageValueArray.idl">Source file</a>
</div>

# mozIStorageValueArray #
<code>  
mozIStorageValueArray wraps an array of SQL values, such as a single database  
row.  
  
</code>
## Methods ##

### getTypeOfIndex(aIndex) ###
<code>  
Returns the type of the value at the given column index;  
one of VALUE_TYPE_NULL, VALUE_TYPE_INTEGER, VALUE_TYPE_FLOAT,  
VALUE_TYPE_TEXT, VALUE_TYPE_BLOB.  
  
</code>
### getInt32(aIndex) ###
<code>  
Obtain a value for the given entry (column) index.  
Due to SQLite's type conversion rules, any of these are valid  
for any column regardless of the column's data type.  However,  
if the specific type matters, getTypeOfIndex should be used  
first to identify the column type, and then the appropriate  
get method should be called.  
  
If you ask for a string value for a NULL column, you will get an empty  
string with IsVoid set to distinguish it from an explicitly set empty  
string.  
  
</code>
### getInt64(aIndex) ###

### getDouble(aIndex) ###

### getUTF8String(aIndex) ###

### getString(aIndex) ###

### getBlob(aIndex, aDataSize, aData) ###

### getIsNull(aIndex) ###

### getSharedUTF8String(aIndex, aLength, aResult) ###
<code>  
Returns a shared string pointer  
  
</code>
### getSharedString(aIndex, aLength, aResult) ###

### getSharedBlob(aIndex, aLength, aResult) ###

## Attributes ##

### numEntries ###
  
numEntries  
  
number of entries in the array (each corresponding to a column  
in the database row)  
  

## Constants ##

### VALUE_TYPE_NULL ###
  
These type values are returned by getTypeOfIndex  
to indicate what type of value is present at  
a given column.  
  

### VALUE_TYPE_INTEGER ###

### VALUE_TYPE_FLOAT ###

### VALUE_TYPE_TEXT ###

### VALUE_TYPE_BLOB ###
