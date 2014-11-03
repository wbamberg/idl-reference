---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/osfile/nsINativeOSFileInternals.idl">Source file</a>
</div>

# nsINativeOSFileInternalsService #
<code>  
A service providing native implementations of some of the features  
of OS.File.  
  
</code>
## Methods ##

### read(path, options, onSuccess, onError) ###
<code>  
Implementation of OS.File.read  
  
@param path The absolute path to the file to read.  
@param options An object that may contain some of the following fields  
- {number} bytes The maximal number of bytes to read.  
- {string} encoding If provided, return the result as a string, decoded  
  using this encoding. Otherwise, pass the result as an ArrayBuffer.  
  Invalid encodings cause onError to be called with the platform-specific  
  "invalid argument" constant.  
- {string} compression Unimplemented at the moment.  
@param onSuccess The success callback.  
@param onError The error callback.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>path</td>
<td>The absolute path to the file to read.  
</td>
</tr>

<tr>
<td>options</td>
<td>An object that may contain some of the following fields  
- {number} bytes The maximal number of bytes to read.  
- {string} encoding If provided, return the result as a string, decoded  
  using this encoding. Otherwise, pass the result as an ArrayBuffer.  
  Invalid encodings cause onError to be called with the platform-specific  
  "invalid argument" constant.  
- {string} compression Unimplemented at the moment.  
</td>
</tr>

<tr>
<td>onSuccess</td>
<td>The success callback.  
</td>
</tr>

<tr>
<td>onError</td>
<td>The error callback.  
</td>
</tr>

</table>
