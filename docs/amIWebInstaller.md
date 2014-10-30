---
layout: default
---

# amIWebInstaller #
  
This interface is used to allow webpages to start installing add-ons.  
  

## Methods ##

### isInstallEnabled ###
  
Checks if installation is enabled for a webpage.  
  
@param  aMimetype  
        The mimetype for the add-on to be installed  
@param  referer  
        The URL of the webpage trying to install an add-on  
@return true if installation is enabled  
  

### installAddonsFromWebpage ###
  
Installs an array of add-ons at the request of a webpage  
  
@param  aMimetype  
        The mimetype for the add-ons  
@param  aOriginator  
        If not e10s, the window installing the add-ons, otherwise the  
        browser installing the add-ons.  
@param  aReferer  
        The URI for the webpage installing the add-ons  
@param  aUris  
        The URIs of add-ons to be installed  
@param  aHashes  
        The hashes for the add-ons to be installed  
@param  aNames  
        The names for the add-ons to be installed  
@param  aIcons  
        The icons for the add-ons to be installed  
@param  aCallback  
        An optional callback to notify about installation success and  
        failure  
@param  aInstallCount  
        An optional argument including the number of add-ons to install  
@return true if the installation was successfully started  
  
