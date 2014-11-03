---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/modules/libjar/nsIZipReader.idl">Source file</a>
</div>

# nsIZipReaderCache #

## Methods ##

### init(cacheSize) ###
<pre>  
Initializes a new zip reader cache.   
@param cacheSize - the number of released entries to maintain before  
  beginning to throw some out (note that the number of outstanding  
  entries can be much greater than this number -- this is the count  
  for those otherwise unused entries)  
  
</pre>
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
<pre>  
Returns a (possibly shared) nsIZipReader for an nsIFile.  
  
If the zip reader for given file is not in the cache, a new zip reader  
is created, initialized, and opened (see nsIZipReader::init and   
nsIZipReader::open). Otherwise the previously created zip reader is   
returned.  
  
@note If someone called close() on the shared nsIZipReader, this method   
      will return the closed zip reader.  
  
</pre>
### isCached(zipFile) ###
<pre>  
returns true if this zipreader already has this file cached  
  
</pre>
### getInnerZip(zipFile, zipEntry) ###
<pre>  
Returns a (possibly shared) nsIZipReader for a zip inside another zip  
  
See getZip  
  
</pre>
### setMustCacheFd(zipFile, aMustCacheFd) ###
<pre>  
Whether to keep NSPR file descriptor for newly opened files in the cache.  
When aMustCacheFd is enabled and a file is given, the file will be flushed  
from the cache if its file descriptor was not cached.  
Note: currently not supported on Windows platform.  
  
</pre>
### getFd(zipFile) ###
<pre>  
Returns the cached NSPR file descriptor of the file.  
Note: currently not supported on Windows platform.  
  
</pre>