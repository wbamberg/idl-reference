---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIContentPrefService2.idl">Source file</a>
</div>

# nsIContentPrefCallback2 #
<pre>  
The callback used by the above methods.  
  
</pre>
## Methods ##

### handleResult(pref) ###
<pre>  
For the retrieval methods, this is called once for each retrieved  
preference.  It is not called for other methods.  
  
@param pref  The retrieved preference.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>pref</td>
<td>The retrieved preference.  
</td>
</tr>

</table>

### handleError(error) ###
<pre>  
Called when an error occurs.  This may be called multiple times before  
handleCompletion is called.  
  
@param error  A number in Components.results describing the error.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>error</td>
<td>A number in Components.results describing the error.  
</td>
</tr>

</table>

### handleCompletion(reason) ###
<pre>  
Called when the method finishes.  This will be called exactly once for  
each method invocation, and afterward no other callback methods will be  
called.  
  
@param reason  One of the COMPLETE_* values indicating the manner in which  
               the method completed.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>reason</td>
<td>One of the COMPLETE_* values indicating the manner in which  
               the method completed.  
</td>
</tr>

</table>

## Constants ##

### COMPLETE_OK ###

### COMPLETE_ERROR ###
