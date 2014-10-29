---
layout: default
---

# nsIScriptSecurityManager #

## canCreateWrapper ##

For each of these hooks returning NS_OK means 'let the action continue'.
Returning an error code means 'veto the action'. XPConnect will return
false to the js engine if the action is vetoed. The implementor of this
interface is responsible for setting a JS exception into the JSContext
if that is appropriate.


## canCreateInstance ##

## canGetService ##

## checkLoadURIFromScript ##

Check that the script currently running in context "cx" can load "uri".

Will return error code NS_ERROR_DOM_BAD_URI if the load request
should be denied.

@param cx the JSContext of the script causing the load
@param uri the URI that is being loaded


## STANDARD ##

Default CheckLoadURI permissions


## LOAD_IS_AUTOMATIC_DOCUMENT_REPLACEMENT ##

## ALLOW_CHROME ##

## DISALLOW_INHERIT_PRINCIPAL ##

## DISALLOW_SCRIPT_OR_DATA ##

## DISALLOW_SCRIPT ##

## DONT_REPORT_ERRORS ##

## checkLoadURIWithPrincipal ##

Check that content with principal aPrincipal can load "uri".

Will return error code NS_ERROR_DOM_BAD_URI if the load request
should be denied.

@param aPrincipal the principal identifying the actor causing the load
@param uri the URI that is being loaded
@param flags the permission set, see above


## checkLoadURIStrWithPrincipal ##

Similar to checkLoadURIWithPrincipal but there are two differences:

1) The URI is a string, not a URI object.
2) This function assumes that the URI may still be subject to fixup (and
hence will check whether fixed-up versions of the URI are allowed to
load as well); if any of the versions of this URI is not allowed, this
function will return error code NS_ERROR_DOM_BAD_URI.


## scriptAllowed ##

Return true if scripts may be executed in the scope of the given global.


## getSystemPrincipal ##

Return the all-powerful system principal.


## getSimpleCodebasePrincipal ##

Return a principal that has the same origin as aURI.
This principals should not be used for any data/permission check, it will
have appId = UNKNOWN_APP_ID.


## getAppCodebasePrincipal ##

Returns a principal that has the given information.
@param appId is the app id of the principal. It can't be UNKNOWN_APP_ID.
@param inMozBrowser is true if the principal has to be considered as
inside a mozbrowser frame.


## getLoadContextCodebasePrincipal ##

Returns a principal that has the appId and inMozBrowser of the load
context.
@param loadContext to get appId/inMozBrowser from.


## getDocShellCodebasePrincipal ##

Returns a principal that has the appId and inMozBrowser of the docshell
inside a mozbrowser frame.
@param docShell to get appId/inMozBrowser from.


## getNoAppCodebasePrincipal ##

Returns a principal with that has the same origin as uri and is not part
of an appliction.
The returned principal will have appId = NO_APP_ID.


## getCodebasePrincipal ##

Legacy name for getNoAppCodebasePrincipal.

@deprecated use getNoAppCodebasePrincipal instead.


## checkSameOrigin ##

Returns OK if aJSContext and target have the same "origin"
(scheme, host, and port).


## checkSameOriginURI ##

Returns OK if aSourceURI and target have the same "origin"
(scheme, host, and port).
ReportError flag suppresses error reports for functions that
don't need reporting.


## getChannelResultPrincipal ##

Get the principal for the given channel.  This will typically be the
channel owner if there is one, and the codebase principal for the
channel's URI otherwise.  aChannel must not be null.


## getChannelURIPrincipal ##

Get the codebase principal for the channel's URI.
aChannel must not be null.


## isSystemPrincipal ##

Check whether a given principal is a system principal.  This allows us
to avoid handing back the system principal to script while allowing
script to check whether a given principal is system.


## NO_APP_ID ##

## UNKNOWN_APP_ID ##

## SAFEBROWSING_APP_ID ##

## getJarPrefix ##

Returns the jar prefix for the app.
appId can be NO_APP_ID or a valid app id. appId should not be
UNKNOWN_APP_ID.
inMozBrowser has to be true if the app is inside a mozbrowser iframe.


## activateDomainPolicy ##

Per-domain controls to enable and disable script. This system is designed
to be used by at most one consumer, and enforces this with its semantics.

Initially, domainPolicyActive is false. When activateDomainPolicy() is
invoked, domainPolicyActive becomes true, and subsequent calls to
activateDomainPolicy() will fail until deactivate() is invoked on the
nsIDomainPolicy returned from activateDomainPolicy(). At this point,
domainPolicyActive becomes false again, and a new consumer may acquire
control of the system by invoking activateDomainPolicy().


## domainPolicyActive ##

## policyAllowsScript ##

Query mechanism for the above policy.

If domainPolicyEnabled is false, this simply returns the current value
of javascript.enabled. Otherwise, it returns the same value, but taking
the various blacklist/whitelist exceptions into account.

