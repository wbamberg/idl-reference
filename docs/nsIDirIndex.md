---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/streamconv/public/nsIDirIndex.idl">Source file</a>
</div>

# nsIDirIndex #
 A class holding information about a directory index.  
These have no reference back to their original source -  
changing these attributes won't affect the directory  
  

## Attributes ##

### type ###
  
The type of the entry - one of the constants above  
  

### contentType ###
  
The content type - may be null if it is unknown.  
Unspecified for directories  
  

### location ###
  
The fully qualified filename, expressed as a uri  
  
This is encoded with the encoding specified in  
the nsIDirIndexParser, and is also escaped.  
  

### description ###
  
A description for the filename, which should be  
displayed by a viewer  
  

### size ###
  
File size, with -1 meaning "unknown"  
  

### lastModified ###
  
Last-modified time in seconds-since-epoch.  
-1 means unknown - this is valid, because there were no  
ftp servers in 1969  
  

## Constants ##

### TYPE_UNKNOWN ###
  
Entry's type is unknown  
  

### TYPE_DIRECTORY ###
  
Entry is a directory  
  

### TYPE_FILE ###
  
Entry is a file  
  

### TYPE_SYMLINK ###
  
Entry is a symlink  
  
