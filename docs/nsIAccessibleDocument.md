---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleDocument.idl">Source file</a>
</div>

# nsIAccessibleDocument #
<pre>  
An interface for in-process accessibility clients  
that wish to retrieve information about a document.  
When accessibility is turned on in Gecko,  
there is an nsIAccessibleDocument for each document  
whether it is XUL, HTML or whatever.  
You can QueryInterface to nsIAccessibleDocument from the nsIAccessible for  
the root node of a document or you can get one from  
nsIAccessible::GetDocument().  
  
</pre>
## Methods ##

### getChildDocumentAt(index) ###
<pre>  
Return the child document accessible at the given index.  
  
</pre>
## Attributes ##

### URL ###
<pre>  
The URL of the document  
  
</pre>
### title ###
<pre>  
The title of the document, as specified in the document.  
  
</pre>
### mimeType ###
<pre>  
The mime type of the document  
  
</pre>
### docType ###
<pre>  
The doc type of the document, as specified in the document.  
  
</pre>
### DOMDocument ###
<pre>  
The nsIDOMDocument interface associated with this document.  
  
</pre>
### window ###
<pre>  
The nsIDOMWindow that the document resides in.  
  
</pre>
### parentDocument ###
<pre>  
Return the parent document accessible.  
  
</pre>
### childDocumentCount ###
<pre>  
Return the count of child document accessibles.  
  
</pre>
### virtualCursor ###
<pre>  
The virtual cursor pivot this document manages.  
  
</pre>