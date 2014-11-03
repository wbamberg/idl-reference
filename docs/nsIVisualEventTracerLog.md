---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIVisualEventTracer.idl">Source file</a>
</div>

# nsIVisualEventTracerLog #

## Methods ##

### writeToProfilingFile() ###
<pre>  
Write the JSON string returned by JSONString to the log defined by  
the environment variable MOZ_PROFILING_FILE.  
  
</pre>
## Attributes ##

### JSONString ###
<pre>  
JSON string of the log.  Use JSON.parse to get it as an object.  
  
</pre>