---
layout: default
---

# nsIFeedResultListener #

nsIFeedResultListener defines a callback used when feed processing
completes.


## handleResult ##
 
Always called, even after an error. There could be new feed-level
data available at this point, if it followed or was interspersed
with the items. Fire-and-Forget implementations only need this.

@param result
       An object implementing nsIFeedResult representing the feed 
       and its metadata. 

