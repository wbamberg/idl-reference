---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsISimpleEnumerator.idl">Source file</a>
</div>

# nsISimpleEnumerator #
  
Used to enumerate over elements defined by its implementor.  
Although hasMoreElements() can be called independently of getNext(),  
getNext() must be pre-ceeded by a call to hasMoreElements(). There is  
no way to "reset" an enumerator, once you obtain one.  
  
@version 1.0  
  

## Methods ##

### hasMoreElements() ###
  
Called to determine whether or not the enumerator has  
any elements that can be returned via getNext(). This method  
is generally used to determine whether or not to initiate or  
continue iteration over the enumerator, though it can be  
called without subsequent getNext() calls. Does not affect  
internal state of enumerator.  
  
@see getNext()  
@return true if there are remaining elements in the enumerator.  
        false if there are no more elements in the enumerator.  
  

#### Returns ####

<table>

<tr>
<td>true if there are remaining elements in the enumerator.  
        false if there are no more elements in the enumerator.  
</td>
</tr>

</table>

### getNext() ###
  
Called to retrieve the next element in the enumerator. The "next"  
element is the first element upon the first call. Must be  
pre-ceeded by a call to hasMoreElements() which returns PR_TRUE.  
This method is generally called within a loop to iterate over  
the elements in the enumerator.  
  
@see hasMoreElements()  
@throws NS_ERROR_FAILURE if there are no more elements  
                         to enumerate.  
@return the next element in the enumeration.  
  

#### Returns ####

<table>

<tr>
<td>the next element in the enumeration.  
</td>
</tr>

</table>
