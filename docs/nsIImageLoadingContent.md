---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIImageLoadingContent.idl">Source file</a>
</div>

# nsIImageLoadingContent #
  
This interface represents a content node that loads images.  The interface  
exists to allow getting information on the images that the content node  
loads and to allow registration of observers for the image loads.  
  
Implementors of this interface should handle all the mechanics of actually  
loading an image -- getting the URI, checking with content policies and  
the security manager to see whether loading the URI is allowed, performing  
the load, firing any DOM events as needed.  
  
An implementation of this interface may support the concepts of a  
"current" image and a "pending" image.  If it does, a request to change  
the currently loaded image will start a "pending" request which will  
become current only when the image is loaded.  It is the responsibility of  
observers to check which request they are getting notifications for.  
  
Observers added in mid-load will not get any notifications they  
missed.  We should NOT freeze this interface without considering  
this issue.  (It could be that the image status on imgIRequest is  
sufficient, when combined with the imageBlockingStatus information.)  
  
Please make sure to update the MozImageLoadingContent WebIDL  
interface to mirror this interface when changing it.  
  

## Methods ##

### addObserver(aObserver) ###
  
Used to register an image decoder observer.  Typically, this will  
be a proxy for a frame that wants to paint the image.  
Notifications from ongoing image loads will be passed to all  
registered observers.  Notifications for all request types,  
current and pending, will be passed through.  
  
  
@throws NS_ERROR_OUT_OF_MEMORY  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>the observer to register  
</td>
</tr>

</table>

### removeObserver(aObserver) ###
  
Used to unregister an image decoder observer.  
  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>the observer to unregister  
</td>
</tr>

</table>

### getRequest(aRequestType) ###
  
Accessor to get the image requests  
  
  
  
@throws NS_ERROR_UNEXPECTED if the request type requested is not  
known  
  

#### Parameters ####

<table>

<tr>
<td>aRequestType</td>
<td>a value saying which request is wanted  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the imgIRequest object (may be null, even when no error  
is thrown)  
</td>
</tr>

</table>

### frameCreated(aFrame) ###
  
Used to notify the image loading content node that a frame has been  
created.  
  

### frameDestroyed(aFrame) ###
  
Used to notify the image loading content node that a frame has been  
destroyed.  
  

### getRequestType(aRequest) ###
  
Used to find out what type of request one is dealing with (eg  
which request got passed through to the imgINotificationObserver  
interface of an observer)  
  
  
  
@throws NS_ERROR_UNEXPECTED if aRequest is not known  
  

#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>the request whose type we want to know  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>an enum value saying what type this request is  
</td>
</tr>

</table>

### loadImageWithChannel(aChannel) ###
  
loadImageWithChannel allows data from an existing channel to be  
used as the image data for this content node.  
  
  
  
@see imgILoader::loadImageWithChannel  
  
@throws NS_ERROR_NULL_POINTER if aChannel is null  
  

#### Parameters ####

<table>

<tr>
<td>aChannel</td>
<td>the channel that will deliver the data  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a stream listener to pump the image data into  
</td>
</tr>

</table>

### forceReload(aNotify) ###
  
forceReload forces reloading of the image pointed to by currentURI  
  
  

#### Parameters ####

<table>

<tr>
<td>aNotify</td>
<td>[optional] request should notify, defaults to true  
@throws NS_ERROR_NOT_AVAILABLE if there is no current URI to reload  
</td>
</tr>

</table>

### forceImageState(aForce, aState) ###
  
Enables/disables image state forcing. When |aForce| is PR_TRUE, we force  
nsImageLoadingContent::ImageState() to return |aState|. Call again with |aForce|  
as PR_FALSE to revert ImageState() to its original behaviour.  
  

### IncrementVisibleCount() ###
  
A visible count is stored, if it is non-zero then this image is considered  
visible. These methods increment, decrement, or return the visible coount.  
  

### DecrementVisibleCount() ###

### GetVisibleCount() ###

## Attributes ##

### loadingEnabled ###
  
loadingEnabled is used to enable and disable loading in  
situations where loading images is unwanted.  Note that enabling  
loading will *not* automatically trigger an image load.  
  

### imageBlockingStatus ###
  
Returns the image blocking status (@see nsIContentPolicy).  This  
will always be an nsIContentPolicy REJECT_* status for cases when  
the image was blocked.  This status always refers to the  
CURRENT_REQUEST load.  
  

### currentURI ###
  
Gets the URI of the current request, if available.  
Otherwise, returns the last URI that this content tried to load, or  
null if there haven't been any such attempts.  
  

### naturalWidth ###
  
The intrinsic size and width of this content. May differ from actual image  
size due to things like responsive image density.  
  

### naturalHeight ###

## Constants ##

### UNKNOWN_REQUEST ###
  
Request types.  Image loading content nodes attempt to do atomic  
image changes when the image url is changed.  This means that  
when the url changes the new image load will start, but the old  
image will remain the "current" request until the new image is  
fully loaded.  At that point, the old "current" request will be  
discarded and the "pending" request will become "current".  
  

### CURRENT_REQUEST ###

### PENDING_REQUEST ###
