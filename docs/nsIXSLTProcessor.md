---
layout: default
---

# nsIXSLTProcessor #

## Methods ##

### importStylesheet(style) ###
  
Import the stylesheet into this XSLTProcessor for transformations.  
  
@param style The root-node of a XSLT stylesheet. This can be either  
             a document node or an element node. If a document node  
             then the document can contain either a XSLT stylesheet  
             or a LRE stylesheet.  
             If the argument is an element node it must be the  
             xsl:stylesheet (or xsl:transform) element of an XSLT  
             stylesheet.  
  
@exception nsIXSLTException  
  

### transformToFragment(source, output) ###
  
Transforms the node source applying the stylesheet given by  
the importStylesheet() function. The owner document of the output node  
owns the returned document fragment.  
  
@param source The node to be transformed  
@param output This document is used to generate the output  
@return DocumentFragment The result of the transformation  
  
@exception nsIXSLTException  
  

### transformToDocument(source) ###
  
Transforms the node source applying the stylesheet given by the  
importStylesheet() function.  
  
@param source The node to be transformed  
@return Document The result of the transformation  
  
@exception nsIXSLTException  
  

### setParameter(namespaceURI, localName, value) ###
  
Sets a parameter to be used in subsequent transformations with this  
nsIXSLTProcessor. If the parameter doesn't exist in the stylesheet the  
parameter will be ignored.  
  
@param namespaceURI The namespaceURI of the XSLT parameter  
@param localName    The local name of the XSLT parameter  
@param value        The new value of the XSLT parameter  
  
@exception NS_ERROR_ILLEGAL_VALUE The datatype of value is  
                                  not supported  
  

### getParameter(namespaceURI, localName) ###
  
Gets a parameter if previously set by setParameter. Returns null  
otherwise.  
  
@param namespaceURI The namespaceURI of the XSLT parameter  
@param localName    The local name of the XSLT parameter  
@return nsIVariant  The value of the XSLT parameter  
  

### removeParameter(namespaceURI, localName) ###
  
Removes a parameter, if set. This will make the processor use the  
default-value for the parameter as specified in the stylesheet.  
  
@param namespaceURI The namespaceURI of the XSLT parameter  
@param localName    The local name of the XSLT parameter  
  

### clearParameters() ###
  
Removes all set parameters from this nsIXSLTProcessor. This will make  
the processor use the default-value for all parameters as specified in  
the stylesheet.  
  

### reset() ###
  
Remove all parameters and stylesheets from this nsIXSLTProcessor.  
  
