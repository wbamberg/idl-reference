---
layout: default
---

# nsIHTTPHeaderListener #
  
The nsIHTTPHeaderListener interface allows plugin authors to  
access HTTP Response headers after issuing an  
nsIPluginHost::{GetURL,PostURL}() call. <P>  
  

## Methods ##

### newResponseHeader(headerName, headerValue) ###
  
Called for each HTTP Response header.  
NOTE: You must copy the values of the params.    
  

### statusLine(line) ###
  
Called once for the HTTP Response status line.  
Value does NOT include a terminating newline.  
NOTE: You must copy this value.  
  
