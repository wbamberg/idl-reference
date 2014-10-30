---
layout: default
---

# nsIFeedResultService #
  
nsIFeedResultService provides a globally-accessible object for retrieving  
the results of feed processing.  
  

## Methods ##

### addToClientReader ###
  
Adds a URI to the user's specified external feed handler, or live   
bookmarks.   
@param   uri  
         The uri of the feed to add.  
@param   title  
         The title of the feed to add.  
@param   subtitle  
         The subtitle of the feed to add.  
@param   feedType  
         The nsIFeed type of the feed.  See nsIFeed.idl  
  

### addFeedResult ###
  
Registers a Feed Result object with a globally accessible service  
so that it can be accessed by a singleton method outside the usual  
flow of control in document loading.  
  
@param   feedResult  
         An object implementing nsIFeedResult representing the feed.  
  

### getFeedResult ###
  
Gets a Feed Handler object registered using addFeedResult.  
  
@param   uri  
         The URI of the feed a handler is being requested for  
  

### removeFeedResult ###
  
Unregisters a Feed Handler object registered using addFeedResult.  
@param   uri  
         The feed URI the handler was registered under. This must be  
         the same *instance* the feed was registered under.  
  

## Attributes ##

### forcePreviewPage ###
  
When set to true, forces the preview page to be displayed, regardless  
of the user's preferences.  
  
