---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/apps/nsIAppsService.idl">Source file</a>
</div>
# nsIAppsService #

## Methods ##

### getAppByManifestURL(manifestURL) ###

### getManifestFor(manifestURL) ###
  
Returns a Promise for the manifest for a given manifestURL.  
This is only supported in the parent process: the promise will be rejected  
in content processes.  
  

### getAppLocalIdByManifestURL(manifestURL) ###
  
Returns the |localId| of the app associated with the |manifestURL| passed  
in parameter.  
Returns nsIScriptSecurityManager::NO_APP_ID if |manifestURL| isn't a valid  
installed manifest URL.  
  

### getAppByLocalId(localId) ###
  
Returns the application associated to this localId.  
  

### getManifestURLByLocalId(localId) ###
  
Returns the manifest URL associated to this localId.  
  

### getManifestCSPByLocalId(localId) ###
  
Returns the manifest CSP associated to this localId.  
  

### getDefaultCSPByLocalId(localId) ###
  
Returns the default CSP associated to this localId.  
  

### getCoreAppsBasePath() ###
  
Returns the basepath for core apps  
  

### getWebAppsBasePath() ###
  
Returns the basepath for regular packaged apps  
  

### getAppInfo(appId) ###

### getRedirect(localId, uri) ###
  
Returns a URI to redirect to when we get a redirection to 'uri'.  
Returns null if no redirection is declared for this uri.  
  

### getAppLocalIdByStoreId(storeID) ###
  
Returns the localId if the app was installed from a store  
  
