---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cache/nsICacheVisitor.idl">Source file</a>
</div>

# nsICacheVisitor #

## Methods ##

### visitDevice(deviceID, deviceInfo) ###
  
Called to provide information about a cache device.  
  
  
  

#### Parameters ####

<table>

<tr>
<td>deviceID</td>
<td>- specifies the device being visited.  
</td>
</tr>

<tr>
<td>deviceInfo</td>
<td>- specifies information about this device.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>false to advance to the next device.  
</td>
</tr>

</table>

### visitEntry(deviceID, entryInfo) ###
  
Called to provide information about a cache entry.  
  
  
  

#### Parameters ####

<table>

<tr>
<td>deviceID</td>
<td>- specifies the device being visited.  
</td>
</tr>

<tr>
<td>entryInfo</td>
<td>- specifies information about this entry.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>false to advance to the next device.  
</td>
</tr>

</table>
