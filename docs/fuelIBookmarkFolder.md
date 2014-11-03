---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIBookmarkFolder #
<pre>  
Interface representing a bookmark folder. Folders  
can hold bookmarks, separators and other folders.  
  
</pre>
## Methods ##

### addBookmark(aTitle, aURI) ###
<pre>  
Adds a new child bookmark to this folder.  
@param   aTitle  
         The title of bookmark.  
@param   aURI  
         The uri of bookmark.  
  
</pre>
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
<pre>  
Adds a new child separator to this folder.  
  
</pre>
### addFolder(aTitle) ###
<pre>  
Adds a new child folder to this folder.  
@param   aTitle  
         The title of folder.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aTitle</td>
<td>         The title of folder.  
</td>
</tr>

</table>

### remove() ###
<pre>  
Removes the folder from the parent folder.  
  
</pre>
## Attributes ##

### id ###
<pre>  
The id of the folder.  
  
</pre>
### title ###
<pre>  
The title of the folder.  
  
</pre>
### description ###
<pre>  
The description of the folder.  
  
</pre>
### type ###
<pre>  
The type of the folder.  
values: "folder"  
  
</pre>
### parent ###
<pre>  
The parent folder of the folder.  
  
</pre>
### annotations ###
<pre>  
The annotations object for the folder.  
  
</pre>
### events ###
<pre>  
The events object for the folder.  
supports: "add", "addchild", "remove", "removechild", "change", "move"  
  
</pre>
### children ###
<pre>  
Array of all bookmarks, separators and folders contained  
in this folder.  
  
</pre>