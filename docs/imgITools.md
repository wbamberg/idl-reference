---
layout: default
---

# imgITools #

## Methods ##

### decodeImage ###
  
decodeImage  
Caller provides an input stream and mimetype. We read from the stream  
and decompress it (according to the specified mime type) and return  
the resulting imgIContainer.  
  
@param aStream  
       An input stream for an encoded image file.  
@param aMimeType  
       Type of image in the stream.  
  

### decodeImageData ###
  
decodeImageData  
Caller provides an input stream and mimetype. We read from the stream  
and decompress it (according to the specified mime type) and return  
the resulting imgIContainer.  
  
This method is deprecated and will be removed at some time in the future;  
new code should use |decodeImage|.  
  
@param aStream  
       An input stream for an encoded image file.  
@param aMimeType  
       Type of image in the stream.  
@param aContainer  
       An imgIContainer holding the decoded image will be returned via  
       this parameter. It is an error to provide any initial value but  
       |null|.  
  

### encodeImage ###
  
encodeImage  
Caller provides an image container, and the mime type it should be  
encoded to. We return an input stream for the encoded image data.  
  
@param aContainer  
       An image container.  
@param aMimeType  
       Type of encoded image desired (eg "image/png").  
@param outputOptions  
       Encoder-specific output options.  
  

### encodeScaledImage ###
  
encodeScaledImage  
Caller provides an image container, and the mime type it should be  
encoded to. We return an input stream for the encoded image data.  
The encoded image is scaled to the specified dimensions.  
  
@param aContainer  
       An image container.  
@param aMimeType  
       Type of encoded image desired (eg "image/png").  
@param aWidth, aHeight  
       The size (in pixels) desired for the resulting image. Specify 0 to  
       use the given image's width or height. Values must be >= 0.  
@param outputOptions  
       Encoder-specific output options.  
  

### getImgLoaderForDocument ###
  
getImgLoaderForDocument  
Retrieve an image loader that reflects the privacy status of the given  
document.  
  
@param doc  
       A document. Must not be null.  
  

### getImgCacheForDocument ###
  
getImgLoaderForDocument  
Retrieve an image cache that reflects the privacy status of the given  
document.  
  
@param doc  
       A document. Null is allowed, but must _only_ be passed  
       when there is no way to obtain a relevant document for  
       the current context in which a cache is desired.  
  

### encodeCroppedImage ###
  
encodeCroppedImage  
Caller provides an image container, and the mime type it should be  
encoded to. We return an input stream for the encoded image data.  
The encoded image is cropped to the specified dimensions.  
  
The given offset and size must not exceed the image bounds.  
  
@param aContainer  
       An image container.  
@param aMimeType  
       Type of encoded image desired (eg "image/png").  
@param aOffsetX, aOffsetY  
       The crop offset (in pixels). Values must be >= 0.  
@param aWidth, aHeight  
       The size (in pixels) desired for the resulting image. Specify 0 to  
       use the given image's width or height. Values must be >= 0.  
@param outputOptions  
       Encoder-specific output options.  
  

### createScriptedObserver ###
  
Create a wrapper around a scripted notification observer (ordinarily  
imgINotificationObserver cannot be implemented from scripts).  
  
@param aObserver The scripted observer to wrap   
  
