---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/modules/libjar/nsIZipReader.idl">Source file</a>
</div>
# nsIZipEntry #

## Attributes ##

### compression ###
  
The type of compression used for the item.  The possible values and  
their meanings are defined in the zip file specification at  
http://www.pkware.com/business_and_developers/developer/appnote/  
  

### size ###
  
The compressed size of the data in the item.  
  

### realSize ###
  
The uncompressed size of the data in the item.  
  

### CRC32 ###
  
The CRC-32 hash of the file in the entry.  
  

### isDirectory ###
  
True if the name of the entry ends with '/' and false otherwise.  
  

### lastModifiedTime ###
  
The time at which this item was last modified.  
  

### isSynthetic ###
  
Use this attribute to determine whether this item is an actual zip entry  
or is one synthesized for part of a real entry's path.  A synthesized  
entry represents a directory within the zip file which has no  
corresponding entry within the zip file.  For example, the entry for the  
directory foo/ in a zip containing exactly one entry for foo/bar.txt  
is synthetic.  If the zip file contains an actual entry for a directory,  
this attribute will be false for the nsIZipEntry for that directory.  
It is impossible for a file to be synthetic.  
  

### permissions ###
  
The UNIX style file permissions of this item.  
  
