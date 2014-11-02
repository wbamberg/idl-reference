---
layout: default
---

# mozIStorageFunction #
  
mozIStorageFunction is to be implemented by storage consumers that  
wish to receive callbacks during the request execution.  
  
SQL can apply functions to values from tables. Examples of  
such functions are MIN(a1,a2) or SQRT(num). Many functions are  
implemented in SQL engine.  
  
This interface allows consumers to implement their own,  
problem-specific functions.  
These functions can be called from triggers, too.  
  
  

## Methods ##

### onFunctionCall(aFunctionArguments) ###
  
onFunctionCall is called when execution of a custom  
function should occur.  
  
@param aNumArguments         The number of arguments  
@param aFunctionArguments    The arguments passed in to the function  
  
@returns any value as Variant type.  
  

#### Parameters ####

<table>

<tr>
<td>aNumArguments</td>
<td>The number of arguments  
</td>
</tr>

<tr>
<td>aFunctionArguments</td>
<td>The arguments passed in to the function  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>any value as Variant type.  
</td>
</tr>

</table>
