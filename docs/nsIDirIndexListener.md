---
layout: default
---

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
<td>request</td>
<td>- the request  
</td>
</tr>

<tr>
<td>request</td>
<td>- the request  
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
<td>request</td>
<td>- the request  
</td>
</tr>

<tr>
<td>request</td>
<td>- the request  
</td>
</tr>

</table>
