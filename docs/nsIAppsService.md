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
<code>  
Returns a Promise for the manifest for a given manifestURL.  
This is only supported in the parent process: the promise will be rejected  
in content processes.  
  
</code>
### getAppLocalIdByManifestURL(manifestURL) ###
<code>  
Returns the |localId| of the app associated with the |manifestURL| passed  
in parameter.  
Returns nsIScriptSecurityManager::NO_APP_ID if |manifestURL| isn't a valid  
installed manifest URL.  
  
</code>
### getAppByLocalId(localId) ###
<code>  
Returns the application associated to this localId.  
  
</code>
### getManifestURLByLocalId(localId) ###
<code>  
Returns the manifest URL associated to this localId.  
  
</code>
### getManifestCSPByLocalId(localId) ###
<code>  
Returns the manifest CSP associated to this localId.  
  
</code>
### getDefaultCSPByLocalId(localId) ###
<code>  
Returns the default CSP associated to this localId.  
  
</code>
### getCoreAppsBasePath() ###
<code>  
Returns the basepath for core apps  
  
</code>
### getWebAppsBasePath() ###
<code>  
Returns the basepath for regular packaged apps  
  
</code>
### getAppInfo(appId) ###

### getRedirect(localId, uri) ###
<code>  
Returns a URI to redirect to when we get a redirection to 'uri'.  
Returns null if no redirection is declared for this uri.  
  
</code>
### getAppLocalIdByStoreId(storeID) ###
<code>  
Returns the localId if the app was installed from a store  
  
</code>