---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/threads/nsIProcess.idl">Source file</a>
</div>

# nsIProcess #

## Methods ##

### init(executable) ###
<code>  
Initialises the process with an executable to be run. Call the run method  
to run the executable.  
@param executable The executable to run.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>executable</td>
<td>The executable to run.  
</td>
</tr>

</table>

### kill() ###
<code>  
Kills the running process. After exiting the process will either have  
been killed or a failure will have been returned.  
  
</code>
### run(blocking, args, count) ###
<code>  
Executes the file this object was initialized with  
@param blocking   Whether to wait until the process terminates before  
returning or not.  
@param args       An array of arguments to pass to the process in the  
                  native character set.  
@param count      The length of the args array.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>blocking</td>
<td>Whether to wait until the process terminates before  
returning or not.  
</td>
</tr>

<tr>
<td>args</td>
<td>An array of arguments to pass to the process in the  
                  native character set.  
</td>
</tr>

<tr>
<td>count</td>
<td>The length of the args array.  
</td>
</tr>

</table>

### runAsync(args, count, observer, holdWeak) ###
<code>  
Executes the file this object was initialized with optionally calling  
an observer after the process has finished running.  
@param args       An array of arguments to pass to the process in the  
                  native character set.  
@param count      The length of the args array.  
@param observer   An observer to notify when the process has completed. It  
                  will receive this process instance as the subject and  
                  "process-finished" or "process-failed" as the topic. The  
                  observer will be notified on the main thread.  
@param holdWeak   Whether to use a weak reference to hold the observer.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>args</td>
<td>An array of arguments to pass to the process in the  
                  native character set.  
</td>
</tr>

<tr>
<td>count</td>
<td>The length of the args array.  
</td>
</tr>

<tr>
<td>observer</td>
<td>An observer to notify when the process has completed. It  
                  will receive this process instance as the subject and  
                  "process-finished" or "process-failed" as the topic. The  
                  observer will be notified on the main thread.  
</td>
</tr>

<tr>
<td>holdWeak</td>
<td>Whether to use a weak reference to hold the observer.  
</td>
</tr>

</table>

### runw(blocking, args, count) ###
<code>  
Executes the file this object was initialized with  
@param blocking   Whether to wait until the process terminates before  
returning or not.  
@param args       An array of arguments to pass to the process in UTF-16  
@param count      The length of the args array.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>blocking</td>
<td>Whether to wait until the process terminates before  
returning or not.  
</td>
</tr>

<tr>
<td>args</td>
<td>An array of arguments to pass to the process in UTF-16  
</td>
</tr>

<tr>
<td>count</td>
<td>The length of the args array.  
</td>
</tr>

</table>

### runwAsync(args, count, observer, holdWeak) ###
<code>  
Executes the file this object was initialized with optionally calling  
an observer after the process has finished running.  
@param args       An array of arguments to pass to the process in UTF-16  
@param count      The length of the args array.  
@param observer   An observer to notify when the process has completed. It  
                  will receive this process instance as the subject and  
                  "process-finished" or "process-failed" as the topic. The  
                  observer will be notified on the main thread.  
@param holdWeak   Whether to use a weak reference to hold the observer.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>args</td>
<td>An array of arguments to pass to the process in UTF-16  
</td>
</tr>

<tr>
<td>count</td>
<td>The length of the args array.  
</td>
</tr>

<tr>
<td>observer</td>
<td>An observer to notify when the process has completed. It  
                  will receive this process instance as the subject and  
                  "process-finished" or "process-failed" as the topic. The  
                  observer will be notified on the main thread.  
</td>
</tr>

<tr>
<td>holdWeak</td>
<td>Whether to use a weak reference to hold the observer.  
</td>
</tr>

</table>

## Attributes ##

### pid ###
  
The process identifier of the currently running process. This will only  
be available after the process has started and may not be available on  
some platforms.  
  

### exitValue ###
  
The exit value of the process. This is only valid after the process has  
exited.  
  

### isRunning ###
  
Returns whether the process is currently running or not.  
  
