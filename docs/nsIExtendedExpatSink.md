---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/parser/htmlparser/nsIExtendedExpatSink.idl">Source file</a>
</div>

# nsIExtendedExpatSink #
<code>  
This interface provides notification of syntax-level events.  
  
</code>
## Methods ##

### handleStartDTD(aDoctypeName, aSysid, aPubid) ###
<code>  
Called at the beginning of the DTD, before any entity or notation  
events.  
@param aDoctypeName The document type name.  
@param aSysid The declared system identifier for the external DTD subset,  
              or null if none was declared.  
@param aPubid The declared public identifier for the external DTD subset,  
              or null if none was declared.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDoctypeName</td>
<td>The document type name.  
</td>
</tr>

<tr>
<td>aSysid</td>
<td>The declared system identifier for the external DTD subset,  
              or null if none was declared.  
</td>
</tr>

<tr>
<td>aPubid</td>
<td>The declared public identifier for the external DTD subset,  
              or null if none was declared.  
</td>
</tr>

</table>

### handleStartNamespaceDecl(aPrefix, aUri) ###
<code>  
Called when a prefix mapping starts to be in-scope, before any  
startElement events.  
@param aPrefix The Namespace prefix being declared. An empty string  
               is used for the default element namespace, which has  
               no prefix.  
@param aUri The Namespace URI the prefix is mapped to.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aPrefix</td>
<td>The Namespace prefix being declared. An empty string  
               is used for the default element namespace, which has  
               no prefix.  
</td>
</tr>

<tr>
<td>aUri</td>
<td>The Namespace URI the prefix is mapped to.  
</td>
</tr>

</table>

### handleEndNamespaceDecl(aPrefix) ###
<code>  
Called when a prefix mapping is no longer in-scope, after any  
endElement events.  
@param aPrefix The prefix that was being mapped. This is the empty string  
               when a default mapping scope ends.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aPrefix</td>
<td>The prefix that was being mapped. This is the empty string  
               when a default mapping scope ends.  
</td>
</tr>

</table>

### handleNotationDecl(aNotationName, aSysid, aPubid) ###
<code>  
This is called for a declaration of notation.  The base argument is  
whatever was set by XML_SetBase. aNotationName will never be  
null. The other arguments can be.  
@param aNotationName The notation name.  
@param aSysId The notation's system identifier, or null if none was given.  
@param aPubId The notation's pubilc identifier, or null if none was given.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aNotationName</td>
<td>The notation name.  
</td>
</tr>

<tr>
<td>aSysId</td>
<td>The notation's system identifier, or null if none was given.  
</td>
</tr>

<tr>
<td>aPubId</td>
<td>The notation's pubilc identifier, or null if none was given.  
</td>
</tr>

</table>

### handleUnparsedEntityDecl(aName, aSysid, aPubid, aNotationName) ###
<code>  
This is called for a declaration of an unparsed (NDATA) entity.  
aName, aSysid and aNotationName arguments will never be  
null. The other arguments may be.  
@param aName  The unparsed entity's name.  
@param aSysId The notation's system identifier.  
@param aPubId The notation's pubilc identifier, or null if none was given.  
@param aNotationName The name of the associated notation.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>The unparsed entity's name.  
</td>
</tr>

<tr>
<td>aSysId</td>
<td>The notation's system identifier.  
</td>
</tr>

<tr>
<td>aPubId</td>
<td>The notation's pubilc identifier, or null if none was given.  
</td>
</tr>

<tr>
<td>aNotationName</td>
<td>The name of the associated notation.  
</td>
</tr>

</table>
