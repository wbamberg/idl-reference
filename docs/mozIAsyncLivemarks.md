---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIAsyncLivemarks.idl">Source file</a>
</div>

# mozIAsyncLivemarks #

## Methods ##

### addLivemark(aLivemarkInfo, aCallback) ###
  
Creates a new livemark  
  
@param aLivemarkInfo  
       mozILivemarkInfo object containing at least title, parentId,  
       index and feedURI of the livemark to create.  
@param [optional] aCallback  
       Invoked when the creation process is done.  In case of failure will  
       receive an error code.  
@return {Promise}  
@throws NS_ERROR_INVALID_ARG if the supplied information is insufficient  
        for the creation.  
@deprecated passing a callback is deprecated. Moreover, for backwards  
            compatibility reasons, when a callback is provided this method  
            won't return a promise.  
  

#### Parameters ####

<table>

<tr>
<td>aLivemarkInfo</td>
<td>       mozILivemarkInfo object containing at least title, parentId,  
       index and feedURI of the livemark to create.  
</td>
</tr>

<tr>
<td>[optional]</td>
<td>aCallback  
       Invoked when the creation process is done.  In case of failure will  
       receive an error code.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>{Promise}  
@throws NS_ERROR_INVALID_ARG if the supplied information is insufficient  
        for the creation.  
@deprecated passing a callback is deprecated. Moreover, for backwards  
            compatibility reasons, when a callback is provided this method  
            won't return a promise.  
</td>
</tr>

</table>

### removeLivemark(aLivemarkInfo, aCallback) ###
  
Removes an existing livemark.  
  
@param aLivemarkInfo  
       mozILivemarkInfo object containing either an id or a guid of the  
       livemark to remove.  
@param [optional] aCallback  
       Invoked when the removal process is done.  In case of failure will  
       receive an error code.  
  
@return {Promise}  
@throws NS_ERROR_INVALID_ARG if the id/guid is invalid.  
@deprecated passing a callback is deprecated. Moreover, for backwards  
            compatibility reasons, when a callback is provided this method  
            won't return a promise.  
  

#### Parameters ####

<table>

<tr>
<td>aLivemarkInfo</td>
<td>       mozILivemarkInfo object containing either an id or a guid of the  
       livemark to remove.  
</td>
</tr>

<tr>
<td>[optional]</td>
<td>aCallback  
       Invoked when the removal process is done.  In case of failure will  
       receive an error code.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>{Promise}  
@throws NS_ERROR_INVALID_ARG if the id/guid is invalid.  
@deprecated passing a callback is deprecated. Moreover, for backwards  
            compatibility reasons, when a callback is provided this method  
            won't return a promise.  
</td>
</tr>

</table>

### getLivemark(aLivemarkInfo, aCallback) ###
  
Gets an existing livemark.  
  
@param aLivemarkInfo  
       mozILivemarkInfo object containing either an id or a guid of the  
       livemark to retrieve.  
@param [optional] aCallback  
       Invoked when the fetching process is done.  In case of failure will  
       receive an error code.  
  
@return {Promise}  
@throws NS_ERROR_INVALID_ARG if the id/guid is invalid or an invalid  
        callback is provided.  
@deprecated passing a callback is deprecated. Moreover, for backwards  
            compatibility reasons, when a callback is provided this method  
            won't return a promise.  
  

#### Parameters ####

<table>

<tr>
<td>aLivemarkInfo</td>
<td>       mozILivemarkInfo object containing either an id or a guid of the  
       livemark to retrieve.  
</td>
</tr>

<tr>
<td>[optional]</td>
<td>aCallback  
       Invoked when the fetching process is done.  In case of failure will  
       receive an error code.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>{Promise}  
@throws NS_ERROR_INVALID_ARG if the id/guid is invalid or an invalid  
        callback is provided.  
@deprecated passing a callback is deprecated. Moreover, for backwards  
            compatibility reasons, when a callback is provided this method  
            won't return a promise.  
</td>
</tr>

</table>

### reloadLivemarks(aForceUpdate) ###
  
Reloads all livemarks if they are expired or if forced to do so.  
  
@param [optional]aForceUpdate  
       If set to true forces a reload even if contents are still valid.  
  
@note The update process is asynchronous, observers registered through  
      registerForUpdates will be notified of updated contents.  
  

#### Parameters ####

<table>

<tr>
<td>[optional]aForceUpdate</td>
<td>       If set to true forces a reload even if contents are still valid.  
</td>
</tr>

</table>
