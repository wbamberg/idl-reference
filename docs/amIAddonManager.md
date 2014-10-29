---
layout: default
---

# amIAddonManager #

A service to make some AddonManager functionality available to C++ callers.
Javascript callers should still use AddonManager.jsm directly.


## mapURIToAddonID ##

Synchronously map a URI to the corresponding Addon ID.

Mappable URIs are limited to in-application resources belonging to the
add-on, such as Javascript compartments, XUL windows, XBL bindings, etc.
but do not include URIs from meta data, such as the add-on homepage.

@param  aURI
        The nsIURI to map
@return
        true if the URI has been mapped successfully to an Addon ID

