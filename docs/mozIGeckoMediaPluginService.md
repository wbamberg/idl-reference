---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/media/gmp/mozIGeckoMediaPluginService.idl">Source file</a>
</div>

# mozIGeckoMediaPluginService #

## Methods ##

### hasPluginForAPI(api, tags) ###
<pre>  
Get a plugin that supports the specified tags.  
Callable on any thread  
  
</pre>
### getGMPVideoDecoder(tags, nodeId, outVideoHost) ###
<pre>  
Get a video decoder that supports the specified tags.  
The array of tags should at least contain a codec tag, and optionally  
other tags such as for EME keysystem.  
Callable only on GMP thread.  
  
</pre>
### getGMPVideoEncoder(tags, nodeId, outVideoHost) ###
<pre>  
Get a video encoder that supports the specified tags.  
The array of tags should at least contain a codec tag, and optionally  
other tags.  
Callable only on GMP thread.  
  
</pre>
### getGMPAudioDecoder(tags, nodeId) ###

### getGMPDecryptor(tags, nodeId) ###

### addPluginDirectory(directory) ###
<pre>  
Add a directory to scan for gecko media plugins.  
@note Main-thread API.  
  
</pre>
### removePluginDirectory(directory) ###
<pre>  
Remove a directory for gecko media plugins.  
@note Main-thread API.  
  
</pre>
### getNodeId(origin, topLevelOrigin, inPrivateBrowsingMode) ###
<pre>  
Gets the NodeId for a (origin, urlbarOrigin, isInprivateBrowsing) tuple.  
  
</pre>
### isPersistentStorageAllowed(nodeId) ###
<pre>  
Returns true if the given node id is allowed to store things  
persistently on disk. Private Browsing and local content are not  
allowed to store persistent data.  
  
</pre>
### getStorageDir() ###
<pre>  
Returns the directory to use as the base for storing data about GMPs.  
  
</pre>
## Attributes ##

### thread ###
<pre>  
The GMP thread. Callable from any thread.  
  
</pre>