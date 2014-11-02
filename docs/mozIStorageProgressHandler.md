---
layout: default
---

# mozIStorageProgressHandler #
  
mozIProgressHandler is to be implemented by storage consumers that  
wish to receive callbacks during the request execution.  
  

## Methods ##

### onProgress(aConnection) ###
  
onProgress is invoked periodically during long running calls.  
  
@param aConnection    connection, for which progress handler is  
                      invoked.  
  
@return true to abort request, false to continue work.  
  

#### Parameters ####

<table>

<tr>
<td>aConnection</td>
<td>connection, for which progress handler is  
                      invoked.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true to abort request, false to continue work.  
</td>
</tr>

</table>
