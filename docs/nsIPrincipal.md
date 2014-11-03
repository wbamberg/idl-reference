---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/caps/nsIPrincipal.idl">Source file</a>
</div>

# nsIPrincipal #

## Methods ##

### equals(other) ###
  
Returns whether the other principal is equivalent to this principal.  
Principals are considered equal if they are the same principal, or  
they have the same origin.  
  

### equalsConsideringDomain(other) ###
  
Like equals, but takes document.domain changes into account.  
  

### subsumes(other) ###
  
Returns whether the other principal is equal to or weaker than this  
principal. Principals are equal if they are the same object or they  
have the same origin.  
  
Thus a principal always subsumes itself.  
  
The system principal subsumes itself and all other principals.  
  
A null principal (corresponding to an unknown, hence assumed minimally  
privileged, security context) is not equal to any other principal  
(including other null principals), and therefore does not subsume  
anything but itself.  
  

### subsumesConsideringDomain(other) ###
  
Same as the previous method, subsumes(), but takes document.domain into  
account.  
  

### checkMayLoad(uri, report, allowIfInheritsPrincipal) ###
  
Checks whether this principal is allowed to load the network resource  
located at the given URI under the same-origin policy. This means that  
codebase principals are only allowed to load resources from the same  
domain, the system principal is allowed to load anything, and null  
principals can only load URIs where they are the principal. This is  
changed by the optional flag allowIfInheritsPrincipal (which defaults to  
false) which allows URIs that inherit their loader's principal.  
  
If the load is allowed this function does nothing. If the load is not  
allowed the function throws NS_ERROR_DOM_BAD_URI.  
  
NOTE: Other policies might override this, such as the Access-Control  
      specification.  
NOTE: The 'domain' attribute has no effect on the behaviour of this  
      function.  
  
  
  

#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>The URI about to be loaded.  
</td>
</tr>

<tr>
<td>report</td>
<td>If true, will report a warning to the console service  
              if the load is not allowed.  
</td>
</tr>

<tr>
<td>allowIfInheritsPrincipal</td>
<td>If true, the load is allowed if the  
                                  loadee inherits the principal of the  
                                  loader.  
@throws NS_ERROR_DOM_BAD_URI if the load is not allowed.  
</td>
</tr>

</table>

## Attributes ##

### hashValue ###
  
Returns a hash value for the principal.  
  

### URI ###
  
The codebase URI to which this principal pertains.  This is  
generally the document URI.  
  

### domain ###
  
The domain URI to which this principal pertains.  
This is congruent with HTMLDocument.domain, and may be null.  
Setting this has no effect on the URI.  
  

### origin ###
  
The origin of this principal's codebase URI.  
An origin is defined as: scheme + host + port.  
  

### csp ###
  
A Content Security Policy associated with this principal.  
  

### jarPrefix ###
  
Returns the jar prefix of the principal.  
The jar prefix is a string that can be used to isolate data or  
permissions between different principals while taking into account  
parameters like the app id or the fact that the principal is embedded in  
a mozbrowser.  
Some principals will return an empty string.  
Some principals will assert if you try to access the jarPrefix.  
  
The jarPrefix is intended to be an opaque identifier. It is currently  
"human-readable" but no callers should assume it will stay as is and  
it might be crypto-hashed at some point.  
  

### baseDomain ###
  
The base domain of the codebase URI to which this principal pertains  
(generally the document URI), handling null principals and  
non-hierarchical schemes correctly.  
  

### appStatus ###
  
Gets the principal's app status, which indicates whether the principal  
corresponds to "app code", and if it does, how privileged that code is.  
This method returns one of the APP_STATUS constants above.  
  
Note that a principal may have  
  
  appId != nsIScriptSecurityManager::NO_APP_ID &&  
  appId != nsIScriptSecurityManager::UNKNOWN_APP_ID  
  
and still have appStatus == APP_STATUS_NOT_INSTALLED.  That's because  
appId identifies the app that contains this principal, but a window  
might be contained in an app and not be running code that the app has  
vouched for.  For example, the window might be inside an <iframe  
mozbrowser>, or the window's origin might not match the app's origin.  
  
If you're doing a check to determine "does this principal correspond to  
app code?", you must check appStatus; checking appId != NO_APP_ID is not  
sufficient.  
  

### appId ###
  
Gets the id of the app this principal is inside.  If this principal is  
not inside an app, returns nsIScriptSecurityManager::NO_APP_ID.  
  
Note that this principal does not necessarily have the permissions of  
the app identified by appId.  For example, this principal might  
correspond to an iframe whose origin differs from that of the app frame  
containing it.  In this case, the iframe will have the appId of its  
containing app frame, but the iframe must not run with the app's  
permissions.  
  
Similarly, this principal might correspond to an <iframe mozbrowser>  
inside an app frame; in this case, the content inside the iframe should  
not have any of the app's permissions, even if the iframe is at the same  
origin as the app.  
  
If you're doing a security check based on appId, you must check  
appStatus as well.  
  

### isInBrowserElement ###
  
Returns true iff the principal is inside a browser element.  (<iframe  
mozbrowser mozapp> does not count as a browser element.)  
  

### unknownAppId ###
  
Returns true if this principal has an unknown appId. This shouldn't  
generally be used. We only expose it due to not providing the correct  
appId everywhere where we construct principals.  
  

### isNullPrincipal ###
  
Returns true iff this principal is a null principal (corresponding to an  
unknown, hence assumed minimally privileged, security context).  
  

## Constants ##

### APP_STATUS_NOT_INSTALLED ###

### APP_STATUS_INSTALLED ###

### APP_STATUS_PRIVILEGED ###

### APP_STATUS_CERTIFIED ###
