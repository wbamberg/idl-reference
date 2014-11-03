---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/streamconv/public/nsIDirIndex.idl">Source file</a>
</div>

# nsIDirIndex #
<pre> A class holding information about a directory index.  
These have no reference back to their original source -  
changing these attributes won't affect the directory  
  
</pre>
## Attributes ##

### type ###
<pre>  
The type of the entry - one of the constants above  
  
</pre>
### contentType ###
<pre>  
The content type - may be null if it is unknown.  
Unspecified for directories  
  
</pre>
### location ###
<pre>  
The fully qualified filename, expressed as a uri  
  
This is encoded with the encoding specified in  
the nsIDirIndexParser, and is also escaped.  
  
</pre>
### description ###
<pre>  
A description for the filename, which should be  
displayed by a viewer  
  
</pre>
### size ###
<pre>  
File size, with -1 meaning "unknown"  
  
</pre>
### lastModified ###
<pre>  
Last-modified time in seconds-since-epoch.  
-1 means unknown - this is valid, because there were no  
ftp servers in 1969  
  
</pre>
## Constants ##

### TYPE_UNKNOWN ###
<pre>  
Entry's type is unknown  
  
</pre>
### TYPE_DIRECTORY ###
<pre>  
Entry is a directory  
  
</pre>
### TYPE_FILE ###
<pre>  
Entry is a file  
  
</pre>
### TYPE_SYMLINK ###
<pre>  
Entry is a symlink  
  
</pre>