---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/modules/libjar/nsIZipReader.idl">Source file</a>
</div>

# nsIZipReaderCache #

## Methods ##

### init(cacheSize) ###
<code>  
Initializes a new zip reader cache.   
@param cacheSize - the number of released entries to maintain before  
  beginning to throw some out (note that the number of outstanding  
  entries can be much greater than this number -- this is the count  
  for those otherwise unused entries)  
  
</code>
#### Parameters ####

<table>

<tr>
<td>cacheSize</td>
<td>- the number of released entries to maintain before  
  beginning to throw some out (note that the number of outstanding  
  entries can be much greater than this number -- this is the count  
  for those otherwise unused entries)  
</td>
</tr>

</table>

### getZip(zipFile) ###
<code>  
Returns a (possibly shared) nsIZipReader for an nsIFile.  
  
If the zip reader for given file is not in the cache, a new zip reader  
is created, initialized, and opened (see nsIZipReader::init and   
nsIZipReader::open). Otherwise the previously created zip reader is   
returned.  
  
@note If someone called close() on the shared nsIZipReader, this method   
      will return the closed zip reader.  
  
</code>
### isCached(zipFile) ###
<code>  
returns true if this zipreader already has this file cached  
  
</code>
### getInnerZip(zipFile, zipEntry) ###
<code>  
Returns a (possibly shared) nsIZipReader for a zip inside another zip  
  
See getZip  
  
</code>
### setMustCacheFd(zipFile, aMustCacheFd) ###
<code>  
Whether to keep NSPR file descriptor for newly opened files in the cache.  
When aMustCacheFd is enabled and a file is given, the file will be flushed  
from the cache if its file descriptor was not cached.  
Note: currently not supported on Windows platform.  
  
</code>
### getFd(zipFile) ###
<code>  
Returns the cached NSPR file descriptor of the file.  
Note: currently not supported on Windows platform.  
  
</code>