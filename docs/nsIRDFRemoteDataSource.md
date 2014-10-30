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
  

### Refresh(aBlocking) ###
  
Refresh the remote datasource, re-loading its contents  
from the URI.  
  
@param aBlocking If <code>true</code>, the call will block  
until the datasource has completely reloaded.  
  

### Flush() ###
  
Request that a data source write its contents out to   
permanent storage, if applicable.  
  

### FlushTo(aURI) ###

## Attributes ##

### loaded ###
  
This value is <code>true</code> when the datasource has  
fully loaded itself.  
  
