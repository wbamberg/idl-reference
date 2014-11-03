---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsISupportsIterators.idl">Source file</a>
</div>

# nsIInputIterator #
<pre>  
...  
  
</pre>
## Methods ##

### getElement() ###
<pre>  
Retrieve (and |AddRef()|) the element this iterator currently points to.  
  
The result is undefined if this iterator currently points outside the  
useful range of the underlying container or sequence.  
  
@result a new reference to the element this iterator currently points to (if any)  
  
</pre>
### stepForward() ###
<pre>  
Advance this iterator to the next position in the underlying container or sequence.  
  
</pre>
### isEqualTo(anotherIterator) ###
<pre>  
Test if |anotherIterator| points to the same position in the underlying container or sequence.  
  
The result is undefined if |anotherIterator| was not created by or for the same underlying container or sequence.  
  
@param anotherIterator another iterator to compare against, created by or for the same underlying container or sequence  
@result true if |anotherIterator| points to the same position in the underlying container or sequence  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>anotherIterator</td>
<td>another iterator to compare against, created by or for the same underlying container or sequence  
@result true if |anotherIterator| points to the same position in the underlying container or sequence  
</td>
</tr>

</table>

### clone() ###
<pre>  
Create a new iterator pointing to the same position in the underlying container or sequence to which this iterator currently points.  
The returned iterator is suitable for use in a subsequent call to |isEqualTo()| against this iterator.  
  
@result a new iterator pointing at the same position in the same underlying container or sequence as this iterator  
  
</pre>