---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/image/public/imgITools.idl">Source file</a>
</div>

# imgITools #

## Methods ##

### decodeImage(aStream, aMimeType) ###
  
decodeImage  
Caller provides an input stream and mimetype. We read from the stream  
and decompress it (according to the specified mime type) and return  
the resulting imgIContainer.  
  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       An input stream for an encoded image file.  
</td>
</tr>

<tr>
<td>aMimeType</td>
<td>       Type of image in the stream.  
</td>
</tr>

</table>

### decodeImageData(aStream, aMimeType, aContainer) ###
  
decodeImageData  
Caller provides an input stream and mimetype. We read from the stream  
and decompress it (according to the specified mime type) and return  
the resulting imgIContainer.  
  
This method is deprecated and will be removed at some time in the future;  
new code should use |decodeImage|.  
  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       An input stream for an encoded image file.  
</td>
</tr>

<tr>
<td>aMimeType</td>
<td>       Type of image in the stream.  
</td>
</tr>

<tr>
<td>aContainer</td>
<td>       An imgIContainer holding the decoded image will be returned via  
       this parameter. It is an error to provide any initial value but  
       |null|.  
</td>
</tr>

</table>

### encodeImage(aContainer, aMimeType, outputOptions) ###
  
encodeImage  
Caller provides an image container, and the mime type it should be  
encoded to. We return an input stream for the encoded image data.  
  
  

#### Parameters ####

<table>

<tr>
<td>aContainer</td>
<td>       An image container.  
</td>
</tr>

<tr>
<td>aMimeType</td>
<td>       Type of encoded image desired (eg "image/png").  
</td>
</tr>

<tr>
<td>outputOptions</td>
<td>       Encoder-specific output options.  
</td>
</tr>

</table>

### encodeScaledImage(aContainer, aMimeType, aWidth, aHeight, outputOptions) ###
  
encodeScaledImage  
Caller provides an image container, and the mime type it should be  
encoded to. We return an input stream for the encoded image data.  
The encoded image is scaled to the specified dimensions.  
  
  

#### Parameters ####

<table>

<tr>
<td>aContainer</td>
<td>       An image container.  
</td>
</tr>

<tr>
<td>aMimeType</td>
<td>       Type of encoded image desired (eg "image/png").  
</td>
</tr>

<tr>
<td>aWidth,</td>
<td>aHeight  
       The size (in pixels) desired for the resulting image. Specify 0 to  
       use the given image's width or height. Values must be >= 0.  
</td>
</tr>

<tr>
<td>outputOptions</td>
<td>       Encoder-specific output options.  
</td>
</tr>

</table>

### getImgLoaderForDocument(doc) ###
  
getImgLoaderForDocument  
Retrieve an image loader that reflects the privacy status of the given  
document.  
  
  

#### Parameters ####

<table>

<tr>
<td>doc</td>
<td>       A document. Must not be null.  
</td>
</tr>

</table>

### getImgCacheForDocument(doc) ###
  
getImgLoaderForDocument  
Retrieve an image cache that reflects the privacy status of the given  
document.  
  
  

#### Parameters ####

<table>

<tr>
<td>doc</td>
<td>       A document. Null is allowed, but must _only_ be passed  
       when there is no way to obtain a relevant document for  
       the current context in which a cache is desired.  
</td>
</tr>

</table>

### encodeCroppedImage(aContainer, aMimeType, aOffsetX, aOffsetY, aWidth, aHeight, outputOptions) ###
  
encodeCroppedImage  
Caller provides an image container, and the mime type it should be  
encoded to. We return an input stream for the encoded image data.  
The encoded image is cropped to the specified dimensions.  
  
The given offset and size must not exceed the image bounds.  
  
  

#### Parameters ####

<table>

<tr>
<td>aContainer</td>
<td>       An image container.  
</td>
</tr>

<tr>
<td>aMimeType</td>
<td>       Type of encoded image desired (eg "image/png").  
</td>
</tr>

<tr>
<td>aOffsetX,</td>
<td>aOffsetY  
       The crop offset (in pixels). Values must be >= 0.  
</td>
</tr>

<tr>
<td>aWidth,</td>
<td>aHeight  
       The size (in pixels) desired for the resulting image. Specify 0 to  
       use the given image's width or height. Values must be >= 0.  
</td>
</tr>

<tr>
<td>outputOptions</td>
<td>       Encoder-specific output options.  
</td>
</tr>

</table>

### createScriptedObserver(aObserver) ###
  
Create a wrapper around a scripted notification observer (ordinarily  
imgINotificationObserver cannot be implemented from scripts).  
  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>The scripted observer to wrap   
</td>
</tr>

</table>
