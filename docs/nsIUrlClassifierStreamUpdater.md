---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/url-classifier/nsIUrlClassifierStreamUpdater.idl">Source file</a>
</div>

# nsIUrlClassifierStreamUpdater #
  
This is a class to manage large table updates from the server.  Rather than  
downloading the whole update and then updating the sqlite database, we  
update tables as the data is streaming in.  
  

## Methods ##

### downloadUpdates(aRequestTables, aRequestBody, aUpdateUrl, aSuccessCallback, aUpdateErrorCallback, aDownloadErrorCallback) ###
  
Try to download updates from updateUrl. If an update is already in  
progress, queues the requested update. This is used in nsIUrlListManager  
as well as in testing.  
  

#### Parameters ####

<table>

<tr>
<td>aRequestTables</td>
<td>Comma-separated list of tables included in this  
       update.  
</td>
</tr>

<tr>
<td>aRequestBody</td>
<td>The body for the request.  
</td>
</tr>

<tr>
<td>aUpdateUrl</td>
<td>The plaintext url from which to request updates.  
</td>
</tr>

<tr>
<td>aSuccessCallback</td>
<td>Called after a successful update.  
</td>
</tr>

<tr>
<td>aUpdateErrorCallback</td>
<td>Called for problems applying the update  
</td>
</tr>

<tr>
<td>aDownloadErrorCallback</td>
<td>Called if we get an http error or a  
       connection refused error.  
</td>
</tr>

</table>
