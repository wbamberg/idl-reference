---
layout: default
---

# nsIFeedResultService #
  
nsIFeedResultService provides a globally-accessible object for retrieving  
the results of feed processing.  
  

## Methods ##

### addToClientReader(uri, title, subtitle, feedType) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>uri  
         The uri of the feed to add.  
</td>
</tr>

<tr>
<td></td>
<td>title  
         The title of the feed to add.  
</td>
</tr>

<tr>
<td></td>
<td>subtitle  
         The subtitle of the feed to add.  
</td>
</tr>

<tr>
<td></td>
<td>feedType  
         The nsIFeed type of the feed.  See nsIFeed.idl  
</td>
</tr>

</table>

### addFeedResult(feedResult) ###
  
Registers a Feed Result object with a globally accessible service  
so that it can be accessed by a singleton method outside the usual  
flow of control in document loading.  
  
@param   feedResult  
         An object implementing nsIFeedResult representing the feed.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>feedResult  
         An object implementing nsIFeedResult representing the feed.  
</td>
</tr>

</table>

### getFeedResult(uri) ###
  
Gets a Feed Handler object registered using addFeedResult.  
  
@param   uri  
         The URI of the feed a handler is being requested for  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>uri  
         The URI of the feed a handler is being requested for  
</td>
</tr>

</table>

### removeFeedResult(uri) ###
  
Unregisters a Feed Handler object registered using addFeedResult.  
@param   uri  
         The feed URI the handler was registered under. This must be  
         the same *instance* the feed was registered under.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>uri  
         The feed URI the handler was registered under. This must be  
         the same *instance* the feed was registered under.  
</td>
</tr>

</table>

## Attributes ##

### forcePreviewPage ###
  
When set to true, forces the preview page to be displayed, regardless  
of the user's preferences.  
  
