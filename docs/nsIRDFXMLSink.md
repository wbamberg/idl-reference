---
layout: default
---

# nsIRDFXMLSink #
  
A "sink" that receives and processes RDF/XML. This interface is used  
by the RDF/XML parser.  
  

## Methods ##

### beginLoad ###
  
Initiate the RDF/XML load.  
  

### interrupt ###
  
Suspend the RDF/XML load.  
  

### resume ###
  
Resume the RDF/XML load.  
  

### endLoad ###
  
Complete the RDF/XML load.  
  

### addNameSpace ###
  
Add namespace information to the RDF/XML sink.  
@param aPrefix the namespace prefix  
@param aURI the namespace URI  
  

### addXMLSinkObserver ###
  
Add an observer that will be notified as the RDF/XML load  
progresses.  
<p>  
  
Note that the sink will acquire a strong reference to the  
observer, so care should be taken to avoid cyclical references  
that cannot be released (i.e., if the observer holds a  
reference to the sink, it should be sure that it eventually  
clears the reference).  
  
@param aObserver the observer to add to the sink's set of  
load observers.  
  

### removeXMLSinkObserver ###
  
Remove an observer from the sink's set of observers.  
@param aObserver the observer to remove.  
  

## Attributes ##

### readOnly ###
  
Set to <code>true</code> if the sink is read-only and cannot  
be modified  
  
