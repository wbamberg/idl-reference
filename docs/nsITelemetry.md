---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/telemetry/nsITelemetry.idl">Source file</a>
</div>

# nsITelemetry #

## Methods ##

### registeredHistograms(count, histograms) ###
<code>  
Returns an array whose values are the names of histograms defined  
in Histograms.json.  
  
</code>
### newHistogram(name, expiration, min, max, bucket_count, histogram_type) ###
<code>   
Create and return a histogram.  Parameters:  
  
@param name Unique histogram name  
@param expiration Expiration version  
@param min - Minimal bucket size  
@param max - Maximum bucket size  
@param bucket_count - number of buckets in the histogram.  
@param type - HISTOGRAM_EXPONENTIAL, HISTOGRAM_LINEAR, HISTOGRAM_BOOLEAN or HISTOGRAM_COUNT  
The returned object has the following functions:  
  add(int) - Adds an int value to the appropriate bucket  
  snapshot() - Returns a snapshot of the histogram with the same data fields as in histogramSnapshots()  
  clear() - Zeros out the histogram's buckets and sum  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>Unique histogram name  
</td>
</tr>

<tr>
<td>expiration</td>
<td>Expiration version  
</td>
</tr>

<tr>
<td>min</td>
<td>- Minimal bucket size  
</td>
</tr>

<tr>
<td>max</td>
<td>- Maximum bucket size  
</td>
</tr>

<tr>
<td>bucket_count</td>
<td>- number of buckets in the histogram.  
</td>
</tr>

<tr>
<td>type</td>
<td>- HISTOGRAM_EXPONENTIAL, HISTOGRAM_LINEAR, HISTOGRAM_BOOLEAN or HISTOGRAM_COUNT  
The returned object has the following functions:  
  add(int) - Adds an int value to the appropriate bucket  
  snapshot() - Returns a snapshot of the histogram with the same data fields as in histogramSnapshots()  
  clear() - Zeros out the histogram's buckets and sum  
</td>
</tr>

</table>

### histogramFrom(name, existing_name) ###
<code>  
Create a histogram using the current state of an existing histogram.  The  
existing histogram must be registered in TelemetryHistograms.h.  
  
@param name Unique histogram name  
@param existing_name Existing histogram name  
The returned object has the same functions as a histogram returned from newHistogram.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>Unique histogram name  
</td>
</tr>

<tr>
<td>existing_name</td>
<td>Existing histogram name  
The returned object has the same functions as a histogram returned from newHistogram.  
</td>
</tr>

</table>

### getHistogramById(id) ###
<code>  
Same as newHistogram above, but for histograms registered in TelemetryHistograms.h.  
  
@param id - unique identifier from TelemetryHistograms.h  
  
</code>
#### Parameters ####

<table>

<tr>
<td>id</td>
<td>- unique identifier from TelemetryHistograms.h  
</td>
</tr>

</table>

### registerAddonHistogram(addon_id, name, min, max, bucket_count, histogram_type) ###
<code> Addon telemetry hooks */  
</code><code>  
Register a histogram for an addon.  Throws an error if the  
histogram name has been registered previously.  
  
@param addon_id - Unique ID of the addon  
@param name - Unique histogram name  
@param min - Minimal bucket size  
@param max - Maximum bucket size  
@param bucket_count - number of buckets in the histogram  
@param histogram_type - HISTOGRAM_EXPONENTIAL, HISTOGRAM_LINEAR,  
       HISTOGRAM_BOOLEAN or HISTOGRAM_COUNT  
  
</code>
#### Parameters ####

<table>

<tr>
<td>addon_id</td>
<td>- Unique ID of the addon  
</td>
</tr>

<tr>
<td>name</td>
<td>- Unique histogram name  
</td>
</tr>

<tr>
<td>min</td>
<td>- Minimal bucket size  
</td>
</tr>

<tr>
<td>max</td>
<td>- Maximum bucket size  
</td>
</tr>

<tr>
<td>bucket_count</td>
<td>- number of buckets in the histogram  
</td>
</tr>

<tr>
<td>histogram_type</td>
<td>- HISTOGRAM_EXPONENTIAL, HISTOGRAM_LINEAR,  
       HISTOGRAM_BOOLEAN or HISTOGRAM_COUNT  
</td>
</tr>

</table>

### getAddonHistogram(addon_id, name) ###
<code>  
Return a histogram previously registered via  
registerAddonHistogram.  Throws an error if the id/name combo has  
not been registered via registerAddonHistogram.  
  
@param addon_id - Unique ID of the addon  
@param name - Registered histogram name  
  
The returned object has the same functions as a histogram returned  
from newHistogram.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>addon_id</td>
<td>- Unique ID of the addon  
</td>
</tr>

<tr>
<td>name</td>
<td>- Registered histogram name  
</td>
</tr>

</table>

### unregisterAddonHistograms(addon_id) ###
<code>  
Delete all histograms associated with the given addon id.  
  
@param addon_id - Unique ID of the addon  
  
</code>
#### Parameters ####

<table>

<tr>
<td>addon_id</td>
<td>- Unique ID of the addon  
</td>
</tr>

</table>

### asyncFetchTelemetryData(aCallback) ###
<code>  
Read data from the previous run. After the callback is called, the last  
shutdown time is available in lastShutdownDuration and any late  
writes in lateWrites.  
  
</code>
### msSinceProcessStart() ###
<code>  
Return the number of seconds since process start using monotonic  
timestamps (unaffected by system clock changes).  
@throws NS_ERROR_NOT_AVAILABLE if TimeStamp doesn't have the data.  
  
</code>
## Attributes ##

### histogramSnapshots ###

### lastShutdownDuration ###
  
The amount of time, in milliseconds, that the last session took  
to shutdown.  Reads as 0 to indicate failure.  
  

### failedProfileLockCount ###
  
The number of failed profile lock attempts that have occurred prior to   
successfully locking the profile  
  

### slowSQL ###

### debugSlowSQL ###

### maximalNumberOfConcurrentThreads ###
  
A number representing the highest number of concurrent threads  
reached during this session.  
  

### chromeHangs ###

### threadHangStats ###

### lateWrites ###

### canRecord ###
  
Set this to false to disable gathering of telemetry statistics.  
  

### canSend ###
  
A flag indicating whether Telemetry can submit official results.  
  

### addonHistogramSnapshots ###
  
An object containing a snapshot from all of the currently  
registered addon histograms.  
{ addon-id1 : data1, ... }  
  
where data is an object whose properties are the names of the  
addon's histograms and whose corresponding values are as in  
histogramSnapshots.  
  

### fileIOReports ###
  
Get statistics of file IO reports, null, if not recorded.  
  
The statistics are returned as an object whose propoerties are the names  
of the files that have been accessed and whose corresponding values are  
arrays of size three, representing startup, normal, and shutdown stages.  
Each stage's entry is either null or an array with the layout  
[total_time, #creates, #reads, #writes, #fsyncs, #stats]  
  

## Constants ##

### HISTOGRAM_EXPONENTIAL ###
  
Histogram types:  
HISTOGRAM_EXPONENTIAL - buckets increase exponentially  
HISTOGRAM_LINEAR - buckets increase linearly  
HISTOGRAM_BOOLEAN - For storing 0/1 values  
HISTOGRAM_FLAG - For storing a single value; its count is always == 1.  
HISTOGRAM_COUNT - For storing counter values without bucketing.  
  

### HISTOGRAM_LINEAR ###

### HISTOGRAM_BOOLEAN ###

### HISTOGRAM_FLAG ###

### HISTOGRAM_COUNT ###
