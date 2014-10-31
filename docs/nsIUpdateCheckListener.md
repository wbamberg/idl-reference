---
layout: default
---

# nsIUpdateCheckListener #
  
An interface describing an object that listens to the progress of an update  
check operation. This object is notified as the check continues, finishes  
and if it has an error.  
  

## Methods ##

### onCheckComplete(request, updates, updateCount) ###
  
The update check was completed.  
@param   request  
         The nsIXMLHttpRequest handling the update check.  
@param   updates  
         An array of nsIUpdate objects listing available updates.  
@param   updateCount  
         The size of the |updates| array.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>request  
         The nsIXMLHttpRequest handling the update check.  
</td>
</tr>

<tr>
<td></td>
<td>request  
         The nsIXMLHttpRequest handling the update check.  
</td>
</tr>

<tr>
<td></td>
<td>request  
         The nsIXMLHttpRequest handling the update check.  
</td>
</tr>

</table>

### onError(request, update) ###
  
An error occurred while loading the remote update service file.  
@param   request  
         The nsIXMLHttpRequest handling the update check.  
@param   update  
         A nsIUpdate object that contains details about the  
         error in its |statusText| property.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>request  
         The nsIXMLHttpRequest handling the update check.  
</td>
</tr>

<tr>
<td></td>
<td>request  
         The nsIXMLHttpRequest handling the update check.  
</td>
</tr>

</table>
