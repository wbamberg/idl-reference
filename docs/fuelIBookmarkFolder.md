---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIBookmarkFolder #
  
Interface representing a bookmark folder. Folders  
can hold bookmarks, separators and other folders.  
  

## Methods ##

### addBookmark(aTitle, aURI) ###
  
Adds a new child bookmark to this folder.  
  

#### Parameters ####

<table>

<tr>
<td>aTitle</td>
<td>         The title of bookmark.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>         The uri of bookmark.  
</td>
</tr>

</table>

### addSeparator() ###
  
Adds a new child separator to this folder.  
  

### addFolder(aTitle) ###
  
Adds a new child folder to this folder.  
  

#### Parameters ####

<table>

<tr>
<td>aTitle</td>
<td>         The title of folder.  
</td>
</tr>

</table>

### remove() ###
  
Removes the folder from the parent folder.  
  

## Attributes ##

### id ###
  
The id of the folder.  
  

### title ###
  
The title of the folder.  
  

### description ###
  
The description of the folder.  
  

### type ###
  
The type of the folder.  
values: "folder"  
  

### parent ###
  
The parent folder of the folder.  
  

### annotations ###
  
The annotations object for the folder.  
  

### events ###
  
The events object for the folder.  
supports: "add", "addchild", "remove", "removechild", "change", "move"  
  

### children ###
  
Array of all bookmarks, separators and folders contained  
in this folder.  
  
