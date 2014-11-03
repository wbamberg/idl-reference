---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xslt/nsIXSLTProcessor.idl">Source file</a>
</div>

# nsIXSLTProcessor #

## Methods ##

### importStylesheet(style) ###
<pre>  
Import the stylesheet into this XSLTProcessor for transformations.  
  
@param style The root-node of a XSLT stylesheet. This can be either  
             a document node or an element node. If a document node  
             then the document can contain either a XSLT stylesheet  
             or a LRE stylesheet.  
             If the argument is an element node it must be the  
             xsl:stylesheet (or xsl:transform) element of an XSLT  
             stylesheet.  
  
@exception nsIXSLTException  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>style</td>
<td>The root-node of a XSLT stylesheet. This can be either  
             a document node or an element node. If a document node  
             then the document can contain either a XSLT stylesheet  
             or a LRE stylesheet.  
             If the argument is an element node it must be the  
             xsl:stylesheet (or xsl:transform) element of an XSLT  
             stylesheet.  
</td>
</tr>

</table>

### transformToFragment(source, output) ###
<pre>  
Transforms the node source applying the stylesheet given by  
the importStylesheet() function. The owner document of the output node  
owns the returned document fragment.  
  
@param source The node to be transformed  
@param output This document is used to generate the output  
@return DocumentFragment The result of the transformation  
  
@exception nsIXSLTException  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>source</td>
<td>The node to be transformed  
</td>
</tr>

<tr>
<td>output</td>
<td>This document is used to generate the output  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>DocumentFragment The result of the transformation  
</td>
</tr>

</table>

### transformToDocument(source) ###
<pre>  
Transforms the node source applying the stylesheet given by the  
importStylesheet() function.  
  
@param source The node to be transformed  
@return Document The result of the transformation  
  
@exception nsIXSLTException  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>source</td>
<td>The node to be transformed  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Document The result of the transformation  
</td>
</tr>

</table>

### setParameter(namespaceURI, localName, value) ###
<pre>  
Sets a parameter to be used in subsequent transformations with this  
nsIXSLTProcessor. If the parameter doesn't exist in the stylesheet the  
parameter will be ignored.  
  
@param namespaceURI The namespaceURI of the XSLT parameter  
@param localName    The local name of the XSLT parameter  
@param value        The new value of the XSLT parameter  
  
@exception NS_ERROR_ILLEGAL_VALUE The datatype of value is  
                                  not supported  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>namespaceURI</td>
<td>The namespaceURI of the XSLT parameter  
</td>
</tr>

<tr>
<td>localName</td>
<td>The local name of the XSLT parameter  
</td>
</tr>

<tr>
<td>value</td>
<td>The new value of the XSLT parameter  
</td>
</tr>

</table>

### getParameter(namespaceURI, localName) ###
<pre>  
Gets a parameter if previously set by setParameter. Returns null  
otherwise.  
  
@param namespaceURI The namespaceURI of the XSLT parameter  
@param localName    The local name of the XSLT parameter  
@return nsIVariant  The value of the XSLT parameter  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>namespaceURI</td>
<td>The namespaceURI of the XSLT parameter  
</td>
</tr>

<tr>
<td>localName</td>
<td>The local name of the XSLT parameter  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>nsIVariant  The value of the XSLT parameter  
</td>
</tr>

</table>

### removeParameter(namespaceURI, localName) ###
<pre>  
Removes a parameter, if set. This will make the processor use the  
default-value for the parameter as specified in the stylesheet.  
  
@param namespaceURI The namespaceURI of the XSLT parameter  
@param localName    The local name of the XSLT parameter  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>namespaceURI</td>
<td>The namespaceURI of the XSLT parameter  
</td>
</tr>

<tr>
<td>localName</td>
<td>The local name of the XSLT parameter  
</td>
</tr>

</table>

### clearParameters() ###
<pre>  
Removes all set parameters from this nsIXSLTProcessor. This will make  
the processor use the default-value for all parameters as specified in  
the stylesheet.  
  
</pre>
### reset() ###
<pre>  
Remove all parameters and stylesheets from this nsIXSLTProcessor.  
  
</pre>