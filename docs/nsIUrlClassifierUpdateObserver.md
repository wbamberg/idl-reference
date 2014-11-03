---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/url-classifier/nsIUrlClassifierDBService.idl">Source file</a>
</div>

# nsIUrlClassifierUpdateObserver #
<code>  
The nsIUrlClassifierUpdateObserver interface is implemented by  
clients streaming updates to the url-classifier (usually  
nsUrlClassifierStreamUpdater.  
  
</code>
## Methods ##

### updateUrlRequested(url, table) ###
<code>  
The update requested a new URL whose contents should be downloaded  
and sent to the classifier as a new stream.  
  
@param url The url that was requested.  
@param table The table name that this URL's contents will be associated  
             with.  This should be passed back to beginStream().  
  
</code>
#### Parameters ####

<table>

<tr>
<td>url</td>
<td>The url that was requested.  
</td>
</tr>

<tr>
<td>table</td>
<td>The table name that this URL's contents will be associated  
             with.  This should be passed back to beginStream().  
</td>
</tr>

</table>

### streamFinished(status, delay) ###
<code>  
A stream update has completed.  
  
@param status The state of the update process.  
@param delay The amount of time the updater should wait to fetch the  
             next URL in ms.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>status</td>
<td>The state of the update process.  
</td>
</tr>

<tr>
<td>delay</td>
<td>The amount of time the updater should wait to fetch the  
             next URL in ms.  
</td>
</tr>

</table>

### updateError(error) ###

### updateSuccess(requestedTimeout) ###
<code>  
The update has completed successfully.  
  
@param requestedTimeout The number of seconds that the caller should  
                        wait before trying to update again.  
/  
</code>
#### Parameters ####

<table>

<tr>
<td>requestedTimeout</td>
<td>The number of seconds that the caller should  
                        wait before trying to update again.  
/  
</td>
</tr>

</table>
