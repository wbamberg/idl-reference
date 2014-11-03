---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/autocomplete/nsIAutoCompleteSimpleResult.idl">Source file</a>
</div>

# nsIAutoCompleteSimpleResultListener #

## Methods ##

### onValueRemoved(aResult, aValue, aRemoveFromDb) ###
<pre>  
Dispatched after a value is removed from the result.  
@param aResult  
       The result from which aValue has been removed.  
@param aValue  
       The removed value.  
@param aRemoveFromDb  
       Whether the value should be removed from persistent storage as well.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aResult</td>
<td>       The result from which aValue has been removed.  
</td>
</tr>

<tr>
<td>aValue</td>
<td>       The removed value.  
</td>
</tr>

<tr>
<td>aRemoveFromDb</td>
<td>       Whether the value should be removed from persistent storage as well.  
</td>
</tr>

</table>
