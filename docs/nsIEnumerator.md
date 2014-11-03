---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIEnumerator.idl">Source file</a>
</div>

# nsIEnumerator #

## Methods ##

### first() ###
<code> First will reset the list. will return NS_FAILED if no items  
  
</code>
### next() ###
<code> Next will advance the list. will return failed if already at end  
  
</code>
### currentItem() ###
<code> CurrentItem will return the CurrentItem item it will fail if the   
 list is empty  
  
</code>
### isDone() ###
<code> return if the collection is at the end.  that is the beginning following   
 a call to Prev and it is the end of the list following a call to next  
  
</code>