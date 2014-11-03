---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIDirectoryService.idl">Source file</a>
</div>

# nsIDirectoryServiceProvider2 #
<pre>  
nsIDirectoryServiceProvider2  
  
An extension of nsIDirectoryServiceProvider which allows  
multiple files to be returned for the given key.  
  
</pre>
## Methods ##

### getFiles(prop) ###
<pre>  
getFiles  
  
Directory Service calls this when it gets a request for  
a prop and the requested type is nsISimpleEnumerator.  
  
@param prop         The symbolic name of the file list.  
  
@return             An enumerator for a list of file locations.  
                    The elements in the enumeration are nsIFile  
@returnCode         NS_SUCCESS_AGGREGATE_RESULT if this result should be  
                    aggregated with other "lower" providers.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>prop</td>
<td>The symbolic name of the file list.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>ode         NS_SUCCESS_AGGREGATE_RESULT if this result should be  
                    aggregated with other "lower" providers.  
</td>
</tr>

</table>
