---
layout: default
---

# mozIStorageBaseStatement #

The base interface for both pure asynchronous storage statements 
(mozIStorageAsyncStatement) and 'classic' storage statements
(mozIStorageStatement) that can be used for both synchronous and asynchronous
purposes.


## finalize ##

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


## bindUTF8StringParameter ##

Bind the given value at the given numeric index.

@param aParamIndex
       0-based index, 0 corresponding to the first numbered argument or
       "?1".
@param aValue
       Argument value.
@param aValueSize
       Length of aValue in bytes.
@{


## bindStringParameter ##

## bindDoubleParameter ##

## bindInt32Parameter ##

## bindInt64Parameter ##

## bindNullParameter ##

## bindBlobParameter ##

## bindAdoptedBlobParameter ##

## bindParameters ##
@}*/

Binds the array of parameters to the statement.  When executeAsync is
called, all the parameters in aParameters are bound and then executed.

@param aParameters
       The array of parameters to bind to the statement upon execution.

@note This is only works on statements being used asynchronously.


## newBindingParamsArray ##

Creates a new mozIStorageBindingParamsArray that can be used to bind
multiple sets of data to a statement with bindParameters.

@return a mozIStorageBindingParamsArray that multiple sets of parameters
        can be bound to.

@note This is only useful for statements being used asynchronously.


## executeAsync ##

Execute a query asynchronously using any currently bound parameters.  This
statement can be reused immediately, and reset does not need to be called.

@note If you have any custom defined functions, they must be re-entrant
      since they can be called on multiple threads.

@param aCallback [optional]
       The callback object that will be notified of progress, errors, and
       completion.
@return an object that can be used to cancel the statements execution.


## MOZ_STORAGE_STATEMENT_INVALID ##

The statement is not usable, either because it failed to initialize or
was explicitly finalized.


## MOZ_STORAGE_STATEMENT_READY ##

The statement is usable.


## MOZ_STORAGE_STATEMENT_EXECUTING ##

Indicates that the statement is executing and the row getters may be used.

@note This is only relevant for mozIStorageStatement instances being used
      in a synchronous fashion.


## state ##

Find out whether the statement is usable (has not been finalized).


## escapeStringForLIKE ##

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

