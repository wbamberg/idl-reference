---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIURIRefObject.idl">Source file</a>
</div>

# nsIURIRefObject #
<code> A class which can represent any node which points to an  
external URI, e.g. <a>, <img>, <script> etc,  
and has the capability to rewrite URLs to be  
relative or absolute.  
Used by the editor but not dependant on it.  
  
</code>
## Methods ##

### Reset() ###
<code>  
Go back to the beginning of the attribute list.  
  
</code>
### GetNextURI() ###
<code>  
Return the next rewritable URI.  
  
</code>
### RewriteAllURIs(aOldPat, aNewPat, aMakeRel) ###
<code>  
Go back to the beginning of the attribute list  
  
@param aOldPat  Old pattern to be replaced, e.g. file:///a/b/  
@param aNewPat  New pattern to be replaced, e.g. http://mypage.aol.com/  
@param aMakeRel Rewrite links as relative vs. absolute  
  
</code>
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
