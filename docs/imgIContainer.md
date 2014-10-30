---
layout: default
---

# imgIContainer #
  
imgIContainer is the interface that represents an image. It allows  
access to frames as Thebes surfaces. It also allows drawing of images  
onto Thebes contexts.  
  
Internally, imgIContainer also manages animation of images.  
  

## Methods ##

### optimalImageSizeForDest(aDest, aWhichFrame, aFilter, aFlags) ###
  
Given a size at which this image will be displayed, and the drawing  
parameters affecting how it will be drawn, returns the image size which  
should be used to draw to produce the highest quality result. This is the  
appropriate size, for example, to use as an input to the pixel snapping  
algorithm.  
  
For best results the size returned by this method should not be cached. It  
can change over time due to changes in the internal state of the image.  
  
@param aDest The size of the destination rect into which this image will be  
             drawn, in device pixels.  
@param aWhichFrame Frame specifier of the FRAME_* variety.  
@param aFilter The filter to be used if we're scaling the image.  
@param aFlags Flags of the FLAG_* variety  
  

### GetType() ###
  
Direct C++ accessor for 'type' attribute, for convenience.  
  

### getFrame(aWhichFrame, aFlags) ###
  
Get a surface for the given frame. This may be a platform-native,  
optimized surface, so you cannot inspect its pixel data. If you  
need that, use SourceSurface::GetDataSurface.  
  
@param aWhichFrame Frame specifier of the FRAME_* variety.  
@param aFlags Flags of the FLAG_* variety  
  

### frameIsOpaque(aWhichFrame) ###
  
Whether the given frame is opaque; that is, needs the background painted  
behind it.  
  
@param aWhichFrame Frame specifier of the FRAME_* variety.  
  

### getImageContainer(aManager) ###
  
Attempts to create an ImageContainer (and Image) containing the current  
frame. Only valid for RASTER type images.  
  

### draw(aContext, aSize, aRegion, aWhichFrame, aFilter, aSVGContext, aFlags) ###
  
Draw the requested frame of this image onto the context specified.  
  
