---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIDragSession.idl">Source file</a>
</div>

# nsIDragSession #

## Methods ##

### getData(aTransferable, aItemIndex) ###
  
Get data from a Drag&Drop. Can be called while the drag is in process  
or after the drop has completed.    
  
@param  aTransferable the transferable for the data to be put into  
@param  aItemIndex which of multiple drag items, zero-based  
  

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
  
Check to set if any of the native data on the clipboard matches this data flavor  
  

## Attributes ##

### canDrop ###
  
Set the current state of the drag, whether it can be dropped or not.  
usually the target "frame" sets this so the native system can render the correct feedback  
  

### onlyChromeDrop ###
  
Indicates if the drop event should be dispatched only to chrome.  
  

### dragAction ###
  
Sets the action (copy, move, link, et.c) for the current drag   
  

### targetSize ###
  
Sets the current width and height of the drag target area.   
It will contain the current size of the Frame that the drag is currently in  
  

### numDropItems ###
  
Get the number of items that were dropped  
  

### sourceDocument ###
  
The document where the drag was started, which will be null if the  
drag originated outside the application. Useful for determining if a drop  
originated in the same document.  
  

### sourceNode ###
  
The dom node that was originally dragged to start the session, which will be null if the  
drag originated outside the application.  
  

### dataTransfer ###
  
The data transfer object for the current drag.  
  
