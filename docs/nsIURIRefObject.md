---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIURIRefObject.idl">Source file</a>
</div>

# nsIURIRefObject #
 A class which can represent any node which points to an  
external URI, e.g. <a>, <img>, <script> etc,  
and has the capability to rewrite URLs to be  
relative or absolute.  
Used by the editor but not dependant on it.  
  

## Methods ##

### Reset() ###
  
Go back to the beginning of the attribute list.  
  

### GetNextURI() ###
  
Return the next rewritable URI.  
  

### RewriteAllURIs(aOldPat, aNewPat, aMakeRel) ###
  
Go back to the beginning of the attribute list  
  
  

#### Parameters ####

<table>

<tr>
<td>aOldPat</td>
<td>Old pattern to be replaced, e.g. file:///a/b/  
</td>
</tr>

<tr>
<td>aNewPat</td>
<td>New pattern to be replaced, e.g. http://mypage.aol.com/  
</td>
</tr>

<tr>
<td>aMakeRel</td>
<td>Rewrite links as relative vs. absolute  
</td>
</tr>

</table>

## Attributes ##

### node ###
