---
layout: default
---

# nsIInputStreamChannel #
  
nsIInputStreamChannel  
  
This interface provides methods to initialize an input stream channel.  
The input stream channel serves as a data pump for an input stream.  
  

## Methods ##

### setURI(aURI) ###
  
Sets the URI for this channel.  This must be called before the  
channel is opened, and it may only be called once.  
  

## Attributes ##

### contentStream ###
  
Get/set the content stream  
  
This stream contains the data that will be pushed to the channel's  
stream listener.  If the stream is non-blocking and supports the  
nsIAsyncInputStream interface, then the stream will be read directly.  
Otherwise, the stream will be read on a background thread.  
  
This attribute must be set before the channel is opened, and it may  
only be set once.  
  
@throws NS_ERROR_IN_PROGRESS if the setter is called after the channel  
has been opened.  
  

### srcdocData ###
  
Get/set the srcdoc data string.  When the input stream channel is   
created to load a srcdoc iframe, this is set to hold the value of the  
srcdoc attribute.  
  
This should be the same value used to create contentStream, but this is  
not checked.  
  
Changing the value of this attribute will not otherwise affect the   
functionality of the channel or input stream.  
  

### isSrcdocChannel ###
  
Returns true if srcdocData has been set within the channel.  
  

### baseURI ###
  
The base URI to be used for the channel.  Used when the base URI cannot  
be inferred by other means, for example when this is a srcdoc channel.  
  
