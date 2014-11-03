---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/caps/nsIScriptSecurityManager.idl">Source file</a>
</div>

# nsIScriptSecurityManager #

## Methods ##

### canCreateWrapper(aJSContext, aIID, aObj, aClassInfo) ###
<pre>  
For each of these hooks returning NS_OK means 'let the action continue'.  
Returning an error code means 'veto the action'. XPConnect will return  
false to the js engine if the action is vetoed. The implementor of this  
interface is responsible for setting a JS exception into the JSContext  
if that is appropriate.  
  
</pre>
### canCreateInstance(aJSContext, aCID) ###

### canGetService(aJSContext, aCID) ###

### checkLoadURIFromScript(cx, uri) ###
<pre>  
Check that the script currently running in context "cx" can load "uri".  
  
Will return error code NS_ERROR_DOM_BAD_URI if the load request  
should be denied.  
  
@param cx the JSContext of the script causing the load  
@param uri the URI that is being loaded  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>cx</td>
<td>the JSContext of the script causing the load  
</td>
</tr>

<tr>
<td>uri</td>
<td>the URI that is being loaded  
</td>
</tr>

</table>

### checkLoadURIWithPrincipal(aPrincipal, uri, flags) ###
<pre>  
Check that content with principal aPrincipal can load "uri".  
  
Will return error code NS_ERROR_DOM_BAD_URI if the load request  
should be denied.  
  
@param aPrincipal the principal identifying the actor causing the load  
@param uri the URI that is being loaded  
@param flags the permission set, see above  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aPrincipal</td>
<td>the principal identifying the actor causing the load  
</td>
</tr>

<tr>
<td>uri</td>
<td>the URI that is being loaded  
</td>
</tr>

<tr>
<td>flags</td>
<td>the permission set, see above  
</td>
</tr>

</table>

### checkLoadURIStrWithPrincipal(aPrincipal, uri, flags) ###
<pre>  
Similar to checkLoadURIWithPrincipal but there are two differences:  
  
1) The URI is a string, not a URI object.  
2) This function assumes that the URI may still be subject to fixup (and  
hence will check whether fixed-up versions of the URI are allowed to  
load as well); if any of the versions of this URI is not allowed, this  
function will return error code NS_ERROR_DOM_BAD_URI.  
  
</pre>
### scriptAllowed(aGlobal) ###
<pre>  
Return true if scripts may be executed in the scope of the given global.  
  
</pre>
### getSystemPrincipal() ###
<pre>  
Return the all-powerful system principal.  
  
</pre>
### getSimpleCodebasePrincipal(aURI) ###
<pre>  
Return a principal that has the same origin as aURI.  
This principals should not be used for any data/permission check, it will  
have appId = UNKNOWN_APP_ID.  
  
</pre>
### getAppCodebasePrincipal(uri, appId, inMozBrowser) ###
<pre>  
Returns a principal that has the given information.  
@param appId is the app id of the principal. It can't be UNKNOWN_APP_ID.  
@param inMozBrowser is true if the principal has to be considered as  
inside a mozbrowser frame.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>appId</td>
<td>is the app id of the principal. It can't be UNKNOWN_APP_ID.  
</td>
</tr>

<tr>
<td>inMozBrowser</td>
<td>is true if the principal has to be considered as  
inside a mozbrowser frame.  
</td>
</tr>

</table>

### getLoadContextCodebasePrincipal(uri, loadContext) ###
<pre>  
Returns a principal that has the appId and inMozBrowser of the load  
context.  
@param loadContext to get appId/inMozBrowser from.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>loadContext</td>
<td>to get appId/inMozBrowser from.  
</td>
</tr>

</table>

### getDocShellCodebasePrincipal(uri, docShell) ###
<pre>  
Returns a principal that has the appId and inMozBrowser of the docshell  
inside a mozbrowser frame.  
@param docShell to get appId/inMozBrowser from.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>docShell</td>
<td>to get appId/inMozBrowser from.  
</td>
</tr>

</table>

### getNoAppCodebasePrincipal(uri) ###
<pre>  
Returns a principal with that has the same origin as uri and is not part  
of an appliction.  
The returned principal will have appId = NO_APP_ID.  
  
</pre>
### getCodebasePrincipal(uri) ###
<pre>  
Legacy name for getNoAppCodebasePrincipal.  
  
@deprecated use getNoAppCodebasePrincipal instead.  
  
</pre>
### checkSameOrigin(aJSContext, aTargetURI) ###
<pre>  
Returns OK if aJSContext and target have the same "origin"  
(scheme, host, and port).  
  
</pre>
### checkSameOriginURI(aSourceURI, aTargetURI, reportError) ###
<pre>  
Returns OK if aSourceURI and target have the same "origin"  
(scheme, host, and port).  
ReportError flag suppresses error reports for functions that  
don't need reporting.  
  
</pre>
### getChannelResultPrincipal(aChannel) ###
<pre>  
Get the principal for the given channel.  This will typically be the  
channel owner if there is one, and the codebase principal for the  
channel's URI otherwise.  aChannel must not be null.  
  
</pre>
### getChannelURIPrincipal(aChannel) ###
<pre>  
Get the codebase principal for the channel's URI.  
aChannel must not be null.  
  
</pre>
### isSystemPrincipal(aPrincipal) ###
<pre>  
Check whether a given principal is a system principal.  This allows us  
to avoid handing back the system principal to script while allowing  
script to check whether a given principal is system.  
  
</pre>
### getJarPrefix(appId, inMozBrowser) ###
<pre>  
Returns the jar prefix for the app.  
appId can be NO_APP_ID or a valid app id. appId should not be  
UNKNOWN_APP_ID.  
inMozBrowser has to be true if the app is inside a mozbrowser iframe.  
  
</pre>
### activateDomainPolicy() ###
<pre>  
Per-domain controls to enable and disable script. This system is designed  
to be used by at most one consumer, and enforces this with its semantics.  
  
Initially, domainPolicyActive is false. When activateDomainPolicy() is  
invoked, domainPolicyActive becomes true, and subsequent calls to  
activateDomainPolicy() will fail until deactivate() is invoked on the  
nsIDomainPolicy returned from activateDomainPolicy(). At this point,  
domainPolicyActive becomes false again, and a new consumer may acquire  
control of the system by invoking activateDomainPolicy().  
  
</pre>
### policyAllowsScript(aDomain) ###
<pre>  
Query mechanism for the above policy.  
  
If domainPolicyEnabled is false, this simply returns the current value  
of javascript.enabled. Otherwise, it returns the same value, but taking  
the various blacklist/whitelist exceptions into account.  
  
</pre>
## Attributes ##

### domainPolicyActive ###

## Constants ##

### STANDARD ###
<pre>  
Default CheckLoadURI permissions  
  
</pre>
### LOAD_IS_AUTOMATIC_DOCUMENT_REPLACEMENT ###

### ALLOW_CHROME ###

### DISALLOW_INHERIT_PRINCIPAL ###

### DISALLOW_SCRIPT_OR_DATA ###

### DISALLOW_SCRIPT ###

### DONT_REPORT_ERRORS ###

### NO_APP_ID ###

### UNKNOWN_APP_ID ###

### SAFEBROWSING_APP_ID ###
