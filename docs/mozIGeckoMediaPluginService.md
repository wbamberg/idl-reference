---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/media/gmp/mozIGeckoMediaPluginService.idl">Source file</a>
</div>

# mozIGeckoMediaPluginService #

## Methods ##

### hasPluginForAPI(api, tags) ###
<code>  
Get a plugin that supports the specified tags.  
Callable on any thread  
  
</code>
### getGMPVideoDecoder(tags, nodeId, outVideoHost) ###
<code>  
Get a video decoder that supports the specified tags.  
The array of tags should at least contain a codec tag, and optionally  
other tags such as for EME keysystem.  
Callable only on GMP thread.  
  
</code>
### getGMPVideoEncoder(tags, nodeId, outVideoHost) ###
<code>  
Get a video encoder that supports the specified tags.  
The array of tags should at least contain a codec tag, and optionally  
other tags.  
Callable only on GMP thread.  
  
</code>
### getGMPAudioDecoder(tags, nodeId) ###

### getGMPDecryptor(tags, nodeId) ###

### addPluginDirectory(directory) ###
<code>  
Add a directory to scan for gecko media plugins.  
@note Main-thread API.  
  
</code>
### removePluginDirectory(directory) ###
<code>  
Remove a directory for gecko media plugins.  
@note Main-thread API.  
  
</code>
### getNodeId(origin, topLevelOrigin, inPrivateBrowsingMode) ###
<code>  
Gets the NodeId for a (origin, urlbarOrigin, isInprivateBrowsing) tuple.  
  
</code>
### isPersistentStorageAllowed(nodeId) ###
<code>  
Returns true if the given node id is allowed to store things  
persistently on disk. Private Browsing and local content are not  
allowed to store persistent data.  
  
</code>
### getStorageDir() ###
<code>  
Returns the directory to use as the base for storing data about GMPs.  
  
</code>
## Attributes ##

### thread ###
  
The GMP thread. Callable from any thread.  
  
