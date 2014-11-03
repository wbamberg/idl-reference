---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIWebBrowserStream.idl">Source file</a>
</div>

# nsIWebBrowserStream #
  
This interface provides a way to stream data to the web browser. This allows  
loading of data from sources which can not be accessed using URIs and  
nsIWebNavigation.  
  

## Methods ##

### openStream(aBaseURI, aContentType) ###
  
Prepare to load a stream of data. When this function returns successfully,  
it must be paired by a call to closeStream.  
  
  
@throw NS_ERROR_NOT_AVAILABLE  
       The requested content type is not supported.  
@throw NS_ERROR_IN_PROGRESS  
       openStream was called twice without an intermediate closeStream.  
  

#### Parameters ####

<table>

<tr>
<td>aBaseURI</td>
<td>       The base URI of the data. Must not be null. Relative  
       URIs will be resolved relative to this URI.  
</td>
</tr>

<tr>
<td>aContentType</td>
<td>       ASCII string giving the content type of the data. If rendering  
       content of this type is not supported, this method fails.  
       This string may include a charset declaration, for example:  
       text/html;charset=ISO-8859-1  
</td>
</tr>

</table>

### appendToStream(aData, aLen) ###
  
Append data to this stream.  
  
@note To append more than 4 GB of data, call this method multiple times.  
  

#### Parameters ####

<table>

<tr>
<td>aData</td>
<td>The data to append  
</td>
</tr>

<tr>
<td>aLen</td>
<td>Length of the data to append.  
</td>
</tr>

</table>

### closeStream() ###
  
Notifies the browser that all the data has been appended. This may notify  
the user that the browser is "done loading" in some form.  
  
@throw NS_ERROR_UNEXPECTED  
       This method was called without a preceding openStream.  
  
