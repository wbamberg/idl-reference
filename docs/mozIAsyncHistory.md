---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIAsyncHistory.idl">Source file</a>
</div>

# mozIAsyncHistory #

## Methods ##

### getPlacesInfo(aPlaceIdentifiers, aCallback) ###
  
Gets the available information for the given array of places, each  
identified by either nsIURI or places GUID (string).  
  
The retrieved places info objects DO NOT include the visits data (the  
|visits| attribute is set to null).  
  
If a given place does not exist in the database, aCallback.handleError is  
called for it with NS_ERROR_NOT_AVAILABLE result code.  
  
@param aPlaceIdentifiers  
       The place[s] for which to retrieve information, identified by either  
       a single place GUID, a single URI, or a JS array of URIs and/or GUIDs.  
@param aCallback  
       A mozIVisitInfoCallback object which consists of callbacks to be  
       notified for successful or failed retrievals.  
       If there's no information available for a given place, aCallback  
       is called with a stub place info object, containing just the provided  
       data (GUID or URI).  
  
@throws NS_ERROR_INVALID_ARG  
        - Passing in NULL for aPlaceIdentifiers or aCallback.  
        - Not providing at least one valid GUID or URI.   
  

#### Parameters ####

<table>

<tr>
<td>aPlaceIdentifiers</td>
<td>       The place[s] for which to retrieve information, identified by either  
       a single place GUID, a single URI, or a JS array of URIs and/or GUIDs.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       A mozIVisitInfoCallback object which consists of callbacks to be  
       notified for successful or failed retrievals.  
       If there's no information available for a given place, aCallback  
       is called with a stub place info object, containing just the provided  
       data (GUID or URI).  
</td>
</tr>

</table>

### updatePlaces(aPlaceInfo, aCallback) ###
  
Adds a set of visits for one or more mozIPlaceInfo objects, and updates  
each mozIPlaceInfo's title or guid.  
  
aCallback.handleResult is called for each visit added.  
  
@param aPlaceInfo  
       The mozIPlaceInfo object[s] containing the information to store or  
       update.  This can be a single object, or an array of objects.  
@param [optional] aCallback  
       A mozIVisitInfoCallback object which consists of callbacks to be  
       notified for successful and/or failed changes.  
  
@throws NS_ERROR_INVALID_ARG  
        - Passing in NULL for aPlaceInfo.  
        - Not providing at least one valid guid, or uri for all  
          mozIPlaceInfo object[s].  
        - Not providing an array or nothing for the visits property of  
          mozIPlaceInfo.  
        - Not providing a visitDate and transitionType for each  
          mozIVisitInfo.  
        - Providing an invalid transitionType for a mozIVisitInfo.  
  

#### Parameters ####

<table>

<tr>
<td>aPlaceInfo</td>
<td>       The mozIPlaceInfo object[s] containing the information to store or  
       update.  This can be a single object, or an array of objects.  
</td>
</tr>

<tr>
<td>[optional]</td>
<td>aCallback  
       A mozIVisitInfoCallback object which consists of callbacks to be  
       notified for successful and/or failed changes.  
</td>
</tr>

</table>

### isURIVisited(aURI, aCallback) ###
  
Checks if a given URI has been visited.  
  
@param aURI  
       The URI to check for.  
@param aCallback  
       A mozIVisitStatusCallback object which receives the visited status.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI to check for.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       A mozIVisitStatusCallback object which receives the visited status.  
</td>
</tr>

</table>
