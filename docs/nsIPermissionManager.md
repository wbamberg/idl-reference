---
layout: default
---

# nsIPermissionManager #

## Methods ##

### add(uri, type, permission, expireType, expireTime) ###
  
Add permission information for a given URI and permission type. This  
operation will cause the type string to be registered if it does not  
currently exist. If a permission already exists for a given type, it  
will be modified.  
  
@param uri         the uri to add the permission for  
@param type        a case-sensitive ASCII string, identifying the consumer.  
                   Consumers should choose this string to be unique, with  
                   respect to other consumers.  
@param permission  an integer representing the desired action (e.g. allow  
                   or deny). The interpretation of this number is up to the  
                   consumer, and may represent different actions for different  
                   types. Consumers may use one of the enumerated permission  
                   actions defined above, for convenience.  
                   NOTE: UNKNOWN_ACTION (0) is reserved to represent the  
                   default permission when no entry is found for a host, and  
                   should not be used by consumers to indicate otherwise.  
@param expiretype  a constant defining whether this permission should  
                   never expire (EXPIRE_NEVER), expire at the end of the  
                   session (EXPIRE_SESSION), or expire at a specified time  
                   (EXPIRE_TIME).  
@param expiretime  an integer representation of when this permission  
                   should be forgotten (milliseconds since Jan 1 1970 0:00:00).   
  

### addFromPrincipal(principal, typed, permission, expireType, expireTime) ###
  
Add permission information for a given principal.  
It is internally calling the other add() method using the nsIURI from the  
principal.  
Passing a system principal will be a no-op because they will always be  
granted permissions.  
  

### remove(host, type) ###
  
Remove permission information for a given host string and permission type.  
The host string represents the exact entry in the permission list (such as  
obtained from the enumerator), not a URI which that permission might apply  
to.  
  
@param host   the host to remove the permission for  
@param type   a case-sensitive ASCII string, identifying the consumer.   
              The type must have been previously registered using the  
              add() method.  
  

### removeFromPrincipal(principal, type) ###
  
Remove permission information for a given principal.  
This is internally calling remove() with the host from the principal's URI.  
Passing system principal will be a no-op because we never add them to the  
database.  
  

### removeAll() ###
  
Clear permission information for all websites.  
  

### removeAllSince(since) ###
  
Clear all permission information added since the specified time.  
  

### testPermission(uri, type) ###
  
Test whether a website has permission to perform the given action.  
@param uri     the uri to be tested  
@param type    a case-sensitive ASCII string, identifying the consumer  
@param return  see add(), param permission. returns UNKNOWN_ACTION when  
               there is no stored permission for this uri and / or type.  
  

### testPermissionFromPrincipal(principal, type) ###
  
Test whether the principal has the permission to perform a given action.  
System principals will always have permissions granted.  
  

### testPermissionFromWindow(window, type) ###
  
Test whether the principal associated with the window's document has the  
permission to perform a given action.  System principals will always  
have permissions granted.  
  

### testExactPermission(uri, type) ###
  
Test whether a website has permission to perform the given action.  
This requires an exact hostname match, subdomains are not a match.  
@param uri     the uri to be tested  
@param type    a case-sensitive ASCII string, identifying the consumer  
@param return  see add(), param permission. returns UNKNOWN_ACTION when  
               there is no stored permission for this uri and / or type.  
  

### testExactPermissionFromPrincipal(principal, type) ###
  
See testExactPermission() above.  
System principals will always have permissions granted.  
  

### testExactPermanentPermission(principal, type) ###
  
Test whether a website has permission to perform the given action  
ignoring active sessions.  
System principals will always have permissions granted.  
  
@param principal the principal  
@param type      a case-sensitive ASCII string, identifying the consumer  
@param return    see add(), param permission. returns UNKNOWN_ACTION when  
                 there is no stored permission for this uri and / or type.  
  

### getPermissionObject(principal, type, exactHost) ###
  
Get the permission object associated with the given principal and action.  
@param principal The principal  
@param type      A case-sensitive ASCII string identifying the consumer  
@param exactHost If true, only the specific host will be matched,  
                 @see testExactPermission. If false, subdomains will  
                 also be searched, @see testPermission.  
@returns The matching permission object, or null if no matching object  
         was found. No matching object is equivalent to UNKNOWN_ACTION.  
@note Clients in general should prefer the test* methods unless they  
      need to know the specific stored details.  
@note This method will always return null for the system principal.  
  

### addrefAppId(appId) ###
  
Increment or decrement our "refcount" of an app id.  
  
We use this refcount to determine an app's lifetime.  When an app's  
refcount goes to 0, we clear the permissions given to the app which are  
set to expire at the end of its session.  
  

### releaseAppId(appId) ###

### removePermissionsForApp(appId, browserOnly) ###
  
Remove all permissions associated with a given app id.  
@param aAppId       The appId of the app  
@param aBrowserOnly Whether we should remove permissions associated with  
                    a browser element (true) or all permissions (false).  
  

### updateExpireTime(principal, type, exactHost, sessionExpireTime, persistentExpireTime) ###
  
If the current permission is set to expire, reset the expiration time. If  
there is no permission or the current permission does not expire, this  
method will silently return.  
  
@param sessionExpiretime  an integer representation of when this permission  
                          should be forgotten (milliseconds since  
                          Jan 1 1970 0:00:00), if it is currently  
                          EXPIRE_SESSION.  
@param sessionExpiretime  an integer representation of when this permission  
                          should be forgotten (milliseconds since  
                          Jan 1 1970 0:00:00), if it is currently  
                          EXPIRE_TIME.  
  

## Attributes ##

### enumerator ###
  
Allows enumeration of all stored permissions  
@return an nsISimpleEnumerator interface that allows access to  
        nsIPermission objects  
  

## Constants ##

### UNKNOWN_ACTION ###
  
Predefined return values for the testPermission method and for  
the permission param of the add method  
NOTE: UNKNOWN_ACTION (0) is reserved to represent the  
default permission when no entry is found for a host, and  
should not be used by consumers to indicate otherwise.  
  

### ALLOW_ACTION ###

### DENY_ACTION ###

### PROMPT_ACTION ###

### EXPIRE_NEVER ###
  
Predefined expiration types for permissions.  Permissions can be permanent  
(never expire), expire at the end of the session, or expire at a specified  
time. Permissions that expire at the end of a session may also have a  
specified expiration time.  
  

### EXPIRE_SESSION ###

### EXPIRE_TIME ###
