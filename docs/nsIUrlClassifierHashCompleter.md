---
layout: default
---

# nsIUrlClassifierHashCompleter #
  
Clients updating the url-classifier database have the option of sending  
partial (32-bit) hashes of URL fragments to be blacklisted.  If the  
url-classifier encounters one of these truncated hashes, it will ask an  
nsIUrlClassifierCompleter instance to asynchronously provide the complete  
hash, along with some associated metadata.  
This is only ever used for testing and should absolutely be deleted (I  
think).  
  

## Methods ##

### complete(partialHash, gethashUrl, callback) ###
  
Request a completed hash from the given gethash url.  
  
@param partialHash  
       The 32-bit hash encountered by the url-classifier.  
@param gethashUrl  
       The gethash url to use.  
@param callback  
       An nsIUrlClassifierCompleterCallback instance.  
  
