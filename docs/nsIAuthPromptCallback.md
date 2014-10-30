---
layout: default
---

# nsIAuthPromptCallback #
  
Interface for callback methods for the asynchronous nsIAuthPrompt2 method.  
Callers MUST call exactly one method if nsIAuthPrompt2::promptPasswordAsync  
returns successfully. They MUST NOT call any method on this interface before  
promptPasswordAsync returns.  
  

## Methods ##

### onAuthAvailable ###
  
Authentication information is available.  
  
@param aContext  
       The context as passed to promptPasswordAsync  
@param aAuthInfo  
       Authentication information. Must be the same object that was passed  
       to promptPasswordAsync.  
  
@note  Any exceptions thrown from this method should be ignored.  
  

### onAuthCancelled ###
  
Notification that the prompt was cancelled.  
  
@param aContext  
       The context that was passed to promptPasswordAsync.  
@param userCancel  
       If false, this prompt was cancelled by calling the  
       the cancel method on the nsICancelable; otherwise,  
       it was cancelled by the user.  
  
