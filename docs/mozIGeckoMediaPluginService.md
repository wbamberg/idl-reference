---
layout: default
---

# mozIGeckoMediaPluginService #

## Methods ##

### hasPluginForAPI(api, tags) ###
  
Get a plugin that supports the specified tags.  
Callable on any thread  
  

### getGMPVideoDecoder(tags, nodeId, outVideoHost) ###
  
Get a video decoder that supports the specified tags.  
The array of tags should at least contain a codec tag, and optionally  
other tags such as for EME keysystem.  
Callable only on GMP thread.  
  

### getGMPVideoEncoder(tags, nodeId, outVideoHost) ###
  
Get a video encoder that supports the specified tags.  
The array of tags should at least contain a codec tag, and optionally  
other tags.  
Callable only on GMP thread.  
  

### getGMPAudioDecoder(tags, nodeId) ###

### getGMPDecryptor(tags, nodeId) ###

### addPluginDirectory(directory) ###
  
Add a directory to scan for gecko media plugins.  
@note Main-thread API.  
  

### removePluginDirectory(directory) ###
  
Remove a directory for gecko media plugins.  
@note Main-thread API.  
  

### getNodeId(origin, topLevelOrigin, inPrivateBrowsingMode) ###
  
Gets the NodeId for a (origin, urlbarOrigin, isInprivateBrowsing) tuple.  
  

### isPersistentStorageAllowed(nodeId) ###
  
Returns true if the given node id is allowed to store things  
persistently on disk. Private Browsing and local content are not  
allowed to store persistent data.  
  

### getStorageDir() ###
  
Returns the directory to use as the base for storing data about GMPs.  
  

## Attributes ##

### thread ###
  
The GMP thread. Callable from any thread.  
  
