---
layout: default
---

# nsIUrlClassifierUpdateObserver #
  
The nsIUrlClassifierUpdateObserver interface is implemented by  
clients streaming updates to the url-classifier (usually  
nsUrlClassifierStreamUpdater.  
  

## Methods ##

### updateUrlRequested(url, table) ###
  
The update requested a new URL whose contents should be downloaded  
and sent to the classifier as a new stream.  
  
@param url The url that was requested.  
@param table The table name that this URL's contents will be associated  
             with.  This should be passed back to beginStream().  
  

#### Parameters ####

<table>

<tr>
<td>url</td>
<td>The url that was requested.  
</td>
</tr>

<tr>
<td>url</td>
<td>The url that was requested.  
</td>
</tr>

</table>

### streamFinished(status, delay) ###
  
A stream update has completed.  
  
@param status The state of the update process.  
@param delay The amount of time the updater should wait to fetch the  
             next URL in ms.  
  

#### Parameters ####

<table>

<tr>
<td>status</td>
<td>The state of the update process.  
</td>
</tr>

<tr>
<td>status</td>
<td>The state of the update process.  
</td>
</tr>

</table>

### updateError(error) ###

### updateSuccess(requestedTimeout) ###
  
The update has completed successfully.  
  
@param requestedTimeout The number of seconds that the caller should  
                        wait before trying to update again.  
/  

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
