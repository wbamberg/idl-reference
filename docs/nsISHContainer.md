---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHContainer.idl">Source file</a>
</div>

# nsISHContainer #
<code>  
The nsISHEntryContainer. The interface to access child entries  
of an nsISHEntry.  
  
  
</code>
## Methods ##

### AddChild(child, offset) ###
<code>  
Add a new child SHEntry.  If offset is -1 adds to the end of the list.  
  
</code>
### RemoveChild(child) ###
<code>  
Removes a child SHEntry  
  
</code>
### GetChildAt(index) ###
<code>  
Get child at an index  
  
</code>
## Attributes ##

### childCount ###
  
The current number of nsISHEntries which are immediate children of the   
current SHEntry  
  
