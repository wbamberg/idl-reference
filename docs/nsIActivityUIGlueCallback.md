---
layout: default
---

# nsIActivityUIGlueCallback #

## Methods ##

### handleEvent(resultType, result) ###
  
Called if the user picked an activitiy to launch.  
@param resultType Inidcates that {@code result} is an index or a native activity result.  
@param result     If WEBAPPS_ACTIVITY, the index of the chosen activity. Send '-1' if no choice is made.  
If NATIVE_ACTIVITY, the return value to be sent to the MozActivity.  
  

#### Parameters ####

<table>

<tr>
<td>resultType</td>
<td>Inidcates that {@code result} is an index or a native activity result.  
</td>
</tr>

<tr>
<td>resultType</td>
<td>Inidcates that {@code result} is an index or a native activity result.  
</td>
</tr>

</table>

## Constants ##

### WEBAPPS_ACTIVITY ###
  
The activity service should start the activity at the specified index.  
  

### NATIVE_ACTIVITY ###
  
The activity service should deliver the specified result to the MozActivity callback.  
  
