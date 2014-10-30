---
layout: default
---

# nsIRDFXMLSinkObserver #
  
An observer that is notified as progress is made on the load  
of an RDF/XML document in an <code>nsIRDFXMLSink</code>.  
  

## Methods ##

### onBeginLoad ###
  
Called when the load begins.  
@param aSink the RDF/XML sink on which the load is beginning.  
  

### onInterrupt ###
  
Called when the load is suspended (e.g., for network quantization).  
@param aSink the RDF/XML sink that is being interrupted.  
  

### onResume ###
  
Called when a suspended load is resuming.  
@param aSink the RDF/XML sink that is resuming.  
  

### onEndLoad ###
  
Called when an RDF/XML load completes successfully.  
@param aSink the RDF/XML sink that has finished loading.  
  

### onError ###
  
Called when an error occurs during the load  
@param aSink the RDF/XML sink in which the error occurred  
@param aStatus the networking result code  
@param aErrorMsg an error message, if applicable  
  
