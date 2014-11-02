---
layout: default
---

# nsICacheVisitor #

## Methods ##

### visitDevice(deviceID, deviceInfo) ###
  
Called to provide information about a cache device.  
  
@param deviceID - specifies the device being visited.  
@param deviceInfo - specifies information about this device.  
  
@return true to start visiting all entries for this device.  
@return false to advance to the next device.  
  

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
  
@param deviceID - specifies the device being visited.  
@param entryInfo - specifies information about this entry.  
  
@return true to visit the next entry on the current device, or if the  
  end of the device has been reached, advance to the next device.  
@return false to advance to the next device.  
  

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
