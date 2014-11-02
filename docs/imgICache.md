---
layout: default
---

# imgICache #
  
imgICache interface  
  
@author Stuart Parmenter <pavlov@netscape.com>  
@version 0.1  
@see imagelib2  
  

## Methods ##

### clearCache(chrome) ###
  
Evict images from the cache.  
  
@param chrome If TRUE,  evict only chrome images.  
              If FALSE, evict everything except chrome images.  
  

#### Parameters ####

<table>

<tr>
<td>chrome</td>
<td>If TRUE,  evict only chrome images.  
              If FALSE, evict everything except chrome images.  
</td>
</tr>

</table>

### removeEntry(uri) ###
  
Evict images from the cache.  
  
@param uri The URI to remove.  
@throws NS_ERROR_NOT_AVAILABLE if \a uri was unable to be removed from the cache.  
  

#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>The URI to remove.  
@throws NS_ERROR_NOT_AVAILABLE if \a uri was unable to be removed from the cache.  
</td>
</tr>

</table>

### findEntryProperties(uri) ###
  
Find Properties  
Used to get properties such as 'type' and 'content-disposition'  
'type' is a nsISupportsCString containing the images' mime type such as 'image/png'  
'content-disposition' will be a nsISupportsCString containing the header  
If you call this before any data has been loaded from a URI, it will succeed,  
but come back empty.  
  
Hopefully this will be removed with bug 805119  
  
@param uri The URI to look up.  
@returns NULL if the URL was not found in the cache  
  

#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>The URI to look up.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>NULL if the URL was not found in the cache  
</td>
</tr>

</table>

### respectPrivacyNotifications() ###
  
Make this cache instance respect private browsing notifications. This entails clearing  
the chrome and content caches whenever the last-pb-context-exited notification is  
observed.  
  
