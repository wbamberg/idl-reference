---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIRequestObserverProxy.idl">Source file</a>
</div>

# nsIRequestObserverProxy #
  
A request observer proxy is used to ship data over to another thread  
specified by the thread's dispatch target. The "true" request observer's  
methods are invoked on the other thread.  
  
This interface only provides the initialization needed after construction.  
Otherwise, these objects are used simply as nsIRequestObserver's.  
  

## Methods ##

### init(observer, context) ###
  
Initializes an nsIRequestObserverProxy.  
  
@param observer - receives observer notifications on the main thread  
@param context  - the context argument that will be passed to OnStopRequest  
                  and OnStartRequest. This has to be stored permanently on  
                  initialization because it sometimes can't be  
                  AddRef/Release'd off-main-thread.  
  

#### Parameters ####

<table>

<tr>
<td>observer</td>
<td>- receives observer notifications on the main thread  
</td>
</tr>

<tr>
<td>context</td>
<td>- the context argument that will be passed to OnStopRequest  
                  and OnStartRequest. This has to be stored permanently on  
                  initialization because it sometimes can't be  
                  AddRef/Release'd off-main-thread.  
</td>
</tr>

</table>
