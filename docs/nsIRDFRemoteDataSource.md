---
layout: default
---

# nsIRDFRemoteDataSource #
  
A datasource that may load asynchronously  
  

## Methods ##

### Init(aURI) ###
  
Specify the URI for the data source: this is the prefix  
that will be used to register the data source in the  
data source registry.  
@param aURI the URI to load  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the URI to load  
</td>
</tr>

</table>

### Refresh(aBlocking) ###
  
Refresh the remote datasource, re-loading its contents  
from the URI.  
  
@param aBlocking If <code>true</code>, the call will block  
until the datasource has completely reloaded.  
  

#### Parameters ####

<table>

<tr>
<td>aBlocking</td>
<td>If <code>true</code>, the call will block  
until the datasource has completely reloaded.  
</td>
</tr>

</table>

### Flush() ###
  
Request that a data source write its contents out to   
permanent storage, if applicable.  
  

### FlushTo(aURI) ###

## Attributes ##

### loaded ###
  
This value is <code>true</code> when the datasource has  
fully loaded itself.  
  
