---
layout: default
---

# nsIDOMParser #
  
The nsIDOMParser interface is a non-SAX interface that can be used  
to parse a string or byte stream containing XML or HTML content  
to a DOM document. Parsing is always synchronous - a document is always  
returned from the parsing methods. This is as opposed to loading and  
parsing with the XMLHttpRequest interface, which can be used for  
asynchronous (callback-based) loading.  
  

## Methods ##

### parseFromString(str, contentType) ###
  
The string passed in is parsed into a DOM document.  
  
@param str The UTF16 string to be parsed  
@param contentType The content type of the string (see parseFromStream)  
@returns The DOM document created as a result of parsing the   
         string  
  

#### Parameters ####

<table>

<tr>
<td>str</td>
<td>The UTF16 string to be parsed  
</td>
</tr>

<tr>
<td>str</td>
<td>The UTF16 string to be parsed  
</td>
</tr>

</table>

### parseFromBuffer(buf, bufLen, contentType) ###
  
The buffer is parsed into a DOM document.  
The charset is determined from the xml entity decl.  
  
@param buf The octet array data to be parsed  
@param bufLen Length (in bytes) of the data  
@param contentType The content type of the data (see parseFromStream)  
@returns The DOM document created as a result of parsing the   
         string  
  

#### Parameters ####

<table>

<tr>
<td>buf</td>
<td>The octet array data to be parsed  
</td>
</tr>

<tr>
<td>buf</td>
<td>The octet array data to be parsed  
</td>
</tr>

<tr>
<td>buf</td>
<td>The octet array data to be parsed  
</td>
</tr>

</table>

### parseFromStream(stream, charset, contentLength, contentType) ###
  
The byte stream passed in is parsed into a DOM document.  
  
Not accessible from web content.  
  
@param stream The byte stream whose contents are parsed  
@param charset The character set that was used to encode the byte  
               stream. NULL if not specified.  
@param contentLength The number of bytes in the input stream.  
@param contentType The content type of the string - either text/xml,  
                   application/xml, or application/xhtml+xml.  
                   Must not be NULL.  
@returns The DOM document created as a result of parsing the   
         stream  
  

#### Parameters ####

<table>

<tr>
<td>stream</td>
<td>The byte stream whose contents are parsed  
</td>
</tr>

<tr>
<td>stream</td>
<td>The byte stream whose contents are parsed  
</td>
</tr>

<tr>
<td>stream</td>
<td>The byte stream whose contents are parsed  
</td>
</tr>

<tr>
<td>stream</td>
<td>The byte stream whose contents are parsed  
</td>
</tr>

</table>

### init(principal, documentURI, baseURI, scriptObject) ###
  
Initialize the principal and document and base URIs that the parser should  
use for documents it creates.  If this is not called, then a null  
principal and its URI will be used.  When creating a DOMParser via the JS  
constructor, this will be called automatically.  This method may only be  
called once.  If this method fails, all following parse attempts will  
fail.  
  
@param principal The principal to use for documents we create.  
                 If this is null, a codebase principal will be created  
                 based on documentURI; in that case the documentURI must  
                 be non-null.  
@param documentURI The documentURI to use for the documents we create.  
                   If null, the principal's URI will be used;  
                   in that case, the principal must be non-null and its  
                   URI must be non-null.  
@param baseURI The baseURI to use for the documents we create.  
               If null, the documentURI will be used.  
@param scriptObject The object from which the context for event handling  
                    can be got.  
  

#### Parameters ####

<table>

<tr>
<td>principal</td>
<td>The principal to use for documents we create.  
                 If this is null, a codebase principal will be created  
                 based on documentURI; in that case the documentURI must  
                 be non-null.  
</td>
</tr>

<tr>
<td>principal</td>
<td>The principal to use for documents we create.  
                 If this is null, a codebase principal will be created  
                 based on documentURI; in that case the documentURI must  
                 be non-null.  
</td>
</tr>

<tr>
<td>principal</td>
<td>The principal to use for documents we create.  
                 If this is null, a codebase principal will be created  
                 based on documentURI; in that case the documentURI must  
                 be non-null.  
</td>
</tr>

<tr>
<td>principal</td>
<td>The principal to use for documents we create.  
                 If this is null, a codebase principal will be created  
                 based on documentURI; in that case the documentURI must  
                 be non-null.  
</td>
</tr>

</table>
