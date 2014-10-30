---
layout: default
---

# nsIFaviconService #

## Methods ##

### getFaviconLinkForIcon(aFaviconURI) ###
  
For a given icon URI, this will return a URI that will result in the image.  
In most cases, this is an annotation URI.  For chrome URIs, this will do  
nothing but returning the input URI.  
  
No validity checking is done. If you pass an icon URI that we've never  
seen, you'll get back a URI that references an invalid icon. The moz-anno  
protocol handler's special case for "favicon" annotations will resolve  
invalid icons to the default icon, although without caching.  
For invalid chrome URIs, you'll get a broken image.  
  
@param aFaviconURI  
       The URI of an icon in the favicon service.  
@return A URI that will give you the icon image.  This is NOT the URI of  
        the icon as set on the page, but a URI that will give you the  
        data out of the favicon service.  For a normal page with a  
        favicon we've stored, this will be an annotation URI which will  
        then cause the corresponding favicon data to be loaded async from  
        this service.  For pages where we don't have a favicon, this will  
        be a chrome URI of the default icon. For chrome URIs, the  
        output will be the same as the input.  
  

### expireAllFavicons() ###
  
Expire all known favicons from the database.  
  
@note This is an async method.  
      On successful completion a "places-favicons-expired" notification is  
      dispatched through observer's service.  
  

### addFailedFavicon(aFaviconURI) ###
  
Adds a given favicon's URI to the failed favicon cache.  
  
The lifespan of the favicon cache is up to the caching system.  This cache  
will also be written when setAndLoadFaviconForPage hits an error while  
fetching an icon.  
  
@param aFaviconURI  
       The URI of an icon in the favicon service.  
  

### removeFailedFavicon(aFaviconURI) ###
  
Removes the given favicon from the failed favicon cache.  If the icon is  
not in the cache, it will silently succeed.  
  
@param aFaviconURI  
       The URI of an icon in the favicon service.  
  

### isFailedFavicon(aFaviconURI) ###
  
Checks to see if a favicon is in the failed favicon cache.  
A positive return value means the icon is in the failed cache and you  
probably shouldn't try to load it.  A false return value means that it's  
worth trying to load it.  
This allows you to avoid trying to load "foo.com/favicon.ico" for every  
page on a site that doesn't have a favicon.  
  
@param aFaviconURI  
       The URI of an icon in the favicon service.  
  

## Attributes ##

### defaultFavicon ###
  
The default favicon URI  
  

## Constants ##

### FAVICON_LOAD_PRIVATE ###

### FAVICON_LOAD_NON_PRIVATE ###
