---
layout: default
---

# nsIExpatSink #
  
This interface should be implemented by any content sink that wants  
to get output from expat and do something with it; in other words,  
by any sink that handles some sort of XML dialect.  
  

## Methods ##

### HandleStartElement(aName, aAtts, aAttsCount, aLineNumber) ###
  
Called to handle the opening tag of an element.  
@param aName the fully qualified tagname of the element  
@param aAtts the array of attribute names and values.  There are  
       aAttsCount/2 names and aAttsCount/2 values, so the total number of  
       elements in the array is aAttsCount.  The names and values  
       alternate.  Thus, if we number attributes starting with 0,  
       aAtts[2*k] is the name of the k-th attribute and aAtts[2*k+1] is  
       the value of that attribute  Both explicitly specified attributes  
       and attributes that are defined to have default values in a DTD are  
       present in aAtts.  
@param aAttsCount the number of elements in aAtts.  
@param aLineNumber the line number of the start tag in the data stream.  
  

### HandleEndElement(aName) ###
  
Called to handle the closing tag of an element.  
@param aName the fully qualified tagname of the element  
  

### HandleComment(aCommentText) ###
  
Called to handle a comment  
@param aCommentText the text of the comment (not including the  
       "<!--" and "-->")  
  

### HandleCDataSection(aData, aLength) ###
  
Called to handle a CDATA section  
@param aData the text in the CDATA section.  This is null-terminated.  
@param aLength the length of the aData string  
  

### HandleDoctypeDecl(aSubset, aName, aSystemId, aPublicId, aCatalogData) ###
  
Called to handle the doctype declaration  
  

### HandleCharacterData(aData, aLength) ###
  
Called to handle character data.  Note that this does NOT get  
called for the contents of CDATA sections.  
@param aData the data to handle.  aData is NOT NULL-TERMINATED.  
@param aLength the length of the aData string  
  

### HandleProcessingInstruction(aTarget, aData) ###
  
Called to handle a processing instruction  
@param aTarget the PI target (e.g. xml-stylesheet)  
@param aData all the rest of the data in the PI  
  

### HandleXMLDeclaration(aVersion, aEncoding, aStandalone) ###
  
Handle the XML Declaration.  
  
@param aVersion    The version string, can be null if not specified.  
@param aEncoding   The encoding string, can be null if not specified.  
@param aStandalone -1, 0, or 1 indicating respectively that there was no  
                   standalone parameter in the declaration, that it was  
                   given as no, or that it was given as yes.  
  

### ReportError(aErrorText, aSourceText, aError) ###
  
Ask the content sink if the expat driver should log an error to the console.  
  
@param aErrorText  Error message to pass to content sink.  
@param aSourceText Source text of the document we're parsing.  
@param aError      Script error object with line number & column number  
  
@retval True if the expat driver should report the error.  
  