Drawing an image involves scaling it to a certain size (which may be  
implemented as a "smart" scale by substituting an HQ-scaled frame or  
rendering at a high DPI), and then selecting a region of that image to  
draw. That region is drawn onto the graphics context and in the process  
transformed by the context matrix, which determines the final area that is  
filled. The basic process looks like this:  
  
                          +------------------+  
                          |      Image       |  
                          |                  |  
                          | intrinsic width  |  
                          |        X         |  
                          | intrinsic height |  
                          +------------------+  
                         /                    \  
                        /                      \  
                       /    (scale to aSize)    \  
                      /                          \  
                     +----------------------------+  
                     |                            |  
                     |        Scaled Image        |  
                     | aSize.width X aSize.height |  
                     |                            |  
                     |       +---------+          |  
                     |       | aRegion |          |  
                     |       +---------+          |  
                     +-------(---------(----------+  
                             |         |  
                            /           \  
                           |  (transform |  
                          /  by aContext  \  
                         |     matrix)     |  
                        /                   \  
                       +---------------------+  
                       |                     |  
                       |      Fill Rect      |  
                       |                     |  
                       +---------------------+  
  
The region may extend outside of the scaled image's boundaries. It's  
actually a region in tiled image space, which is formed by tiling the  
scaled image infinitely in every direction. Drawing with a region larger  
than the scaled image thus causes the filled area to contain multiple tiled  
copies of the image, which looks like this:  
  
          ....................................................  
          :                :                :                :  
          :      Tile      :      Tile      :      Tile      :  
          :        +------------[aRegion]------------+       :  
          :........|.......:................:........|.......:  
          :        |       :                :        |       :  
          :      Ti|le     :  Scaled Image  :      Ti|le     :  
          :        |       :                :        |       :  
          :........|.......:................:........|.......:  
          :        +---------------------------------+       :  
          :      Ti|le     :      Tile      :      Ti|le     :  
          :       /        :                :         \      :  
          :......(.........:................:..........).....:  
                 |                                     |  
                /                                       \  
               |      (transform by aContext matrix)     |  
              /                                           \  
             +---------------------------------------------+  
             |     :                                 :     |  
             |.....:.................................:.....|  
             |     :                                 :     |  
             |     :           Tiled Fill            :     |  
             |     :                                 :     |  
             |.....:.................................:.....|  
             |     :                                 :     |  
             +---------------------------------------------+  
  
  
@param aContext The Thebes context to draw the image to.  
@param aSize The size to which the image should be scaled before drawing.  
             This requirement may be satisfied using HQ scaled frames,  
             selecting from different resolution layers, drawing at a  
             higher DPI, or just performing additional scaling on the  
             graphics context. Callers can use optimalImageSizeForDest()  
             to determine the best choice for this parameter if they have  
             no special size requirements.  
@param aRegion The region in tiled image space which will be drawn onto the  
               graphics context. aRegion is in the coordinate space of the  
               image after it has been scaled to aSize - that is, the image  
               is scaled first, and then aRegion is applied. When aFlags  
               includes FLAG_CLAMP, the image will be extended to this area  
               by clamping image sample coordinates. Otherwise, the image  
               will be automatically tiled as necessary. aRegion can also  
               optionally contain a second region which restricts the set of  
               pixels we're allowed to sample from when drawing; this is  
               only of use to callers which need to draw with pixel snapping.  
@param aWhichFrame Frame specifier of the FRAME_* variety.  
@param aFilter The filter to be used if we're scaling the image.  
@param aSVGContext If specified, SVG-related rendering context, such as  
                   overridden attributes on the image document's root <svg>  
                   node, and the size of the viewport that the full image  
                   would occupy. Ignored for raster images.  
@param aFlags Flags of the FLAG_* variety  
  

### requestDecode() ###

### startDecoding() ###

### isDecoded() ###

### lockImage() ###
  
Increments the lock count on the image. An image will not be discarded  
as long as the lock count is nonzero. Note that it is still possible for  
the image to be undecoded if decode-on-draw is enabled and the image  
was never drawn.  
  
Upon instantiation images have a lock count of zero.  
  

### unlockImage() ###
  
Decreases the lock count on the image. If the lock count drops to zero,  
the image is allowed to discard its frame data to save memory.  
  
Upon instantiation images have a lock count of zero. It is an error to  
call this method without first having made a matching lockImage() call.  
In other words, the lock count is not allowed to be negative.  
  

### requestDiscard() ###
  
If this image is unlocked, discard its decoded data.  If the image is  
locked or has already been discarded, do nothing.  
  

### requestRefresh(aTime) ###
  
Indicates that this imgIContainer has been triggered to update  
its internal animation state. Likely this should only be called  
from within nsImageFrame or objects of similar type.  
  

### resetAnimation() ###

### getFrameIndex(aWhichFrame) ###

### getOrientation() ###

### getFirstFrameDelay() ###

### setAnimationStartTime(aTime) ###

### getImageSpaceInvalidationRect(aRect) ###

### unwrap() ###

## Attributes ##

### width ###
  
The width of the container rectangle.  In the case of any error,  
zero is returned, and an exception will be thrown.  
  

### height ###
  
The height of the container rectangle.  In the case of any error,  
zero is returned, and an exception will be thrown.  
  

### intrinsicSize ###
  
The intrinsic size of this image in appunits. If the image has no intrinsic  
size in a dimension, -1 will be returned for that dimension. In the case of  
any error, an exception will be thrown.  
  

### intrinsicRatio ###
  
The (dimensionless) intrinsic ratio of this image. In the case of any error,  
an exception will be thrown.  
  

### type ###
  
The type of this image (one of the TYPE_* values above).  
  

### animated ###
  
Whether this image is animated. You can only be guaranteed that querying  
this will not throw if STATUS_DECODE_COMPLETE is set on the imgIRequest.  
  
@throws NS_ERROR_NOT_AVAILABLE if the animated state cannot be determined.  
  

### animationMode ###

## Constants ##

### TYPE_RASTER ###
  
Enumerated values for the 'type' attribute (below).  
  

### TYPE_VECTOR ###

### FLAG_NONE ###
  
Flags for imgIContainer operations.  
  
Meanings:  
  
FLAG_NONE: Lack of flags  
  
FLAG_SYNC_DECODE: Forces synchronous/non-progressive decode of all  
available data before the call returns. It is an error to pass this flag  
from a call stack that originates in a decoder (ie, from a decoder  
observer event).  
  
FLAG_DECODE_NO_PREMULTIPLY_ALPHA: Do not premultiply alpha if  
it's not already premultiplied in the image data.  
  
FLAG_DECODE_NO_COLORSPACE_CONVERSION: Do not do any colorspace conversion;  
ignore any embedded profiles, and don't convert to any particular destination  
space.  
  
FLAG_CLAMP: Extend the image to the fill area by clamping image sample  
coordinates instead of by tiling. This only affects 'draw'.  
  
FLAG_HIGH_QUALITY_SCALING: A hint as to whether this image should be  
scaled using the high quality scaler. Do not set this if not drawing to  
a window or not listening to invalidations.  
  

### FLAG_SYNC_DECODE ###

### FLAG_DECODE_NO_PREMULTIPLY_ALPHA ###

### FLAG_DECODE_NO_COLORSPACE_CONVERSION ###

### FLAG_CLAMP ###

### FLAG_HIGH_QUALITY_SCALING ###

### FLAG_WANT_DATA_SURFACE ###
  
Can be passed to GetFrame when the caller wants a DataSourceSurface  
instead of a hardware accelerated surface. This can be important for  
performance (by avoiding an upload to/readback from the GPU) when the  
caller knows they want a SourceSurface of type DATA.  
  

### FLAG_BYPASS_SURFACE_CACHE ###
  
Forces drawing to happen rather than taking cached rendering from the  
surface cache. This is used when we are printing, for example, where we  
want the vector commands from VectorImages to end up in the PDF output  
rather than a cached rendering at screen resolution.  
  

### FRAME_FIRST ###
  
Constants for specifying various "special" frames.  
  
FRAME_FIRST: The first frame  
FRAME_CURRENT: The current frame  
  
FRAME_MAX_VALUE should be set to the value of the maximum constant above,  
as it is used for ensuring that a valid value was passed in.  
  

### FRAME_CURRENT ###

### FRAME_MAX_VALUE ###

### kNormalAnimMode ###
  
Animation mode Constants  
  0 = normal  
  1 = don't animate  
  2 = loop once  
  

### kDontAnimMode ###

### kLoopOnceAnimMode ###
