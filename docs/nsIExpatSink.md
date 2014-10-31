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
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>the fully qualified tagname of the element  
</td>
</tr>

<tr>
<td>aAtts</td>
<td>the array of attribute names and values.  There are  
       aAttsCount/2 names and aAttsCount/2 values, so the total number of  
       elements in the array is aAttsCount.  The names and values  
       alternate.  Thus, if we number attributes starting with 0,  
       aAtts[2*k] is the name of the k-th attribute and aAtts[2*k+1] is  
       the value of that attribute  Both explicitly specified attributes  
       and attributes that are defined to have default values in a DTD are  
       present in aAtts.  
</td>
</tr>

<tr>
<td>aAttsCount</td>
<td>the number of elements in aAtts.  
</td>
</tr>

<tr>
<td>aLineNumber</td>
<td>the line number of the start tag in the data stream.  
</td>
</tr>

</table>

### HandleEndElement(aName) ###
  
Called to handle the closing tag of an element.  
@param aName the fully qualified tagname of the element  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>the fully qualified tagname of the element  
</td>
</tr>

</table>

### HandleComment(aCommentText) ###
  
Called to handle a comment  
@param aCommentText the text of the comment (not including the  
       "<!--" and "-->")  
  

#### Parameters ####

<table>

<tr>
<td>aCommentText</td>
<td>the text of the comment (not including the  
       "<!--" and "-->")  
</td>
</tr>

</table>

### HandleCDataSection(aData, aLength) ###
  
Called to handle a CDATA section  
@param aData the text in the CDATA section.  This is null-terminated.  
@param aLength the length of the aData string  
  

#### Parameters ####

<table>

<tr>
<td>aData</td>
<td>the text in the CDATA section.  This is null-terminated.  
</td>
</tr>

<tr>
<td>aLength</td>
<td>the length of the aData string  
</td>
</tr>

</table>

### HandleDoctypeDecl(aSubset, aName, aSystemId, aPublicId, aCatalogData) ###
  
Called to handle the doctype declaration  
  

### HandleCharacterData(aData, aLength) ###
  
Called to handle character data.  Note that this does NOT get  
called for the contents of CDATA sections.  
@param aData the data to handle.  aData is NOT NULL-TERMINATED.  
@param aLength the length of the aData string  
  

#### Parameters ####

<table>

<tr>
<td>aData</td>
<td>the data to handle.  aData is NOT NULL-TERMINATED.  
</td>
</tr>

<tr>
<td>aLength</td>
<td>the length of the aData string  
</td>
</tr>

</table>

### HandleProcessingInstruction(aTarget, aData) ###
  
Called to handle a processing instruction  
@param aTarget the PI target (e.g. xml-stylesheet)  
@param aData all the rest of the data in the PI  
  

#### Parameters ####

<table>

<tr>
<td>aTarget</td>
<td>the PI target (e.g. xml-stylesheet)  
</td>
</tr>

<tr>
<td>aData</td>
<td>all the rest of the data in the PI  
</td>
</tr>

</table>

### HandleXMLDeclaration(aVersion, aEncoding, aStandalone) ###
  
Handle the XML Declaration.  
  
@param aVersion    The version string, can be null if not specified.  
@param aEncoding   The encoding string, can be null if not specified.  
@param aStandalone -1, 0, or 1 indicating respectively that there was no  
                   standalone parameter in the declaration, that it was  
                   given as no, or that it was given as yes.  
  

#### Parameters ####

<table>

<tr>
<td>aVersion</td>
<td>The version string, can be null if not specified.  
</td>
</tr>

<tr>
<td>aEncoding</td>
<td>The encoding string, can be null if not specified.  
</td>
</tr>

<tr>
<td>aStandalone</td>
<td>-1, 0, or 1 indicating respectively that there was no  
                   standalone parameter in the declaration, that it was  
                   given as no, or that it was given as yes.  
</td>
</tr>

</table>

### ReportError(aErrorText, aSourceText, aError) ###
  
Ask the content sink if the expat driver should log an error to the console.  
  
@param aErrorText  Error message to pass to content sink.  
@param aSourceText Source text of the document we're parsing.  
@param aError      Script error object with line number & column number  
  
@retval True if the expat driver should report the error.  
  

#### Parameters ####

<table>

<tr>
<td>aErrorText</td>
<td>Error message to pass to content sink.  
</td>
</tr>

<tr>
<td>aSourceText</td>
<td>Source text of the document we're parsing.  
</td>
</tr>

<tr>
<td>aError</td>
<td>Script error object with line number & column number  
</td>
</tr>

</table>
