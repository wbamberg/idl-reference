---
layout: default
---

# nsIForwardIterator #
  
...  
  

## Methods ##

### getElement ###
  
Retrieve (and |AddRef()|) the element this iterator currently points to.  
  
The result is undefined if this iterator currently points outside the  
useful range of the underlying container or sequence.  
  
@result a new reference to the element this iterator currently points to (if any)  
  

### putElement ###
  
Put |anElementToPut| into the underlying container or sequence at the position currently pointed to by this iterator.  
The iterator and the underlying container or sequence cooperate to |Release()|  
the replaced element, if any and if necessary, and to |AddRef()| the new element.  
  
The result is undefined if this iterator currently points outside the  
useful range of the underlying container or sequence.  
  
@param anElementToPut the element to place into the underlying container or sequence  
  

### stepForward ###
  
Advance this iterator to the next position in the underlying container or sequence.  
  

### isEqualTo ###
  
Test if |anotherIterator| points to the same position in the underlying container or sequence.  
  
The result is undefined if |anotherIterator| was not created by or for the same underlying container or sequence.  
  
@param anotherIterator another iterator to compare against, created by or for the same underlying container or sequence  
@result true if |anotherIterator| points to the same position in the underlying container or sequence  
  

### clone ###
  
Create a new iterator pointing to the same position in the underlying container or sequence to which this iterator currently points.  
The returned iterator is suitable for use in a subsequent call to |isEqualTo()| against this iterator.  
  
@result a new iterator pointing at the same position in the same underlying container or sequence as this iterator  
  
