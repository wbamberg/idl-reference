---
layout: default
---

# nsIHandlerApp #
  
nsIHandlerApp represents an external application that can handle content  
of some sort (either a MIME type or a protocol).  
  
FIXME: now that we've made nsIWebHandlerApp inherit from nsIHandlerApp,  
we should also try to make nsIWebContentHandlerInfo inherit from or possibly  
be replaced by nsIWebHandlerApp (bug 394710).  
  

## Methods ##

### equals ###
  
Whether or not the given handler app is logically equivalent to the  
invokant (i.e. they represent the same app).  
  
Two apps are the same if they are both either local or web handlers  
and their executables/URI templates and command line parameters are  
the same.  
  
@param aHandlerApp the handler app to compare to the invokant  
  
@returns true if the two are logically equivalent, false otherwise  
  

### launchWithURI ###
  
Launches the application with the specified URI.  
  
@param aURI  
       The URI to launch this application with  
  
@param aWindowContext   
  
       Currently only relevant to web-handler apps.  If given, this  
       represents the docshell to load the handler in and is passed  
       through to nsIURILoader.openURI.  If this parameter is null or  
       not present, the web handler app implementation will attempt to   
       find/create a place to load the handler and do so.  As of this  
       writing, it tries to load the web handler in a new window using  
       nsIBrowserDOMWindow.openURI.  In the future, it may attempt to   
       have a more comprehensive strategy which could include handing  
       off to the system default browser (bug 394479).  
  

## Attributes ##

### name ###
  
Human readable name for the handler  
  

### detailedDescription ###
  
Detailed description for this handler. Suitable for  
a tooltip or short informative sentence.  
  
