---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/threads/nsIThreadManager.idl">Source file</a>
</div>

# nsIThreadManager #
<pre>  
An interface for creating and locating nsIThread instances.  
  
</pre>
## Methods ##

### newThread(creationFlags, stackSize) ###
<pre>  
Create a new thread (a global, user PRThread).  
  
@param creationFlags  
  Reserved for future use.  Pass 0.  
@param stackSize  
  Number of bytes to reserve for the thread's stack.  
  
@returns  
  The newly created nsIThread object.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>creationFlags</td>
<td>  Reserved for future use.  Pass 0.  
</td>
</tr>

<tr>
<td>stackSize</td>
<td>  Number of bytes to reserve for the thread's stack.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>  The newly created nsIThread object.  
</td>
</tr>

</table>

### getThreadFromPRThread(prthread) ###
<pre>  
Get the nsIThread object (if any) corresponding to the given PRThread.  
This method returns null if there is no corresponding nsIThread.  
  
@param prthread  
  The PRThread of the nsIThread being requested.  
  
@returns  
  The nsIThread object corresponding to the given PRThread or null if no  
  such nsIThread exists.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>prthread</td>
<td>  The PRThread of the nsIThread being requested.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>  The nsIThread object corresponding to the given PRThread or null if no  
  such nsIThread exists.  
</td>
</tr>

</table>

## Attributes ##

### mainThread ###
<pre>  
Get the main thread.  
  
</pre>
### currentThread ###
<pre>  
Get the current thread.  If the calling thread does not already have a  
nsIThread associated with it, then a new nsIThread will be created and  
associated with the current PRThread.  
  
</pre>
### isMainThread ###
<pre>  
This attribute is true if the calling thread is the main thread of the  
application process.  
  
</pre>
## Constants ##

### DEFAULT_STACK_SIZE ###
<pre>  
Default number of bytes reserved for a thread's stack, if no stack size  
is specified in newThread(). 0 means use platform default.  
  
</pre>