---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/base/nsIStyleSheetService.idl">Source file</a>
</div>

# nsIStyleSheetService #

## Methods ##

### loadAndRegisterSheet(sheetURI, type) ###
  
Synchronously loads a style sheet from |sheetURI| and adds it to the list  
of user or agent style sheets.  
  
A user sheet loaded via this API will come before userContent.css and  
userChrome.css in the cascade (so the rules in it will have lower  
precedence than rules in those sheets).  
  
An agent sheet loaded via this API will come after ua.css in the cascade  
(so the rules in it will have higher precedence than rules in ua.css).  
  
The relative ordering of two user or two agent sheets loaded via  
this API is undefined.  
  
Sheets added via this API take effect on all documents, including  
already-loaded ones, immediately.  
  

### sheetRegistered(sheetURI, type) ###
  
Returns true if a style sheet at |sheetURI| has previously been  
added to the list of style sheets specified by |type|.  
  

### preloadSheet(sheetURI, type) ###
  
Synchronously loads a style sheet from |sheetURI| and returns the  
new style sheet object. Can be used with nsIDOMWindowUtils.addSheet.  
  

### unregisterSheet(sheetURI, type) ###
  
Remove the style sheet at |sheetURI| from the list of style sheets  
specified by |type|.  The removal takes effect immediately, even for  
already-loaded documents.  
  

## Constants ##

### AGENT_SHEET ###

### USER_SHEET ###

### AUTHOR_SHEET ###
