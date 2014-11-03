---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIBookmark #
<pre>  
Interface representing a bookmark item.  
  
</pre>
## Methods ##

### remove() ###
<pre>  
Removes the item from the parent folder. Used to  
delete a bookmark or separator  
  
</pre>
## Attributes ##

### id ###
<pre>  
The id of the bookmark.  
  
</pre>
### title ###
<pre>  
The title of the bookmark.  
  
</pre>
### uri ###
<pre>  
The uri of the bookmark.  
  
</pre>
### description ###
<pre>  
The description of the bookmark.  
  
</pre>
### keyword ###
<pre>  
The keyword associated with the bookmark.  
  
</pre>
### type ###
<pre>  
The type of the bookmark.  
values: "bookmark", "separator"  
  
</pre>
### parent ###
<pre>  
The parent folder of the bookmark.  
  
</pre>
### annotations ###
<pre>  
The annotations object for the bookmark.  
  
</pre>
### events ###
<pre>  
The events object for the bookmark.  
supports: "remove", "change", "visit", "move"  
  
</pre>