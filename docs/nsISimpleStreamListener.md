---
layout: default
---

# nsISimpleStreamListener #
  
A simple stream listener can be used with AsyncRead to supply data to  
a output stream.  
  

## Methods ##

### init(aSink, aObserver) ###
  
Initialize the simple stream listener.  
  
@param aSink data will be read from the channel to this output stream.  
             Must implement writeFrom.  
@param aObserver optional stream observer (can be NULL)  
  

#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>data will be read from the channel to this output stream.  
             Must implement writeFrom.  
</td>
</tr>

<tr>
<td>aObserver</td>
<td>optional stream observer (can be NULL)  
</td>
</tr>

</table>
