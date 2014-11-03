---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIAsyncLivemarks.idl">Source file</a>
</div>

# mozILivemark #

## Methods ##

### reload(aForceUpdate) ###
  
Reload livemark contents if they are expired or if forced to do so.  
  
  
@note The update process is asynchronous, it's possible to register a  
      result observer to be notified of updated contents through  
      registerForUpdates.  
  

#### Parameters ####

<table>

<tr>
<td>[optional]aForceUpdate</td>
<td>       If set to true forces a reload even if contents are still valid.  
</td>
</tr>

</table>

### getNodesForContainer(aContainerNode) ###
  
Returns an array of nsINavHistoryResultNode objects, representing children  
of this livemark.  The nodes will have aContainerNode as parent.  
  
  

#### Parameters ####

<table>

<tr>
<td>aContainerNode</td>
<td>       Object implementing nsINavHistoryContainerResultNode, to be used as  
       parent of the livemark nodes.  
</td>
</tr>

</table>

### registerForUpdates(aContainerNode, aResultObserver) ###
  
Registers a container node for updates on this livemark.  
When the livemark contents change, an invalidateContainer(aContainerNode)  
request is sent to aResultObserver.  
  
  

#### Parameters ####

<table>

<tr>
<td>aContainerNode</td>
<td>       Object implementing nsINavHistoryContainerResultNode, representing  
       this livemark.  
</td>
</tr>

<tr>
<td>aResultObserver</td>
<td>       The nsINavHistoryResultObserver that should be notified of changes  
       to the livemark contents.  
</td>
</tr>

</table>

### unregisterForUpdates(aContainerNode) ###
  
Unregisters a previously registered container node.  
  
  
@note it's suggested to always unregister containers that are no more used,  
      to free up the associated resources.  A good time to do so is when  
      the container gets closed.  
  

#### Parameters ####

<table>

<tr>
<td>aContainerNode</td>
<td>       Object implementing nsINavHistoryContainerResultNode, representing  
       this livemark.  
</td>
</tr>

</table>

## Attributes ##

### status ###
  
Status of this livemark.  One of the STATUS_* constants above.  
  

## Constants ##

### STATUS_READY ###

### STATUS_LOADING ###

### STATUS_FAILED ###
