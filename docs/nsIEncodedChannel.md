---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIEncodedChannel.idl">Source file</a>
</div>

# nsIEncodedChannel #
  
A channel interface which allows special handling of encoded content  
  

## Methods ##

### doApplyContentConversions(aNextListener, aNewNextListener, aCtxt) ###
  
This function will start converters if they are available.  
aNewNextListener will be nullptr if no converter is available.  
  

## Attributes ##

### contentEncodings ###
  
This attribute holds the MIME types corresponding to the content  
encodings on the channel.  The enumerator returns nsISupportsCString  
objects.  The first one corresponds to the outermost encoding on the  
channel and then we work our way inward.  "identity" is skipped and not  
represented on the list.  Unknown encodings make the enumeration stop.  
If you want the actual Content-Encoding value, use  
getResponseHeader("Content-Encoding").  
  
When there is no Content-Encoding header, this property is null.  
  
Modifying the Content-Encoding header on the channel will cause  
this enumerator to have undefined behavior.  Don't do it.  
  
Also note that contentEncodings only exist during or after OnStartRequest.  
Calling contentEncodings before OnStartRequest is an error.  
  

### applyConversion ###
  
This attribute controls whether or not content conversion should be  
done per the Content-Encoding response header.  applyConversion can only   
be set before or during OnStartRequest.  Calling this during   
OnDataAvailable is an error.   
  
TRUE by default.  
  
