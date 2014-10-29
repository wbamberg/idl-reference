---
layout: default
---

# nsIPermission #

This interface defines a "permission" object,
used to specify allowed/blocked objects from
user-specified sites (cookies, images etc).


## Attributes ##

### host ###

The name of the host for which the permission is set


### appId ###

The id of the app for which the permission is set.


### isInBrowserElement ###

Whether the permission has been set to a page inside a browser element.


### type ###

a case-sensitive ASCII string, indicating the type of permission
(e.g., "cookie", "image", etc).
This string is specified by the consumer when adding a permission 
via nsIPermissionManager.
@see nsIPermissionManager


### capability ###

The permission (see nsIPermissionManager.idl for allowed values)


### expireType ###

The expiration type of the permission (session, time-based or none).
Constants are EXPIRE_*, defined in nsIPermissionManager.
@see nsIPermissionManager


### expireTime ###

The expiration time of the permission (milliseconds since Jan 1 1970
0:00:00).

