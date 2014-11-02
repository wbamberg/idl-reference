---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/crashes/nsICrashService.idl">Source file</a>
</div>
# nsICrashService #

## Methods ##

### addCrash(processType, crashType, id) ###
  
Records the occurrence of a crash.  
  
@param processType  
       One of the PROCESS_TYPE constants defined below.  
@param crashType  
       One of the CRASH_TYPE constants defined below.  
@param id  
       Crash ID. Likely a UUID.  
  

#### Parameters ####

<table>

<tr>
<td>processType</td>
<td>       One of the PROCESS_TYPE constants defined below.  
</td>
</tr>

<tr>
<td>crashType</td>
<td>       One of the CRASH_TYPE constants defined below.  
</td>
</tr>

<tr>
<td>id</td>
<td>       Crash ID. Likely a UUID.  
</td>
</tr>

</table>

## Constants ##

### PROCESS_TYPE_MAIN ###

### PROCESS_TYPE_CONTENT ###

### PROCESS_TYPE_PLUGIN ###

### PROCESS_TYPE_GMPLUGIN ###

### CRASH_TYPE_CRASH ###

### CRASH_TYPE_HANG ###
