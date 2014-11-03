---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIConsoleAPIStorage.idl">Source file</a>
</div>

# nsIConsoleAPIStorage #

## Methods ##

### getEvents(aId) ###
  
Get the events array by inner window ID or all events from all windows.  
  
  

#### Parameters ####

<table>

<tr>
<td>string</td>
<td>[aId]  
       Optional, the inner window ID for which you want to get the array of  
       cached events.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>array  
         The array of cached events for the given window. If no |aId| is  
         given this function returns all of the cached events, from any  
         window.  
</td>
</tr>

</table>

### recordEvent(aId, aEvent) ###
  
Record an event associated with the given window ID.  
  
  

#### Parameters ####

<table>

<tr>
<td>string</td>
<td>aId  
       The ID of the inner window for which the event occurred or "jsm" for  
       messages logged from JavaScript modules..  
</td>
</tr>

<tr>
<td>object</td>
<td>aEvent  
       A JavaScript object you want to store.  
</td>
</tr>

</table>

### clearEvents(aId) ###
  
Clear storage data for the given window.  
  
  

#### Parameters ####

<table>

<tr>
<td>string</td>
<td>[aId]  
       Optional, the inner window ID for which you want to clear the  
       messages. If this is not specified all of the cached messages are  
       cleared, from all window objects.  
</td>
</tr>

</table>
