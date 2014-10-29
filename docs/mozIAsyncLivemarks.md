---
layout: default
---

# mozIAsyncLivemarks #

## Methods ##

### addLivemark ###

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


### removeLivemark ###

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


### getLivemark ###

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


### reloadLivemarks ###

Reloads all livemarks if they are expired or if forced to do so.

@param [optional]aForceUpdate
       If set to true forces a reload even if contents are still valid.

@note The update process is asynchronous, observers registered through
      registerForUpdates will be notified of updated contents.

