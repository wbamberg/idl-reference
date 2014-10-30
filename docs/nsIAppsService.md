---
layout: default
---

# nsIAppsService #

## Methods ##

### getAppByManifestURL ###

### getManifestFor ###
  
Returns a Promise for the manifest for a given manifestURL.  
This is only supported in the parent process: the promise will be rejected  
in content processes.  
  

### getAppLocalIdByManifestURL ###
  
Returns the |localId| of the app associated with the |manifestURL| passed  
in parameter.  
Returns nsIScriptSecurityManager::NO_APP_ID if |manifestURL| isn't a valid  
installed manifest URL.  
  

### getAppByLocalId ###
  
Returns the application associated to this localId.  
  

### getManifestURLByLocalId ###
  
Returns the manifest URL associated to this localId.  
  

### getManifestCSPByLocalId ###
  
Returns the manifest CSP associated to this localId.  
  

### getDefaultCSPByLocalId ###
  
Returns the default CSP associated to this localId.  
  

### getCoreAppsBasePath ###
  
Returns the basepath for core apps  
  

### getWebAppsBasePath ###
  
Returns the basepath for regular packaged apps  
  

### getAppInfo ###

### getRedirect ###
  
Returns a URI to redirect to when we get a redirection to 'uri'.  
Returns null if no redirection is declared for this uri.  
  

### getAppLocalIdByStoreId ###
  
Returns the localId if the app was installed from a store  
  
