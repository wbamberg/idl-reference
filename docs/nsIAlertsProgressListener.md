---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/alerts/nsIAlertsService.idl">Source file</a>
</div>

# nsIAlertsProgressListener #

## Methods ##

### onProgress(name, progress, progressMax, text) ###
<pre>  
Called to notify the alert service that progress has occurred for the  
given notification previously displayed with showAlertNotification().  
  
@param name         The name of the notification displaying the  
                    progress. On Android the name is hashed and used  
                    as a notification ID.  
@param progress     Numeric value in the range 0 to progressMax  
                    indicating the current progress.  
@param progressMax  Numeric value indicating the maximum progress.  
@param text         The contents of the alert. If not provided,  
                    the percentage will be displayed.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The name of the notification displaying the  
                    progress. On Android the name is hashed and used  
                    as a notification ID.  
</td>
</tr>

<tr>
<td>progress</td>
<td>Numeric value in the range 0 to progressMax  
                    indicating the current progress.  
</td>
</tr>

<tr>
<td>progressMax</td>
<td>Numeric value indicating the maximum progress.  
</td>
</tr>

<tr>
<td>text</td>
<td>The contents of the alert. If not provided,  
                    the percentage will be displayed.  
</td>
</tr>

</table>

### onCancel(name) ###
<pre>  
Called to cancel and hide the given notification previously displayed  
with showAlertNotification().  
  
@param name         The name of the notification.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The name of the notification.  
</td>
</tr>

</table>
