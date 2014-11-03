---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/url-classifier/nsIUrlClassifierDBService.idl">Source file</a>
</div>

# nsIUrlClassifierLookupCallback #
<pre>  
This is an internal helper interface for communication between the  
main thread and the dbservice worker thread.  It is called for each  
lookup to provide a set of possible results, which the main thread  
may need to expand using an nsIUrlClassifierCompleter.  
  
</pre>
## Methods ##

### lookupComplete(results) ###
<pre>  
The lookup process is complete.  
  
@param results  
       If this parameter is null, there were no results found.  
       If not, it contains an array of nsUrlClassifierEntry objects  
       with possible matches.  The callee is responsible for freeing  
       this array.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>results</td>
<td>       If this parameter is null, there were no results found.  
       If not, it contains an array of nsUrlClassifierEntry objects  
       with possible matches.  The callee is responsible for freeing  
       this array.  
</td>
</tr>

</table>
