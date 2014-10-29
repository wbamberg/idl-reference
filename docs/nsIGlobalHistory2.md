---
layout: default
---

# nsIGlobalHistory2 #

## Methods ##

### addURI ###

Add a URI to global history

@param aURI      the URI of the page
@param aRedirect whether the URI was redirected to another location;
                 this is 'true' for the original URI which is
                 redirected.
@param aToplevel whether the URI is loaded in a top-level window
@param aReferrer the URI of the referring page

@note  Docshell will not filter out URI schemes like chrome: data:
       about: and view-source:.  Embedders should consider filtering out
       these schemes and others, e.g. mailbox: for the main URI and the
       referrer.


### isVisited ###

Checks to see whether the given URI is in history.

@param aURI the uri to the page
@return true if a URI has been visited


### setPageTitle ###

Set the page title for the given uri. URIs that are not already in
global history will not be added.

@param aURI    the URI for which to set to the title
@param aTitle  the page title

