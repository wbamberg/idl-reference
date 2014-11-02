---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/image/decoders/icon/nsIIconURI.idl">Source file</a>
</div>
# nsIMozIconURI #
  
nsIIconURI  
  
This interface derives from nsIURI, to provide additional information  
about moz-icon URIs.  
  
What *is* a moz-icon URI you ask?  Well, it has the following syntax:  
  
moz-icon:[<valid-url> | //<file-with-extension> | //stock/<stock-icon>]? ['?'[<parameter-value-pairs>]]  
  
<valid-url> is a valid URL spec.  
  
<file-with-extension> is any filename with an extension, e.g. "dummy.html".  
If the file you want an icon for isn't known to exist, you can use this instead of a URL and just  
place a dummy file name with the extension or content type you want.  
  
<stock-icon> is the name of a platform-dependant stock icon.  
  
Legal parameter value pairs are listed below:  
  
  Parameter:   size  
  Values:      [<integer> | button | toolbar | toolbarsmall | menu | dialog]  
  Description: If integer, this is the desired size in square pixels of the icon  
               Else, use the OS default for the specified keyword context.  
  
  Parameter:   state  
  Values:      [normal | disabled]  
  Description: The state of the icon.  
  
  Parameter:   contentType  
  Values:      <mime-type>  
  Description: The mime type we want an icon for. This is ignored by stock images.  
  

## Attributes ##

### iconURL ###
  
iconFile  
  
the file URL contained within this moz-icon url, or null.  
  

### imageSize ###
  
imageSize  
  
The image area in square pixels, defaulting to 16 if unspecified.  
  

### stockIcon ###
  
stockIcon  
  
The stock icon name requested from the OS.  
  

### iconSize ###
  
iconSize  
  
The stock icon size requested from the OS.  
  

### iconState ###
  
iconState  
  
The stock icon state requested from the OS.  
  

### contentType ###
  
contentType  
  
A valid mime type, or the empty string.  
  

### fileExtension ###
  
fileExtension  
  
The file extension of the file which we are looking up.  
  
