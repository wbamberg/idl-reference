---
layout: default
---

# nsIScriptableRegion #

## Methods ##

### init() ###

### setToRegion(aRegion) ###
  
copy operator equivalent that takes another region  
  
@param      region to copy  
@return     void  
  
/  

### setToRect(aX, aY, aWidth, aHeight) ###
  
copy operator equivalent that takes a rect  
  
@param      aX xoffset of rect to set region to  
@param      aY yoffset of rect to set region to  
@param      aWidth width of rect to set region to  
@param      aHeight height of rect to set region to  
@return     void  
  
/  

### intersectRegion(aRegion) ###
  
destructively intersect another region with this one  
  
@param      region to intersect  
@return     void  
  
/  

### intersectRect(aX, aY, aWidth, aHeight) ###
  
destructively intersect a rect with this region  
  
@param      aX xoffset of rect to intersect with region  
@param      aY yoffset of rect to intersect with region  
@param      aWidth width of rect to intersect with region  
@param      aHeight height of rect to intersect with region  
@return     void  
  
/  

### unionRegion(aRegion) ###
  
destructively union another region with this one  
  
@param      region to union  
@return     void  
  
/  

### unionRect(aX, aY, aWidth, aHeight) ###
  
destructively union a rect with this region  
  
@param      aX xoffset of rect to union with region  
@param      aY yoffset of rect to union with region  
@param      aWidth width of rect to union with region  
@param      aHeight height of rect to union with region  
@return     void  
  
/  

### subtractRegion(aRegion) ###
  
destructively subtract another region with this one  
  
@param      region to subtract  
@return     void  
  
/  

### subtractRect(aX, aY, aWidth, aHeight) ###
  
destructively subtract a rect from this region  
  
@param      aX xoffset of rect to subtract with region  
@param      aY yoffset of rect to subtract with region  
@param      aWidth width of rect to subtract with region  
@param      aHeight height of rect to subtract with region  
@return     void  
  
/  

### isEmpty() ###
  
is this region empty? i.e. does it contain any pixels  
  
@param      none  
@return     returns whether the region is empty  
  
/  

### isEqualRegion(aRegion) ###
  
== operator equivalent i.e. do the regions contain exactly  
the same pixels  
  
@param      region to compare  
@return     whether the regions are identical  
  
/  

### getBoundingBox(aX, aY, aWidth, aHeight) ###
  
returns the bounding box of the region i.e. the smallest  
rectangle that completely contains the region.          
  
@param      aX out parameter for xoffset of bounding rect for region  
@param      aY out parameter for yoffset of bounding rect for region  
@param      aWidth out parameter for width of bounding rect for region  
@param      aHeight out parameter for height of bounding rect for region  
@return     void  
  
/  

### offset(aXOffset, aYOffset) ###
  
offsets the region in x and y  
  
@param  xoffset  pixel offset in x  
@param  yoffset  pixel offset in y  
@return          void  
  
/  

### getRects() ###
  
@return null if there are no rects,  
@return flat array of rects,ie [x1,y1,width1,height1,x2...].  
The result will contain bogus data if values don't fit in 31 bit  
/  

### containsRect(aX, aY, aWidth, aHeight) ###
  
does the region intersect the rectangle?  
  
@param      rect to check for containment  
@return     true if the region intersects the rect  
  
/  

## Attributes ##

### region ###
