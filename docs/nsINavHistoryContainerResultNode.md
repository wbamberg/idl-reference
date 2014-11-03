---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsINavHistoryService.idl">Source file</a>
</div>

# nsINavHistoryContainerResultNode #
  
Base class for container results. This includes all types of groupings.  
Bookmark folders and places queries will be QueryResultNodes which extends  
these items.  
  

## Methods ##

### getChild(aIndex) ###

### getChildIndex(aNode) ###
  
Get the index of a direct child in this container.  
  
  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>       a result node.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>aNode's index in this container.  
@throws NS_ERROR_NOT_AVAILABLE if containerOpen is false.  
@throws NS_ERROR_INVALID_ARG if aNode isn't a direct child of this  
container.  
</td>
</tr>

</table>

### findNodeByDetails(aURIString, aTime, aItemId, aRecursive) ###
  
Look for a node in the container by some of its details.  Does not search  
closed containers.  
  
  
@throws NS_ERROR_NOT_AVAILABLE if this container is closed.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       the node's uri attribute value  
</td>
</tr>

<tr>
<td>aTime</td>
<td>       the node's time attribute value.  
</td>
</tr>

<tr>
<td>aItemId</td>
<td>       the node's itemId attribute value.  
</td>
</tr>

<tr>
<td>aRecursive</td>
<td>       whether or not to search recursively.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a result node that matches the given details if any, null  
        otherwise.  
</td>
</tr>

</table>

## Attributes ##

### containerOpen ###
  
Set this to allow descent into the container. When closed, attempting  
to call getChildren or childCount will result in an error. You should  
set this to false when you are done reading.  
  
For HOST and DAY groupings, doing this is free since the children have  
been precomputed. For queries and bookmark folders, being open means they  
will keep themselves up-to-date by listening for updates and re-querying  
as needed.  
  

### state ###
  
Indicates whether the container is closed, loading, or opened.  Loading  
implies that the container has been opened asynchronously and has not yet  
fully opened.  
  

### hasChildren ###
  
This indicates whether this node "may" have children, and can be used  
when the container is open or closed. When the container is closed, it  
will give you an exact answer if the node can easily be populated (for  
example, a bookmark folder). If not (for example, a complex history query),  
it will return true. When the container is open, it will always be  
accurate. It is intended to be used to see if we should draw the "+" next  
to a tree item.  
  

### childCount ###
  
This gives you the children of the nodes. It is preferrable to use this  
interface over the array one, since it avoids creating an nsIArray object  
and the interface is already the correct type.  
  
@throws NS_ERROR_NOT_AVAILABLE if containerOpen is false.  
  

## Constants ##

### STATE_CLOSED ###

### STATE_LOADING ###

### STATE_OPENED ###
