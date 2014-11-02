---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/range/nsIDOMRange.idl">Source file</a>
</div>

# nsIDOMRange #
  
The nsIDOMRange interface is an interface to a DOM range object.  
  
For more information on this interface please see  
http://www.w3.org/TR/DOM-Level-2-Traversal-Range/  
  

## Methods ##

### setStart(refNode, offset) ###

### setEnd(refNode, offset) ###

### setStartBefore(refNode) ###

### setStartAfter(refNode) ###

### setEndBefore(refNode) ###

### setEndAfter(refNode) ###

### collapse(toStart) ###

### selectNode(refNode) ###

### selectNodeContents(refNode) ###

### compareBoundaryPoints(how, sourceRange) ###

### deleteContents() ###

### extractContents() ###

### cloneContents() ###

### insertNode(newNode) ###

### surroundContents(newParent) ###

### cloneRange() ###

### toString() ###

### detach() ###

### createContextualFragment(fragment) ###

### isPointInRange(parent, offset) ###

### comparePoint(parent, offset) ###

### intersectsNode(node) ###
  
Returns whether the range intersects node.  
  

### getClientRects() ###

### getBoundingClientRect() ###

## Attributes ##

### startContainer ###

### startOffset ###

### endContainer ###

### endOffset ###

### collapsed ###

### commonAncestorContainer ###

## Constants ##

### START_TO_START ###

### START_TO_END ###

### END_TO_END ###

### END_TO_START ###
