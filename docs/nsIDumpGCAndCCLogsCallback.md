---
layout: default
---

# nsIDumpGCAndCCLogsCallback #
  
Callback interface for |dumpGCAndCCLogsToFile|, below.  Note that  
these method calls can occur before |dumpGCAndCCLogsToFile|  
returns.  
  

## Methods ##

### onDump(aGCLog, aCCLog, aIsParent) ###
  
Called whenever a process has successfully finished dumping its GC/CC logs.  
Incomplete dumps (e.g., if the child crashes or is killed due to memory  
exhaustion) are not reported.  
  
@param aGCLog The file that the GC log was written to.  
  
@param aCCLog The file that the CC log was written to.  
  
@param aIsParent indicates whether this log file pair is from the  
parent process.  
  

#### Parameters ####

<table>

<tr>
<td>aGCLog</td>
<td>The file that the GC log was written to.  
</td>
</tr>

<tr>
<td>aGCLog</td>
<td>The file that the GC log was written to.  
</td>
</tr>

<tr>
<td>aGCLog</td>
<td>The file that the GC log was written to.  
</td>
</tr>

</table>

### onFinish() ###
  
Called when GC/CC logging has finished, after all calls to |onDump|.  
  
