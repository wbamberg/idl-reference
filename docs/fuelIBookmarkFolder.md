---
layout: default
---

# fuelIBookmarkFolder #
  
Interface representing a bookmark folder. Folders  
can hold bookmarks, separators and other folders.  
  

## Methods ##

### addBookmark ###
  
Adds a new child bookmark to this folder.  
@param   aTitle  
         The title of bookmark.  
@param   aURI  
         The uri of bookmark.  
  

### addSeparator ###
  
Adds a new child separator to this folder.  
  

### addFolder ###
  
Adds a new child folder to this folder.  
@param   aTitle  
         The title of folder.  
  

### remove ###
  
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
  
