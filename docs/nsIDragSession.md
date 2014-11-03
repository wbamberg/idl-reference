---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIDragSession.idl">Source file</a>
</div>

# nsIDragSession #

## Methods ##

### getData(aTransferable, aItemIndex) ###
<pre>  
Get data from a Drag&Drop. Can be called while the drag is in process  
or after the drop has completed.    
  
@param  aTransferable the transferable for the data to be put into  
@param  aItemIndex which of multiple drag items, zero-based  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aTransferable</td>
<td>the transferable for the data to be put into  
</td>
</tr>

<tr>
<td>aItemIndex</td>
<td>which of multiple drag items, zero-based  
</td>
</tr>

</table>

### isDataFlavorSupported(aDataFlavor) ###
<pre>  
Check to set if any of the native data on the clipboard matches this data flavor  
  
</pre>
## Attributes ##

### canDrop ###
<pre>  
Set the current state of the drag, whether it can be dropped or not.  
usually the target "frame" sets this so the native system can render the correct feedback  
  
</pre>
### onlyChromeDrop ###
<pre>  
Indicates if the drop event should be dispatched only to chrome.  
  
</pre>
### dragAction ###
<pre>  
Sets the action (copy, move, link, et.c) for the current drag   
  
</pre>
### targetSize ###
<pre>  
Sets the current width and height of the drag target area.   
It will contain the current size of the Frame that the drag is currently in  
  
</pre>
### numDropItems ###
<pre>  
Get the number of items that were dropped  
  
</pre>
### sourceDocument ###
<pre>  
The document where the drag was started, which will be null if the  
drag originated outside the application. Useful for determining if a drop  
originated in the same document.  
  
</pre>
### sourceNode ###
<pre>  
The dom node that was originally dragged to start the session, which will be null if the  
drag originated outside the application.  
  
</pre>
### dataTransfer ###
<pre>  
The data transfer object for the current drag.  
  
</pre>