---
layout: default
---

# nsICookieManager #
 
An optional interface for accessing or removing the cookies
that are in the cookie list


## removeAll ##

Called to remove all cookies from the cookie list


## enumerator ##

Called to enumerate through each cookie in the cookie list.
The objects enumerated over are of type nsICookie


## remove ##

Called to remove an individual cookie from the cookie list, specified
by host, name, and path. If the cookie cannot be found, no exception
is thrown. Typically, the arguments to this method will be obtained
directly from the desired nsICookie object.

@param aHost The host or domain for which the cookie was set. @see
             nsICookieManager2::add for a description of acceptable host
             strings. If the target cookie is a domain cookie, a leading
             dot must be present.
@param aName The name specified in the cookie
@param aPath The path for which the cookie was set
@param aBlocked Indicates if cookies from this host should be permanently blocked


