---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/modules/libjar/nsIZipReader.idl">Source file</a>
</div>

# nsIZipEntry #

## Attributes ##

### compression ###
<pre>  
The type of compression used for the item.  The possible values and  
their meanings are defined in the zip file specification at  
http://www.pkware.com/business_and_developers/developer/appnote/  
  
</pre>
### size ###
<pre>  
The compressed size of the data in the item.  
  
</pre>
### realSize ###
<pre>  
The uncompressed size of the data in the item.  
  
</pre>
### CRC32 ###
<pre>  
The CRC-32 hash of the file in the entry.  
  
</pre>
### isDirectory ###
<pre>  
True if the name of the entry ends with '/' and false otherwise.  
  
</pre>
### lastModifiedTime ###
<pre>  
The time at which this item was last modified.  
  
</pre>
### isSynthetic ###
<pre>  
Use this attribute to determine whether this item is an actual zip entry  
or is one synthesized for part of a real entry's path.  A synthesized  
entry represents a directory within the zip file which has no  
corresponding entry within the zip file.  For example, the entry for the  
directory foo/ in a zip containing exactly one entry for foo/bar.txt  
is synthetic.  If the zip file contains an actual entry for a directory,  
this attribute will be false for the nsIZipEntry for that directory.  
It is impossible for a file to be synthetic.  
  
</pre>
### permissions ###
<pre>  
The UNIX style file permissions of this item.  
  
</pre>