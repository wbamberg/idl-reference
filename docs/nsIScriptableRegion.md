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

#### Parameters ####

<table>

<tr>
<td></td>
<td>region to copy  
</td>
</tr>

</table>

### setToRect(aX, aY, aWidth, aHeight) ###
  
copy operator equivalent that takes a rect  
  
@param      aX xoffset of rect to set region to  
@param      aY yoffset of rect to set region to  
@param      aWidth width of rect to set region to  
@param      aHeight height of rect to set region to  
@return     void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aX xoffset of rect to set region to  
</td>
</tr>

<tr>
<td></td>
<td>aY yoffset of rect to set region to  
</td>
</tr>

<tr>
<td></td>
<td>aWidth width of rect to set region to  
</td>
</tr>

<tr>
<td></td>
<td>aHeight height of rect to set region to  
</td>
</tr>

</table>

### intersectRegion(aRegion) ###
  
destructively intersect another region with this one  
  
@param      region to intersect  
@return     void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>region to intersect  
</td>
</tr>

</table>

### intersectRect(aX, aY, aWidth, aHeight) ###
  
destructively intersect a rect with this region  
  
@param      aX xoffset of rect to intersect with region  
@param      aY yoffset of rect to intersect with region  
@param      aWidth width of rect to intersect with region  
@param      aHeight height of rect to intersect with region  
@return     void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aX xoffset of rect to intersect with region  
</td>
</tr>

<tr>
<td></td>
<td>aY yoffset of rect to intersect with region  
</td>
</tr>

<tr>
<td></td>
<td>aWidth width of rect to intersect with region  
</td>
</tr>

<tr>
<td></td>
<td>aHeight height of rect to intersect with region  
</td>
</tr>

</table>

### unionRegion(aRegion) ###
  
destructively union another region with this one  
  
@param      region to union  
@return     void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>region to union  
</td>
</tr>

</table>

### unionRect(aX, aY, aWidth, aHeight) ###
  
destructively union a rect with this region  
  
@param      aX xoffset of rect to union with region  
@param      aY yoffset of rect to union with region  
@param      aWidth width of rect to union with region  
@param      aHeight height of rect to union with region  
@return     void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aX xoffset of rect to union with region  
</td>
</tr>

<tr>
<td></td>
<td>aY yoffset of rect to union with region  
</td>
</tr>

<tr>
<td></td>
<td>aWidth width of rect to union with region  
</td>
</tr>

<tr>
<td></td>
<td>aHeight height of rect to union with region  
</td>
</tr>

</table>

### subtractRegion(aRegion) ###
  
destructively subtract another region with this one  
  
@param      region to subtract  
@return     void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>region to subtract  
</td>
</tr>

</table>

### subtractRect(aX, aY, aWidth, aHeight) ###
  
destructively subtract a rect from this region  
  
@param      aX xoffset of rect to subtract with region  
@param      aY yoffset of rect to subtract with region  
@param      aWidth width of rect to subtract with region  
@param      aHeight height of rect to subtract with region  
@return     void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aX xoffset of rect to subtract with region  
</td>
</tr>

<tr>
<td></td>
<td>aY yoffset of rect to subtract with region  
</td>
</tr>

<tr>
<td></td>
<td>aWidth width of rect to subtract with region  
</td>
</tr>

<tr>
<td></td>
<td>aHeight height of rect to subtract with region  
</td>
</tr>

</table>

### isEmpty() ###
  
is this region empty? i.e. does it contain any pixels  
  
@param      none  
@return     returns whether the region is empty  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>none  
</td>
</tr>

</table>

### isEqualRegion(aRegion) ###
  
== operator equivalent i.e. do the regions contain exactly  
the same pixels  
  
@param      region to compare  
@return     whether the regions are identical  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>region to compare  
</td>
</tr>

</table>

### getBoundingBox(aX, aY, aWidth, aHeight) ###
  
returns the bounding box of the region i.e. the smallest  
rectangle that completely contains the region.          
  
@param      aX out parameter for xoffset of bounding rect for region  
@param      aY out parameter for yoffset of bounding rect for region  
@param      aWidth out parameter for width of bounding rect for region  
@param      aHeight out parameter for height of bounding rect for region  
@return     void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aX out parameter for xoffset of bounding rect for region  
</td>
</tr>

<tr>
<td></td>
<td>aY out parameter for yoffset of bounding rect for region  
</td>
</tr>

<tr>
<td></td>
<td>aWidth out parameter for width of bounding rect for region  
</td>
</tr>

<tr>
<td></td>
<td>aHeight out parameter for height of bounding rect for region  
</td>
</tr>

</table>

### offset(aXOffset, aYOffset) ###
  
offsets the region in x and y  
  
@param  xoffset  pixel offset in x  
@param  yoffset  pixel offset in y  
@return          void  
  
/  

#### Parameters ####

<table>

<tr>
<td></td>
<td>xoffset  pixel offset in x  
</td>
</tr>

<tr>
<td></td>
<td>yoffset  pixel offset in y  
</td>
</tr>

</table>

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

#### Parameters ####

<table>

<tr>
<td></td>
<td>rect to check for containment  
</td>
</tr>

</table>

## Attributes ##

### region ###
