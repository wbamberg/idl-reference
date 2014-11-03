---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/streamconv/public/nsIDirIndexListener.idl">Source file</a>
</div>

# nsIDirIndexListener #
  
This interface is used to receive contents of directory index listings  
from a protocol. They can then be transformed into an output format  
(such as rdf, html, etc)  
  

## Methods ##

### onIndexAvailable(aRequest, aCtxt, aIndex) ###
  
Called for each directory entry  
  
@param request - the request  
@param ctxt - opaque parameter  
@param index - new index to add  
  

#### Parameters ####

<table>

<tr>
<td>request</td>
<td>- the request  
</td>
</tr>

<tr>
<td>ctxt</td>
<td>- opaque parameter  
</td>
</tr>

<tr>
<td>index</td>
<td>- new index to add  
</td>
</tr>

</table>

### onInformationAvailable(aRequest, aCtxt, aInfo) ###
  
Called for each information line  
  
@param request - the request  
@param ctxt - opaque parameter  
@param info - new info to add  
  

#### Parameters ####

<table>

<tr>
<td>request</td>
<td>- the request  
</td>
</tr>

<tr>
<td>ctxt</td>
<td>- opaque parameter  
</td>
</tr>

<tr>
<td>info</td>
<td>- new info to add  
</td>
</tr>

</table>
