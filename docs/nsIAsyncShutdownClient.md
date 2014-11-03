---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/asyncshutdown/nsIAsyncShutdown.idl">Source file</a>
</div>

# nsIAsyncShutdownClient #
<code>  
A client for a nsIAsyncShutdownBarrier.  
  
</code>
## Methods ##

### addBlocker(aBlocker, aFileName, aLineNumber, aStack) ###
<code>  
Add a blocker.  
  
After a `blocker` has been added with `addBlocker`, if it is not  
removed with `removeBlocker`, this will, by design, eventually  
CAUSE A CRASH.  
  
Calling `addBlocker` once nsIAsyncShutdownBarrier::wait() has been  
called on the owning barrier returns an error.  
  
@param aBlocker The blocker to add. Once  
nsIAsyncShutdownBarrier::wait() has been called, it will not  
call its `aOnReady` callback until all blockers have been  
removed, each  by a call to `removeBlocker`.  
@param aFileName The filename of the callsite, as given by `__FILE__`.  
@param aLineNumber The linenumber of the callsite, as given by `__LINE__`.  
@param aStack Information on the stack that lead to this call. Generally  
empty when called from C++.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aBlocker</td>
<td>The blocker to add. Once  
nsIAsyncShutdownBarrier::wait() has been called, it will not  
call its `aOnReady` callback until all blockers have been  
removed, each  by a call to `removeBlocker`.  
</td>
</tr>

<tr>
<td>aFileName</td>
<td>The filename of the callsite, as given by `__FILE__`.  
</td>
</tr>

<tr>
<td>aLineNumber</td>
<td>The linenumber of the callsite, as given by `__LINE__`.  
</td>
</tr>

<tr>
<td>aStack</td>
<td>Information on the stack that lead to this call. Generally  
empty when called from C++.  
</td>
</tr>

</table>

### removeBlocker(aBlocker) ###
<code>  
Remove a blocker.  
  
@param aBlocker A blocker previously added to this client through  
`addBlocker`. Noop if the blocker has never been added or has been  
removed already.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aBlocker</td>
<td>A blocker previously added to this client through  
`addBlocker`. Noop if the blocker has never been added or has been  
removed already.  
</td>
</tr>

</table>

## Attributes ##

### name ###
  
The name of the barrier.  
  

### jsclient ###
  
The JS implementation of the client.  
  
It is strongly recommended that JS clients of this API use  
`jsclient` instead of the `nsIAsyncShutdownClient`. See  
AsyncShutdown.jsm for more information on the JS version of  
this API.  
  
