---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIAsyncFavicons.idl">Source file</a>
</div>

# mozIAsyncFavicons #

## Methods ##

### setAndFetchFaviconForPage(aPageURI, aFaviconURI, aForceReload, aFaviconLoadType, aCallback) ###
  
Declares that a given page uses a favicon with the given URI and   
attempts to fetch and save the icon data by loading the favicon URI  
through an async network request.  
  
If the icon data already exists, we won't try to reload the icon unless  
aForceReload is true.  Similarly, if the icon is in the failed favicon  
cache we won't do anything unless aForceReload is true, in which case  
we'll try to reload the favicon.  
  
This function will only save favicons for pages that are already stored in  
the database, like visited pages or bookmarks.  For any other URIs, it  
will succeed but do nothing.  This function will also ignore the error  
page favicon URI (see FAVICON_ERRORPAGE_URL below).  
  
Icons that fail to load will automatically be added to the failed favicon  
cache, and this function will not save favicons for non-bookmarked URIs  
when history is disabled.  
  
@note This function is identical to  
      nsIFaviconService::setAndLoadFaviconForPage.  
  
  
@see nsIFaviconDataCallback in nsIFaviconService.idl.  
  

#### Parameters ####

<table>

<tr>
<td>aPageURI</td>
<td>       URI of the page whose favicon is being set.  
</td>
</tr>

<tr>
<td>aFaviconURI</td>
<td>       URI of the favicon to associate with the page.  
</td>
</tr>

<tr>
<td>aForceReload</td>
<td>       If aForceReload is false, we try to reload the favicon only if we  
       don't have it or it has expired from the cache.  Setting  
       aForceReload to true causes us to reload the favicon even if we  
       have a usable copy.  
</td>
</tr>

<tr>
<td>aFaviconLoadType</td>
<td>       Set to FAVICON_LOAD_PRIVATE if the favicon is loaded from a private  
       browsing window.  Set to FAVICON_LOAD_NON_PRIVATE otherwise.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       Once we're done setting and/or fetching the favicon, we invoke this  
       callback.  
</td>
</tr>

</table>

### replaceFaviconData(aFaviconURI, aData, aDataLen, aMimeType, aExpiration) ###
  
Sets the data for a given favicon URI either by replacing existing data in  
the database or taking the place of otherwise fetched icon data when  
calling setAndFetchFaviconForPage later.  
  
Favicon data for favicon URIs that are not associated with a page URI via  
setAndFetchFaviconForPage will be stored in memory, but may be expired at  
any time, so you should make an effort to associate favicon URIs with page  
URIs as soon as possible.  
  
It's better to not use this function for chrome: icon URIs since you can  
reference the chrome image yourself. getFaviconLinkForIcon/Page will ignore  
any associated data if the favicon URI is "chrome:" and just return the  
same chrome URI.  
  
This function does NOT send out notifications that the data has changed.  
Pages using this favicons that are visible in history or bookmarks views  
will keep the old icon until they have been refreshed by other means.  
  
This function tries to optimize the favicon size, if it is bigger  
than a defined limit we will try to convert it to a 16x16 png image.  
If the conversion fails and favicon is still bigger than our max accepted  
size it won't be saved.  
  
  

#### Parameters ####

<table>

<tr>
<td>aFaviconURI</td>
<td>       URI of the favicon whose data is being set.  
</td>
</tr>

<tr>
<td>aData</td>
<td>       Binary contents of the favicon to save  
</td>
</tr>

<tr>
<td>aDataLength</td>
<td>       Length of binary data  
</td>
</tr>

<tr>
<td>aMimeType</td>
<td>       MIME type of the data to store.  This is important so that we know  
       what to report when the favicon is used.  You should always set this  
       param unless you are clearing an icon.  
</td>
</tr>

<tr>
<td>aExpiration</td>
<td>       Time in microseconds since the epoch when this favicon expires.  
       Until this time, we won't try to load it again.  
@throws NS_ERROR_FAILURE  
        Thrown if the favicon is overbloated and won't be saved to the db.  
</td>
</tr>

</table>

### replaceFaviconDataFromDataURL(aFaviconURI, aDataURL, aExpiration) ###
  
Same as replaceFaviconData but the data is provided by a string  
containing a data URL.  
  
@see replaceFaviconData  
  
  

#### Parameters ####

<table>

<tr>
<td>aFaviconURI</td>
<td>       URI of the favicon whose data is being set.  
</td>
</tr>

<tr>
<td>aDataURL</td>
<td>       string containing a data URL that represents the contents of  
       the favicon to save  
</td>
</tr>

<tr>
<td>aExpiration</td>
<td>       Time in microseconds since the epoch when this favicon expires.  
       Until this time, we won't try to load it again.  
@throws NS_ERROR_FAILURE  
        Thrown if the favicon is overbloated and won't be saved to the db.  
</td>
</tr>

</table>

### getFaviconURLForPage(aPageURI, aCallback) ###
  
Retrieves the favicon URI associated to the given page, if any.  
  
  
@note When the callback is invoked, aDataLen will be always 0, aData will  
      be an empty array, and aMimeType will be an empty string, regardless  
      of whether a favicon is associated with the page.  
  
@see nsIFaviconDataCallback in nsIFaviconService.idl.  
  

#### Parameters ####

<table>

<tr>
<td>aPageURI</td>
<td>       URI of the page whose favicon URI we're looking up.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       This callback is always invoked to notify the result of the lookup.  
       The aURI parameter will be the favicon URI, or null when no favicon  
       is associated with the page or an error occurred while fetching it.  
</td>
</tr>

</table>

### getFaviconDataForPage(aPageURI, aCallback) ###
  
Retrieves the favicon URI and data associated to the given page, if any.  
  
  
@see nsIFaviconDataCallback in nsIFaviconService.idl.  
  

#### Parameters ####

<table>

<tr>
<td>aPageURI</td>
<td>       URI of the page whose favicon URI and data we're looking up.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       This callback is always invoked to notify the result of the lookup.  The aURI  
       parameter will be the favicon URI, or null when no favicon is  
       associated with the page or an error occurred while fetching it.  If  
       aURI is not null, the other parameters may contain the favicon data.  
       However, if no favicon data is currently associated with the favicon  
       URI, aDataLen will be 0, aData will be an empty array, and aMimeType  
       will be an empty string.  
</td>
</tr>

</table>
