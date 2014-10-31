---
layout: default
---

# nsIAsyncStreamCopier2 #

## Methods ##

### init(aSource, aSink, aTarget, aChunkSize, aCloseSource, aCloseSink) ###
  
Initialize the stream copier.  
  
If neither the source nor the sink are buffered, buffering will  
be automatically added to the sink.  
  
  
@param aSource  
       contains the data to be copied.  
@param aSink  
       specifies the destination for the data.  
@param aTarget  
       specifies the thread on which the copy will occur.  a null value  
       is permitted and will cause the copy to occur on an unspecified  
       background thread.  
@param aChunkSize  
       specifies how many bytes to read/write at a time.  this controls  
       the granularity of the copying.  it should match the segment size  
       of the "buffered" streams involved.  
@param aCloseSource  
       true if aSource should be closed after copying (this is generally  
       the desired behavior).  
@param aCloseSink  
       true if aSink should be closed after copying (this is generally  
       the desired behavior).  
  

#### Parameters ####

<table>

<tr>
<td>aSource</td>
<td>       contains the data to be copied.  
</td>
</tr>

<tr>
<td>aSink</td>
<td>       specifies the destination for the data.  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>       specifies the thread on which the copy will occur.  a null value  
       is permitted and will cause the copy to occur on an unspecified  
       background thread.  
</td>
</tr>

<tr>
<td>aChunkSize</td>
<td>       specifies how many bytes to read/write at a time.  this controls  
       the granularity of the copying.  it should match the segment size  
       of the "buffered" streams involved.  
</td>
</tr>

<tr>
<td>aCloseSource</td>
<td>       true if aSource should be closed after copying (this is generally  
       the desired behavior).  
</td>
</tr>

<tr>
<td>aCloseSink</td>
<td>       true if aSink should be closed after copying (this is generally  
       the desired behavior).  
</td>
</tr>

</table>

### asyncCopy(aObserver, aObserverContext) ###
  
asyncCopy triggers the start of the copy.  The observer will be notified  
when the copy completes.  
  
@param aObserver  
       receives notifications.  
@param aObserverContext  
       passed to observer methods.  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>       receives notifications.  
</td>
</tr>

<tr>
<td>aObserverContext</td>
<td>       passed to observer methods.  
</td>
</tr>

</table>
