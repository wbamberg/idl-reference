---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIBookmark #
  
Interface representing a bookmark item.  
  

## Methods ##

### remove() ###
  
Removes the item from the parent folder. Used to  
delete a bookmark or separator  
  

## Attributes ##

### id ###
  
The id of the bookmark.  
  

### title ###
  
The title of the bookmark.  
  

### uri ###
  
The uri of the bookmark.  
  

### description ###
  
The description of the bookmark.  
  

### keyword ###
  
The keyword associated with the bookmark.  
  

### type ###
  
The type of the bookmark.  
values: "bookmark", "separator"  
  

### parent ###
  
The parent folder of the bookmark.  
  

### annotations ###
  
The annotations object for the bookmark.  
  

### events ###
  
The events object for the bookmark.  
supports: "remove", "change", "visit", "move"  
  
