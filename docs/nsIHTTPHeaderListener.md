---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/plugins/base/nsIHTTPHeaderListener.idl">Source file</a>
</div>

# nsIHTTPHeaderListener #
<pre>  
The nsIHTTPHeaderListener interface allows plugin authors to  
access HTTP Response headers after issuing an  
nsIPluginHost::{GetURL,PostURL}() call. <P>  
  
</pre>
## Methods ##

### newResponseHeader(headerName, headerValue) ###
<pre>  
Called for each HTTP Response header.  
NOTE: You must copy the values of the params.    
  
</pre>
### statusLine(line) ###
<pre>  
Called once for the HTTP Response status line.  
Value does NOT include a terminating newline.  
NOTE: You must copy this value.  
  
</pre>