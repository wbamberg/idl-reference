---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/core/nsIDOMDOMImplementation.idl">Source file</a>
</div>

# nsIDOMDOMImplementation #
<pre>  
The nsIDOMDOMImplementation interface provides a number of methods for   
performing operations that are independent of any particular instance   
of the document object model.  
  
For more information on this interface please see   
http://www.w3.org/TR/DOM-Level-2-Core/  
  
</pre>
## Methods ##

### hasFeature(feature, version) ###

### createDocumentType(qualifiedName, publicId, systemId) ###

### createDocument(namespaceURI, qualifiedName, doctype) ###

### createHTMLDocument(title) ###
<pre>  
Returns an HTML document with a basic DOM already constructed and with an  
appropriate title element.  
  
@param title the title of the Document  
@see <http://www.whatwg.org/html/#creating-documents>  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>title</td>
<td>the title of the Document  
@see <http://www.whatwg.org/html/#creating-documents>  
</td>
</tr>

</table>
