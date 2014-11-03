---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIMemoryInfoDumper.idl">Source file</a>
</div>

# nsIDumpGCAndCCLogsCallback #
<pre>  
Callback interface for |dumpGCAndCCLogsToFile|, below.  Note that  
these method calls can occur before |dumpGCAndCCLogsToFile|  
returns.  
  
</pre>
## Methods ##

### onDump(aGCLog, aCCLog, aIsParent) ###
<pre>  
Called whenever a process has successfully finished dumping its GC/CC logs.  
Incomplete dumps (e.g., if the child crashes or is killed due to memory  
exhaustion) are not reported.  
  
@param aGCLog The file that the GC log was written to.  
  
@param aCCLog The file that the CC log was written to.  
  
@param aIsParent indicates whether this log file pair is from the  
parent process.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aGCLog</td>
<td>The file that the GC log was written to.  
</td>
</tr>

<tr>
<td>aCCLog</td>
<td>The file that the CC log was written to.  
</td>
</tr>

<tr>
<td>aIsParent</td>
<td>indicates whether this log file pair is from the  
parent process.  
</td>
</tr>

</table>

### onFinish() ###
<pre>  
Called when GC/CC logging has finished, after all calls to |onDump|.  
  
</pre>