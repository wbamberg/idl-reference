---
layout: default
---

# mozIStorageBaseStatement #
  
The base interface for both pure asynchronous storage statements   
(mozIStorageAsyncStatement) and 'classic' storage statements  
(mozIStorageStatement) that can be used for both synchronous and asynchronous  
purposes.  
  

## Methods ##

### finalize() ###
  
Finalizes a statement so you can successfully close a database connection.  
Once a statement has been finalized it can no longer be used for any  
purpose.  
  
Statements are implicitly finalized when their reference counts hits zero.  
If you are a native (C++) caller this is accomplished by setting all of  
your nsCOMPtr instances to be NULL.  If you are operating from JavaScript  
code then you cannot rely on this behavior because of the involvement of  
garbage collection.  
  
When finalizing an asynchronous statement you do not need to worry about  
whether the statement has actually been executed by the asynchronous  
thread; you just need to call finalize after your last call to executeAsync  
involving the statement.  However, you do need to use asyncClose instead of  
close on the connection if any statements have been used asynchronously.  
  

### bindUTF8StringParameter(aParamIndex, aValue) ###
  
Bind the given value at the given numeric index.  
  
@param aParamIndex  
       0-based index, 0 corresponding to the first numbered argument or  
       "?1".  
@param aValue  
       Argument value.  
@param aValueSize  
       Length of aValue in bytes.  
@{  
  

#### Parameters ####

<table>

<tr>
<td>aParamIndex</td>
<td>       0-based index, 0 corresponding to the first numbered argument or  
       "?1".  
</td>
</tr>

<tr>
<td>aParamIndex</td>
<td>       0-based index, 0 corresponding to the first numbered argument or  
       "?1".  
</td>
</tr>

<tr>
<td>aParamIndex</td>
<td>       0-based index, 0 corresponding to the first numbered argument or  
       "?1".  
</td>
</tr>

</table>

### bindStringParameter(aParamIndex, aValue) ###

### bindDoubleParameter(aParamIndex, aValue) ###

### bindInt32Parameter(aParamIndex, aValue) ###

### bindInt64Parameter(aParamIndex, aValue) ###

### bindNullParameter(aParamIndex) ###

### bindBlobParameter(aParamIndex, aValue, aValueSize) ###

### bindAdoptedBlobParameter(aParamIndex, aValue, aValueSize) ###

### bindParameters(aParameters) ###
@}*/  
  
Binds the array of parameters to the statement.  When executeAsync is  
called, all the parameters in aParameters are bound and then executed.  
  
@param aParameters  
       The array of parameters to bind to the statement upon execution.  
  
@note This is only works on statements being used asynchronously.  
  

#### Parameters ####

<table>

<tr>
<td>aParameters</td>
<td>       The array of parameters to bind to the statement upon execution.  
</td>
</tr>

</table>

### newBindingParamsArray() ###
  
Creates a new mozIStorageBindingParamsArray that can be used to bind  
multiple sets of data to a statement with bindParameters.  
  
@return a mozIStorageBindingParamsArray that multiple sets of parameters  
        can be bound to.  
  
@note This is only useful for statements being used asynchronously.  
  

### executeAsync(aCallback) ###
  
Execute a query asynchronously using any currently bound parameters.  This  
statement can be reused immediately, and reset does not need to be called.  
  
@note If you have any custom defined functions, they must be re-entrant  
      since they can be called on multiple threads.  
  
@param aCallback [optional]  
       The callback object that will be notified of progress, errors, and  
       completion.  
@return an object that can be used to cancel the statements execution.  
  

#### Parameters ####

<table>

<tr>
<td>aCallback</td>
<td>[optional]  
       The callback object that will be notified of progress, errors, and  
       completion.  
</td>
</tr>

</table>

### escapeStringForLIKE(aValue, aEscapeChar) ###
  
Escape a string for SQL LIKE search.  
  
@note Consumers will have to use same escape char when doing statements  
      such as:   ...LIKE '?1' ESCAPE '/'...  
  
@param aValue  
       The string to escape for SQL LIKE.  
@param aEscapeChar  
       The escape character.  
@return an AString of an escaped version of aValue  
        (%, _ and the escape char are escaped with the escape char)  
        For example, we will convert "foo/bar_baz%20cheese"   
        into "foo//bar/_baz/%20cheese" (if the escape char is '/').  
  

#### Parameters ####

<table>

<tr>
<td>aValue</td>
<td>       The string to escape for SQL LIKE.  
</td>
</tr>

<tr>
<td>aValue</td>
<td>       The string to escape for SQL LIKE.  
</td>
</tr>

</table>

## Attributes ##

### state ###
  
Find out whether the statement is usable (has not been finalized).  
  

## Constants ##

### MOZ_STORAGE_STATEMENT_INVALID ###
  
The statement is not usable, either because it failed to initialize or  
was explicitly finalized.  
  

### MOZ_STORAGE_STATEMENT_READY ###
  
The statement is usable.  
  

### MOZ_STORAGE_STATEMENT_EXECUTING ###
  
Indicates that the statement is executing and the row getters may be used.  
  
@note This is only relevant for mozIStorageStatement instances being used  
      in a synchronous fashion.  
  
