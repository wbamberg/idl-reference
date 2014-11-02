---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/streamconv/public/nsIStreamConverterService.idl">Source file</a>
</div>

# nsIStreamConverterService #
  
The nsIStreamConverterService is a higher level stream converter factory  
responsible for locating and creating stream converters  
(nsIStreamConverter).  
  
This service retrieves an interface that can convert data from a particular  
MIME type, to a particular MIME type. It is responsible for any intermediary  
conversion required in order to get from X to Z, assuming direct conversion  
is not possible.  
  
@author Jud Valeski  
@see nsIStreamConverter  
  

## Methods ##

### canConvert(aFromType, aToType) ###
  
Tests whether conversion between the two specified types is possible.  
This is cheaper than calling convert()/asyncConvertData(); it is not  
necessary to call this function before calling one of those, though.  
  

### convert(aFromStream, aFromType, aToType, aContext) ###
  
<b>SYNCHRONOUS VERSION</b>  
Converts a stream of one type, to a stream of another type.  
  
Use this method when you have a stream you want to convert.  
  
@param aFromStream   The stream representing the original/raw data.  
@param aFromType     The MIME type of aFromStream.  
@param aToType       The MIME type of the returned stream.  
@param aContext      Either an opaque context, or a converter specific  
                     context (implementation specific).  
@return              The converted stream. NOTE: The returned stream  
                     may not already be converted. An efficient stream  
                     converter implementation will convert data on  
                     demand rather than buffering the converted data  
                     until it is used.  
  

#### Parameters ####

<table>

<tr>
<td>aFromStream</td>
<td>The stream representing the original/raw data.  
</td>
</tr>

<tr>
<td>aFromType</td>
<td>The MIME type of aFromStream.  
</td>
</tr>

<tr>
<td>aToType</td>
<td>The MIME type of the returned stream.  
</td>
</tr>

<tr>
<td>aContext</td>
<td>Either an opaque context, or a converter specific  
                     context (implementation specific).  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The converted stream. NOTE: The returned stream  
                     may not already be converted. An efficient stream  
                     converter implementation will convert data on  
                     demand rather than buffering the converted data  
                     until it is used.  
</td>
</tr>

</table>

### asyncConvertData(aFromType, aToType, aListener, aContext) ###
  
<b>ASYNCHRONOUS VERSION</b>  
Retrieves a nsIStreamListener that receives the original/raw data via its  
nsIStreamListener::OnDataAvailable() callback, then converts and pushes   
the data to aListener.  
  
Use this method when you want to proxy (and convert) nsIStreamListener  
callbacks asynchronously.  
  
@param aFromType     The MIME type of the original/raw data.  
@param aToType       The MIME type of the converted data.  
@param aListener     The listener that receives the converted data.  
@param aCtxt         Either an opaque context, or a converter specific  
                     context (implementation specific).  
@return              A nsIStreamListener that receives data via its  
                     OnDataAvailable() method.  
  

#### Parameters ####

<table>

<tr>
<td>aFromType</td>
<td>The MIME type of the original/raw data.  
</td>
</tr>

<tr>
<td>aToType</td>
<td>The MIME type of the converted data.  
</td>
</tr>

<tr>
<td>aListener</td>
<td>The listener that receives the converted data.  
</td>
</tr>

<tr>
<td>aCtxt</td>
<td>Either an opaque context, or a converter specific  
                     context (implementation specific).  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A nsIStreamListener that receives data via its  
                     OnDataAvailable() method.  
</td>
</tr>

</table>
