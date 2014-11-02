---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleDocument.idl">Source file</a>
</div>

# nsIAccessibleDocument #
  
An interface for in-process accessibility clients  
that wish to retrieve information about a document.  
When accessibility is turned on in Gecko,  
there is an nsIAccessibleDocument for each document  
whether it is XUL, HTML or whatever.  
You can QueryInterface to nsIAccessibleDocument from the nsIAccessible for  
the root node of a document or you can get one from  
nsIAccessible::GetDocument().  
  

## Methods ##

### getChildDocumentAt(index) ###
  
Return the child document accessible at the given index.  
  

## Attributes ##

### URL ###
  
The URL of the document  
  

### title ###
  
The title of the document, as specified in the document.  
  

### mimeType ###
  
The mime type of the document  
  

### docType ###
  
The doc type of the document, as specified in the document.  
  

### DOMDocument ###
  
The nsIDOMDocument interface associated with this document.  
  

### window ###
  
The nsIDOMWindow that the document resides in.  
  

### parentDocument ###
  
Return the parent document accessible.  
  

### childDocumentCount ###
  
Return the count of child document accessibles.  
  

### virtualCursor ###
  
The virtual cursor pivot this document manages.  
  
