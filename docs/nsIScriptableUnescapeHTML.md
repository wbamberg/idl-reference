---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/parser/html/nsIScriptableUnescapeHTML.idl">Source file</a>
</div>

# nsIScriptableUnescapeHTML #
<code>  
This interface is OBSOLETE and exists solely for legacy extensions.  
  
</code>
## Methods ##

### unescape(src) ###
<code>   
Converts HTML to plain text. This is equivalent to calling  
nsIParserUtils::convertToPlainText(src,   
  nsIDocumentEncoder::OutputSelectionOnly |  
  nsIDocumentEncoder::OutputAbsoluteLinks, 0).  
  
You should call nsIParserUtils::convertToPlainText() instead of calling   
this method.  
  
@param src The HTML string to convert to plain text.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>src</td>
<td>The HTML string to convert to plain text.  
</td>
</tr>

</table>

### parseFragment(fragment, isXML, baseURI, element) ###
<code>  
Parses markup into a sanitized document fragment. This is equivalent to  
calling nsIParserUtils::parseFragment(fragment, 0, isXML, baseURI,  
element).  
  
You should call nsIParserUtils::parseFragment() instead of calling this   
method.  
@param fragment the input markup  
@param isXML true if |fragment| is XML and false if HTML  
@param baseURI the base URL for this fragment  
@param element the context node for the fragment parsing algorithm  
  
</code>
#### Parameters ####

<table>

<tr>
<td>fragment</td>
<td>the input markup  
</td>
</tr>

<tr>
<td>isXML</td>
<td>true if |fragment| is XML and false if HTML  
</td>
</tr>

<tr>
<td>baseURI</td>
<td>the base URL for this fragment  
</td>
</tr>

<tr>
<td>element</td>
<td>the context node for the fragment parsing algorithm  
</td>
</tr>

</table>
