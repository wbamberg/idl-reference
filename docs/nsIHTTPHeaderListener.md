---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/plugins/base/nsIHTTPHeaderListener.idl">Source file</a>
</div>

# nsIHTTPHeaderListener #
<code>  
The nsIHTTPHeaderListener interface allows plugin authors to  
access HTTP Response headers after issuing an  
nsIPluginHost::{GetURL,PostURL}() call. <P>  
  
</code>
## Methods ##

### newResponseHeader(headerName, headerValue) ###
<code>  
Called for each HTTP Response header.  
NOTE: You must copy the values of the params.    
  
</code>
### statusLine(line) ###
<code>  
Called once for the HTTP Response status line.  
Value does NOT include a terminating newline.  
NOTE: You must copy this value.  
  
</code>