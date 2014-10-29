---
layout: default
---

# nsIRDFXMLParser #

## parseAsync ##

Create a stream listener that can be used to asynchronously
parse RDF/XML.
@param aSink the RDF datasource the will receive the data
@param aBaseURI the base URI used to resolve relative
  references in the RDF/XML
@return an nsIStreamListener object to handle the data


## parseString ##

Parse a string of RDF/XML
@param aSink the RDF datasource that will receive the data
@param aBaseURI the base URI used to resolve relative
  references in the RDF/XML
@param aSource a UTF8 string containing RDF/XML data.

