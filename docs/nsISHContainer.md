---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHContainer.idl">Source file</a>
</div>

# nsISHContainer #
  
The nsISHEntryContainer. The interface to access child entries  
of an nsISHEntry.  
  
  

## Methods ##

### AddChild(child, offset) ###
  
Add a new child SHEntry.  If offset is -1 adds to the end of the list.  
  

### RemoveChild(child) ###
  
Removes a child SHEntry  
  

### GetChildAt(index) ###
  
Get child at an index  
  

## Attributes ##

### childCount ###
  
The current number of nsISHEntries which are immediate children of the   
current SHEntry  
  
