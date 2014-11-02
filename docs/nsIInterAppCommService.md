---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/apps/nsIInterAppCommService.idl">Source file</a>
</div>
# nsIInterAppCommService #
  
Implemented by the contract id @mozilla.org/inter-app-communication-service;1  
  
This interface contains helpers for Inter-App Communication API [1] related  
purposes. A singleton service of this interface will be instantiated during  
the system boot-up, which plays the role of the central service receiving  
messages from and interacting with the content processes.  
  
[1] https://wiki.mozilla.org/WebAPI/Inter_App_Communication_Alt_proposal  
  

## Methods ##

### registerConnection(keyword, handlerPageURI, manifestURI, description, rules) ###
