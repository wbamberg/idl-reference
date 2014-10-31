---
layout: default
---

# nsIURIChecker #
  
nsIURIChecker  
  
The URI checker is a component that can be used to verify the existence  
of a resource at the location specified by a given URI.  It will use  
protocol specific methods to verify the URI (e.g., use of HEAD request  
for HTTP URIs).  
  

## Methods ##

### init(aURI) ###
  
Initializes the URI checker.  After this method is called, it is valid  
to further configure the URI checker by calling its nsIRequest methods.  
This method creates the channel that will be used to verify the URI.  
In the case of the HTTP protocol, only a HEAD request will be issued.  
  
@param aURI  
       The URI to be checked.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI to be checked.  
</td>
</tr>

</table>

### asyncCheck(aObserver, aContext) ###
  
Begin asynchronous checking URI for validity.  Notification will be  
asynchronous through the nsIRequestObserver callback interface.  When  
OnStartRequest is fired, the baseChannel attribute will have been  
updated to reflect the final channel used (corresponding to any redirects  
that may have been followed).  
  
Our interpretations of the nsIRequestObserver status codes:  
  NS_BINDING_SUCCEEDED:   link is valid  
  NS_BINDING_FAILED:      link is invalid (gave an error)  
  NS_BINDING_ABORTED:     timed out, or cancelled  
  
@param aObserver  
       The object to notify when the link is verified.  We will  
       call aObserver.OnStartRequest followed immediately by  
       aObserver.OnStopRequest.  It is recommended that the caller use  
       OnStopRequest to act on the link's status.  The underlying request  
       will not be cancelled until after OnStopRequest has been called.  
@param aContext  
       A closure that will be passed back to the nsIRequestObserver  
       methods.  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>       The object to notify when the link is verified.  We will  
       call aObserver.OnStartRequest followed immediately by  
       aObserver.OnStopRequest.  It is recommended that the caller use  
       OnStopRequest to act on the link's status.  The underlying request  
       will not be cancelled until after OnStopRequest has been called.  
</td>
</tr>

<tr>
<td>aContext</td>
<td>       A closure that will be passed back to the nsIRequestObserver  
       methods.  
</td>
</tr>

</table>

## Attributes ##

### baseChannel ###
  
Returns the base channel that will be used to verify the URI.  
  
