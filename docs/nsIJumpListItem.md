---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIJumpListItem.idl">Source file</a>
</div>

# nsIJumpListItem #
<code>  
Implements Win7 Taskbar jump list item interfaces.  
  
Note to consumers: it's reasonable to expect we'll need support for other types  
of jump list items (an audio file, an email message, etc.). To add types,  
create the specific interface here, add an implementation class to WinJumpListItem,  
and add support to addListBuild & removed items processing.  
  
  
</code>
## Methods ##

### equals(item) ###
<code>  
Compare this item to another.  
  
Compares the type and other properties specific to this item's  
type.  
  
separator: type  
link: type, uri, title  
shortcut: type, handler app  
  
</code>
## Attributes ##

### type ###
  
Retrieves the jump list item type.  
  

## Constants ##

### JUMPLIST_ITEM_EMPTY ###

### JUMPLIST_ITEM_SEPARATOR ###

### JUMPLIST_ITEM_LINK ###

### JUMPLIST_ITEM_SHORTCUT ###
