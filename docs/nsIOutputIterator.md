---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsISupportsIterators.idl">Source file</a>
</div>

# nsIOutputIterator #
  
...  
  

## Methods ##

### putElement(anElementToPut) ###
  
Put |anElementToPut| into the underlying container or sequence at the position currently pointed to by this iterator.  
The iterator and the underlying container or sequence cooperate to |Release()|  
the replaced element, if any and if necessary, and to |AddRef()| the new element.  
  
The result is undefined if this iterator currently points outside the  
useful range of the underlying container or sequence.  
  
  

#### Parameters ####

<table>

<tr>
<td>anElementToPut</td>
<td>the element to place into the underlying container or sequence  
</td>
</tr>

</table>

### stepForward() ###
  
Advance this iterator to the next position in the underlying container or sequence.  
  
