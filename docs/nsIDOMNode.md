---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/core/nsIDOMNode.idl">Source file</a>
</div>

# nsIDOMNode #
<pre>  
The nsIDOMNode interface is the primary datatype for the entire   
Document Object Model.  
It represents a single node in the document tree.  
  
For more information on this interface please see   
http://dvcs.w3.org/hg/domcore/raw-file/tip/Overview.html  
  
</pre>
## Methods ##

### insertBefore(newChild, refChild) ###

### replaceChild(newChild, oldChild) ###

### removeChild(oldChild) ###

### appendChild(newChild) ###

### hasChildNodes() ###

### cloneNode(deep) ###

### normalize() ###

### compareDocumentPosition(other) ###

### lookupPrefix(namespaceURI) ###

### isDefaultNamespace(namespaceURI) ###

### lookupNamespaceURI(prefix) ###

### isEqualNode(arg) ###

### setUserData(key, data) ###

### getUserData(key) ###

### contains(aOther) ###

## Attributes ##

### nodeName ###

### nodeValue ###

### nodeType ###

### parentNode ###

### parentElement ###

### childNodes ###

### firstChild ###

### lastChild ###

### previousSibling ###

### nextSibling ###

### ownerDocument ###

### namespaceURI ###

### prefix ###

### localName ###

### baseURI ###

### textContent ###

## Constants ##

### ELEMENT_NODE ###

### ATTRIBUTE_NODE ###

### TEXT_NODE ###

### CDATA_SECTION_NODE ###

### ENTITY_REFERENCE_NODE ###

### ENTITY_NODE ###

### PROCESSING_INSTRUCTION_NODE ###

### COMMENT_NODE ###

### DOCUMENT_NODE ###

### DOCUMENT_TYPE_NODE ###

### DOCUMENT_FRAGMENT_NODE ###

### NOTATION_NODE ###

### DOCUMENT_POSITION_DISCONNECTED ###

### DOCUMENT_POSITION_PRECEDING ###

### DOCUMENT_POSITION_FOLLOWING ###

### DOCUMENT_POSITION_CONTAINS ###

### DOCUMENT_POSITION_CONTAINED_BY ###

### DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC ###
