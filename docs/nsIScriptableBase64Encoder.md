---
layout: default
---

# nsIScriptableBase64Encoder #
  
nsIScriptableBase64Encoder efficiently encodes the contents  
of a nsIInputStream to a Base64 string.  This avoids the need  
to read the entire stream into a buffer, and only then do the  
Base64 encoding.  
  
 If you already have a buffer full of data, you should use  
 btoa instead!  
  

## Methods ##

### encodeToCString(stream, length) ###
  
 These methods take an nsIInputStream and return a narrow or wide  
 string with the contents of the nsIInputStream base64 encoded.  
  
 The stream passed in must support ReadSegments and must not be  
 a non-blocking stream that will return NS_BASE_STREAM_WOULD_BLOCK.  
 If either of these restrictions are violated we will abort.  
  

### encodeToString(stream, length) ###
