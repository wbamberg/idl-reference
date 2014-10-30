---
layout: default
---

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
  
@param aOldPat  Old pattern to be replaced, e.g. file:///a/b/  
@param aNewPat  New pattern to be replaced, e.g. http://mypage.aol.com/  
@param aMakeRel Rewrite links as relative vs. absolute  
  

## Attributes ##

### node ###
