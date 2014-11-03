---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/apps/nsIAppsService.idl">Source file</a>
</div>

# nsIAppsService #

## Methods ##

### getAppByManifestURL(manifestURL) ###

### getManifestFor(manifestURL) ###
<pre>  
Returns a Promise for the manifest for a given manifestURL.  
This is only supported in the parent process: the promise will be rejected  
in content processes.  
  
</pre>
### getAppLocalIdByManifestURL(manifestURL) ###
<pre>  
Returns the |localId| of the app associated with the |manifestURL| passed  
in parameter.  
Returns nsIScriptSecurityManager::NO_APP_ID if |manifestURL| isn't a valid  
installed manifest URL.  
  
</pre>
### getAppByLocalId(localId) ###
<pre>  
Returns the application associated to this localId.  
  
</pre>
### getManifestURLByLocalId(localId) ###
<pre>  
Returns the manifest URL associated to this localId.  
  
</pre>
### getManifestCSPByLocalId(localId) ###
<pre>  
Returns the manifest CSP associated to this localId.  
  
</pre>
### getDefaultCSPByLocalId(localId) ###
<pre>  
Returns the default CSP associated to this localId.  
  
</pre>
### getCoreAppsBasePath() ###
<pre>  
Returns the basepath for core apps  
  
</pre>
### getWebAppsBasePath() ###
<pre>  
Returns the basepath for regular packaged apps  
  
</pre>
### getAppInfo(appId) ###

### getRedirect(localId, uri) ###
<pre>  
Returns a URI to redirect to when we get a redirection to 'uri'.  
Returns null if no redirection is declared for this uri.  
  
</pre>
### getAppLocalIdByStoreId(storeID) ###
<pre>  
Returns the localId if the app was installed from a store  
  
</pre>