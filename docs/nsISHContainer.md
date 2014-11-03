---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHContainer.idl">Source file</a>
</div>

# nsISHContainer #
<pre>  
The nsISHEntryContainer. The interface to access child entries  
of an nsISHEntry.  
  
  
</pre>
## Methods ##

### AddChild(child, offset) ###
<pre>  
Add a new child SHEntry.  If offset is -1 adds to the end of the list.  
  
</pre>
### RemoveChild(child) ###
<pre>  
Removes a child SHEntry  
  
</pre>
### GetChildAt(index) ###
<pre>  
Get child at an index  
  
</pre>
## Attributes ##

### childCount ###
<pre>  
The current number of nsISHEntries which are immediate children of the   
current SHEntry  
  
</pre>