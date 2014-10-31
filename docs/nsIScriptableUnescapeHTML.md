---
layout: default
---

# nsIScriptableUnescapeHTML #
  
This interface is OBSOLETE and exists solely for legacy extensions.  
  

## Methods ##

### unescape(src) ###
   
Converts HTML to plain text. This is equivalent to calling  
nsIParserUtils::convertToPlainText(src,   
  nsIDocumentEncoder::OutputSelectionOnly |  
  nsIDocumentEncoder::OutputAbsoluteLinks, 0).  
  
You should call nsIParserUtils::convertToPlainText() instead of calling   
this method.  
  
@param src The HTML string to convert to plain text.  
  

#### Parameters ####

<table>

<tr>
<td>src</td>
<td>The HTML string to convert to plain text.  
</td>
</tr>

</table>

### parseFragment(fragment, isXML, baseURI, element) ###
  
Parses markup into a sanitized document fragment. This is equivalent to  
calling nsIParserUtils::parseFragment(fragment, 0, isXML, baseURI,  
element).  
  
You should call nsIParserUtils::parseFragment() instead of calling this   
method.  
@param fragment the input markup  
@param isXML true if |fragment| is XML and false if HTML  
@param baseURI the base URL for this fragment  
@param element the context node for the fragment parsing algorithm  
  

#### Parameters ####

<table>

<tr>
<td>fragment</td>
<td>the input markup  
</td>
</tr>

<tr>
<td>fragment</td>
<td>the input markup  
</td>
</tr>

<tr>
<td>fragment</td>
<td>the input markup  
</td>
</tr>

<tr>
<td>fragment</td>
<td>the input markup  
</td>
</tr>

</table>
