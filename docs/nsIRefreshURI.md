---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIRefreshURI.idl">Source file</a>
</div>
# nsIRefreshURI #

## Methods ##

### refreshURI(aURI, aMillis, aRepeat, aMetaRefresh) ###
  
Load a uri after waiting for aMillis milliseconds. If the docshell  
is busy loading a page currently, the refresh request will be  
queued and executed when the current load finishes.   
  
@param aUri The uri to refresh.  
@param aMillis The number of milliseconds to wait.  
@param aRepeat Flag to indicate if the uri is to be   
               repeatedly refreshed every aMillis milliseconds.  
@param aMetaRefresh Flag to indicate if this is a Meta refresh.  
  

#### Parameters ####

<table>

<tr>
<td>aUri</td>
<td>The uri to refresh.  
</td>
</tr>

<tr>
<td>aMillis</td>
<td>The number of milliseconds to wait.  
</td>
</tr>

<tr>
<td>aRepeat</td>
<td>Flag to indicate if the uri is to be   
               repeatedly refreshed every aMillis milliseconds.  
</td>
</tr>

<tr>
<td>aMetaRefresh</td>
<td>Flag to indicate if this is a Meta refresh.  
</td>
</tr>

</table>

### forceRefreshURI(aURI, aMillis, aMetaRefresh) ###
  
Loads a URI immediately as if it were a refresh.  
  
@param aURI The URI to refresh.  
@param aMillis The number of milliseconds by which this refresh would  
               be delayed if it were not being forced.  
@param aMetaRefresh Flag to indicate if this is a meta refresh.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>The URI to refresh.  
</td>
</tr>

<tr>
<td>aMillis</td>
<td>The number of milliseconds by which this refresh would  
               be delayed if it were not being forced.  
</td>
</tr>

<tr>
<td>aMetaRefresh</td>
<td>Flag to indicate if this is a meta refresh.  
</td>
</tr>

</table>

### setupRefreshURI(aChannel) ###
  
Checks the passed in channel to see if there is a refresh header,   
if there is, will setup a timer to refresh the uri found  
in the header. If docshell is busy loading a page currently, the  
request will be queued and executed when the current page   
finishes loading.   
  
Returns the NS_REFRESHURI_HEADER_FOUND success code if a refresh  
header was found and successfully setup.  
  
@param aChannel The channel to be parsed.   
  

#### Parameters ####

<table>

<tr>
<td>aChannel</td>
<td>The channel to be parsed.   
</td>
</tr>

</table>

### setupRefreshURIFromHeader(aBaseURI, principal, aHeader) ###
  
Parses the passed in header string and sets up a refreshURI if  
a "refresh" header is found. If docshell is busy loading a page   
currently, the request will be queued and executed when   
the current page finishes loading.   
  
@param aBaseURI base URI to resolve refresh uri with.  
@param principal the associated principal  
@param aHeader  The meta refresh header string.  
  

#### Parameters ####

<table>

<tr>
<td>aBaseURI</td>
<td>base URI to resolve refresh uri with.  
</td>
</tr>

<tr>
<td>principal</td>
<td>the associated principal  
</td>
</tr>

<tr>
<td>aHeader</td>
<td>The meta refresh header string.  
</td>
</tr>

</table>

### cancelRefreshURITimers() ###
  
Cancels all timer loads.  
  

## Attributes ##

### refreshPending ###
  
True when there are pending refreshes, false otherwise.  
  
