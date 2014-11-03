---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageStatement.idl">Source file</a>
</div>

# mozIStorageStatement #
<pre>  
A SQL statement that can be used for both synchronous and asynchronous  
purposes.  
  
</pre>
## Methods ##

### clone() ###
<pre>  
Create a clone of this statement, by initializing a new statement  
with the same connection and same SQL statement as this one.  It  
does not preserve statement state; that is, if a statement is  
being executed when it is cloned, the new statement will not be  
executing.  
  
</pre>
### getParameterName(aParamIndex) ###
<pre>  
Name of nth parameter, if given  
  
</pre>
### getParameterIndex(aName) ###
<pre>  
Returns the index of the named parameter.  
  
@param aName  
       The name of the parameter you want the index for.  This does not  
       include the leading ':'.  
@return the index of the named parameter.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>       The name of the parameter you want the index for.  This does not  
       include the leading ':'.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the index of the named parameter.  
</td>
</tr>

</table>

### getColumnName(aColumnIndex) ###
<pre>  
Name of nth column  
  
</pre>
### getColumnIndex(aName) ###
<pre>  
Obtains the index of the column with the specified name.  
  
@param aName  
       The name of the column.  
@return The index of the column with the specified name.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>       The name of the column.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The index of the column with the specified name.  
</td>
</tr>

</table>

### getColumnDecltype(aParamIndex) ###
<pre>  
Obtains the declared column type of a prepared statement.  
  
@param aParamIndex  
       The zero-based index of the column who's declared type we are  
       interested in.  
@return the declared index type.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aParamIndex</td>
<td>       The zero-based index of the column who's declared type we are  
       interested in.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the declared index type.  
</td>
</tr>

</table>

### reset() ###
<pre>  
Reset parameters/statement execution  
  
</pre>
### execute() ###
<pre>  
Execute the query, ignoring any results.  This is accomplished by  
calling executeStep() once, and then calling reset().  
  
Error and last insert info, etc. are available from  
the mozStorageConnection.  
  
</pre>
### executeStep() ###
<pre>  
Execute a query, using any currently-bound parameters.  Reset  
must be called on the statement after the last call of  
executeStep.  
  
@return a boolean indicating whether there are more rows or not;  
        row data may be accessed using mozIStorageValueArray methods on  
        the statement.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>a boolean indicating whether there are more rows or not;  
        row data may be accessed using mozIStorageValueArray methods on  
        the statement.  
</td>
</tr>

</table>

### getTypeOfIndex(aIndex) ###
<pre>  
Indicate the data type of the current result row for the the given column.  
SQLite will perform type conversion if you ask for a value as a different  
type than it is stored as.  
  
@param aIndex  
       0-based column index.  
@return The type of the value at the given column index; one of  
        VALUE_TYPE_NULL, VALUE_TYPE_INTEGER, VALUE_TYPE_FLOAT,  
        VALUE_TYPE_TEXT, VALUE_TYPE_BLOB.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>       0-based column index.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The type of the value at the given column index; one of  
        VALUE_TYPE_NULL, VALUE_TYPE_INTEGER, VALUE_TYPE_FLOAT,  
        VALUE_TYPE_TEXT, VALUE_TYPE_BLOB.  
</td>
</tr>

</table>

### getInt32(aIndex) ###
<pre>  
Retrieve the contents of a column from the current result row as an  
integer.  
  
@param aIndex  
       0-based colummn index.  
@return Column value interpreted as an integer per type conversion rules.  
@{  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>       0-based colummn index.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Column value interpreted as an integer per type conversion rules.  
@{  
</td>
</tr>

</table>

### getInt64(aIndex) ###

### getDouble(aIndex) ###
<pre> @} */  
</pre><pre>  
Retrieve the contents of a column from the current result row as a  
floating point double.  
  
@param aIndex  
       0-based colummn index.  
@return Column value interpreted as a double per type conversion rules.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>       0-based colummn index.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Column value interpreted as a double per type conversion rules.  
</td>
</tr>

</table>

### getUTF8String(aIndex) ###
<pre>  
Retrieve the contents of a column from the current result row as a  
string.  
  
@param aIndex  
       0-based colummn index.  
@return The value for the result column interpreted as a string.  If the  
        stored value was NULL, you will get an empty string with IsVoid set  
        to distinguish it from an explicitly set empty string.  
@{  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>       0-based colummn index.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The value for the result column interpreted as a string.  If the  
        stored value was NULL, you will get an empty string with IsVoid set  
        to distinguish it from an explicitly set empty string.  
@{  
</td>
</tr>

</table>

### getString(aIndex) ###

### getBlob(aIndex, aDataSize, aData) ###
<pre> @} */  
</pre><pre>  
Retrieve the contents of a column from the current result row as a  
blob.  
  
@param aIndex  
       0-based colummn index.  
@param[out] aDataSize  
            The number of bytes in the blob.  
@param[out] aData  
            The contents of the BLOB.  This will be NULL if aDataSize == 0.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>       0-based colummn index.  
</td>
</tr>

<tr>
<td>[out]</td>
<td>aDataSize  
            The number of bytes in the blob.  
</td>
</tr>

<tr>
<td>[out]</td>
<td>aData  
            The contents of the BLOB.  This will be NULL if aDataSize == 0.  
</td>
</tr>

</table>

### getIsNull(aIndex) ###
<pre>  
Check whether the given column in the current result row is NULL.  
  
@param aIndex  
       0-based colummn index.  
@return true if the value for the result column is null.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>       0-based colummn index.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the value for the result column is null.  
</td>
</tr>

</table>

### getSharedUTF8String(aIndex, aLength, aResult) ###
<pre>  
Returns a shared string pointer  
  
</pre>
### getSharedString(aIndex, aLength, aResult) ###

### getSharedBlob(aIndex, aLength, aResult) ###

## Attributes ##

### parameterCount ###

### columnCount ###
<pre>  
Number of columns returned  
  
</pre>
### numEntries ###
<pre>  
The number of entries in the array (each corresponding to a column in the  
database row)  
  
</pre>
## Constants ##

### VALUE_TYPE_NULL ###
<pre>  
Execute a query, using any currently-bound parameters.  Reset is called  
when no more data is returned.  This method is only available to JavaScript  
consumers.  
  
@deprecated As of Mozilla 1.9.2 in favor of executeStep().  
  
@return a boolean indicating whether there are more rows or not.  
  
[deprecated] boolean step();  
  
</pre><pre>  
Obtains the current list of named parameters, which are settable.  This  
property is only available to JavaScript consumers.  
  
readonly attribute mozIStorageStatementParams params;  
  
</pre><pre>  
Obtains the current row, with access to all the data members by name.  This  
property is only available to JavaScript consumers.  
  
readonly attribute mozIStorageStatementRow row;  
  
</pre><pre>  
These type values are returned by getTypeOfIndex  
to indicate what type of value is present at  
a given column.  
  
</pre>
### VALUE_TYPE_INTEGER ###

### VALUE_TYPE_FLOAT ###

### VALUE_TYPE_TEXT ###

### VALUE_TYPE_BLOB ###
