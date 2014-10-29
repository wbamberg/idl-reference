---
layout: default
---

# mozIStorageStatement #

A SQL statement that can be used for both synchronous and asynchronous
purposes.


## clone ##

Create a clone of this statement, by initializing a new statement
with the same connection and same SQL statement as this one.  It
does not preserve statement state; that is, if a statement is
being executed when it is cloned, the new statement will not be
executing.


## parameterCount ##

## getParameterName ##

Name of nth parameter, if given


## getParameterIndex ##

Returns the index of the named parameter.

@param aName
       The name of the parameter you want the index for.  This does not
       include the leading ':'.
@return the index of the named parameter.


## columnCount ##

Number of columns returned


## getColumnName ##

Name of nth column


## getColumnIndex ##

Obtains the index of the column with the specified name.

@param aName
       The name of the column.
@return The index of the column with the specified name.


## getColumnDecltype ##

Obtains the declared column type of a prepared statement.

@param aParamIndex
       The zero-based index of the column who's declared type we are
       interested in.
@return the declared index type.


## reset ##

Reset parameters/statement execution


## execute ##

Execute the query, ignoring any results.  This is accomplished by
calling executeStep() once, and then calling reset().

Error and last insert info, etc. are available from
the mozStorageConnection.


## executeStep ##

Execute a query, using any currently-bound parameters.  Reset
must be called on the statement after the last call of
executeStep.

@return a boolean indicating whether there are more rows or not;
        row data may be accessed using mozIStorageValueArray methods on
        the statement.


## VALUE_TYPE_NULL ##

Execute a query, using any currently-bound parameters.  Reset is called
when no more data is returned.  This method is only available to JavaScript
consumers.

@deprecated As of Mozilla 1.9.2 in favor of executeStep().

@return a boolean indicating whether there are more rows or not.

[deprecated] boolean step();


Obtains the current list of named parameters, which are settable.  This
property is only available to JavaScript consumers.

readonly attribute mozIStorageStatementParams params;


Obtains the current row, with access to all the data members by name.  This
property is only available to JavaScript consumers.

readonly attribute mozIStorageStatementRow row;


These type values are returned by getTypeOfIndex
to indicate what type of value is present at
a given column.


## VALUE_TYPE_INTEGER ##

## VALUE_TYPE_FLOAT ##

## VALUE_TYPE_TEXT ##

## VALUE_TYPE_BLOB ##

## numEntries ##

The number of entries in the array (each corresponding to a column in the
database row)


## getTypeOfIndex ##

Indicate the data type of the current result row for the the given column.
SQLite will perform type conversion if you ask for a value as a different
type than it is stored as.

@param aIndex
       0-based column index.
@return The type of the value at the given column index; one of
        VALUE_TYPE_NULL, VALUE_TYPE_INTEGER, VALUE_TYPE_FLOAT,
        VALUE_TYPE_TEXT, VALUE_TYPE_BLOB.


## getInt32 ##

Retrieve the contents of a column from the current result row as an
integer.

@param aIndex
       0-based colummn index.
@return Column value interpreted as an integer per type conversion rules.
@{


## getInt64 ##

## getDouble ##
 @} */

Retrieve the contents of a column from the current result row as a
floating point double.

@param aIndex
       0-based colummn index.
@return Column value interpreted as a double per type conversion rules.


## getUTF8String ##

Retrieve the contents of a column from the current result row as a
string.

@param aIndex
       0-based colummn index.
@return The value for the result column interpreted as a string.  If the
        stored value was NULL, you will get an empty string with IsVoid set
        to distinguish it from an explicitly set empty string.
@{


## getString ##

## getBlob ##
 @} */

Retrieve the contents of a column from the current result row as a
blob.

@param aIndex
       0-based colummn index.
@param[out] aDataSize
            The number of bytes in the blob.
@param[out] aData
            The contents of the BLOB.  This will be NULL if aDataSize == 0.


## getIsNull ##

Check whether the given column in the current result row is NULL.

@param aIndex
       0-based colummn index.
@return true if the value for the result column is null.


## getSharedUTF8String ##

Returns a shared string pointer


## getSharedString ##

## getSharedBlob ##
