---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsIHttpHeaderVisitor.idl">Source file</a>
</div>

# nsIHttpHeaderVisitor #
<code>  
Implement this interface to visit http headers.  
  
</code>
## Methods ##

### visitHeader(aHeader, aValue) ###
<code>  
Called by the nsIHttpChannel implementation when visiting request and  
response headers.  
  
@param aHeader  
       the header being visited.  
@param aValue  
       the header value (possibly a comma delimited list).  
  
@throw any exception to terminate enumeration  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aHeader</td>
<td>       the header being visited.  
</td>
</tr>

<tr>
<td>aValue</td>
<td>       the header value (possibly a comma delimited list).  
</td>
</tr>

</table>
