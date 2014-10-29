---
layout: default
---

# nsIUrlClassifierStreamUpdater #

This is a class to manage large table updates from the server.  Rather than
downloading the whole update and then updating the sqlite database, we
update tables as the data is streaming in.


## downloadUpdates ##

Try to download updates from updateUrl. If an update is already in
progress, queues the requested update. This is used in nsIUrlListManager
as well as in testing.
@param aRequestTables Comma-separated list of tables included in this
       update.
@param aRequestBody The body for the request.
@param aUpdateUrl The plaintext url from which to request updates.
@param aSuccessCallback Called after a successful update.
@param aUpdateErrorCallback Called for problems applying the update
@param aDownloadErrorCallback Called if we get an http error or a
       connection refused error.

