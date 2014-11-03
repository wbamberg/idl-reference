---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIEmbeddingSiteWindow.idl">Source file</a>
</div>

# nsIEmbeddingSiteWindow #
  
The nsIEmbeddingSiteWindow is implemented by the embedder to provide  
Gecko with the means to call up to the host to resize the window,  
hide or show it and set/get its title.  
  

## Methods ##

### setDimensions(flags, x, y, cx, cy) ###
  
Sets the dimensions for the window; the position & size. The  
flags to indicate what the caller wants to set and whether the size  
refers to the inner or outer area. The inner area refers to just  
the embedded area, wheras the outer area can also include any   
surrounding chrome, window frame, title bar, and so on.  
  
  
  
@see getDimensions  
@see DIM_FLAGS_POSITION  
@see DIM_FLAGS_SIZE_OUTER  
@see DIM_FLAGS_SIZE_INNER  
  

#### Parameters ####

<table>

<tr>
<td>flags</td>
<td>Combination of position, inner and outer size flags.  
</td>
</tr>

<tr>
<td>x</td>
<td>Left hand corner of the outer area.  
</td>
</tr>

<tr>
<td>y</td>
<td>Top corner of the outer area.  
</td>
</tr>

<tr>
<td>cx</td>
<td>Width of the inner or outer area.  
</td>
</tr>

<tr>
<td>cy</td>
<td>Height of the inner or outer area.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td><code>NS_OK</code> if operation was performed correctly;  
        <code>NS_ERROR_UNEXPECTED</code> if window could not be  
          destroyed;  
        <code>NS_ERROR_INVALID_ARG</code> for bad flag combination  
          or illegal dimensions.  
</td>
</tr>

</table>

### getDimensions(flags, x, y, cx, cy) ###
  
Gets the dimensions of the window. The caller may pass  
<CODE>nullptr</CODE> for any value it is uninterested in receiving.  
  
  
@see setDimensions  
@see DIM_FLAGS_POSITION  
@see DIM_FLAGS_SIZE_OUTER  
@see DIM_FLAGS_SIZE_INNER  
  

#### Parameters ####

<table>

<tr>
<td>flags</td>
<td>Combination of position, inner and outer size flag .  
</td>
</tr>

<tr>
<td>x</td>
<td>Left hand corner of the outer area; or <CODE>nullptr</CODE>.  
</td>
</tr>

<tr>
<td>y</td>
<td>Top corner of the outer area; or <CODE>nullptr</CODE>.  
</td>
</tr>

<tr>
<td>cx</td>
<td>Width of the inner or outer area; or <CODE>nullptr</CODE>.  
</td>
</tr>

<tr>
<td>cy</td>
<td>Height of the inner or outer area; or <CODE>nullptr</CODE>.  
</td>
</tr>

</table>

### setFocus() ###
  
Give the window focus.  
  

### blur() ###
  
Blur the window. This should unfocus the window and send an onblur event.  
  

## Attributes ##

### visibility ###
  
Visibility of the window.  
  

### title ###
  
Title of the window.  
  

### siteWindow ###
  
Native window for the site's window. The implementor should copy the  
native window object into the address supplied by the caller. The  
type of the native window that the address refers to is  platform  
and OS specific as follows:  
  
<ul>  
  <li>On Win32 it is an <CODE>HWND</CODE>.</li>  
  <li>On MacOS this is a <CODE>WindowPtr</CODE>.</li>  
  <li>On GTK this is a <CODE>GtkWidget*</CODE>.</li>  
</ul>  
  

## Constants ##

### DIM_FLAGS_POSITION ###
  
Flag indicates that position of the top left corner of the outer area  
is required/specified.  
  
@see setDimensions  
@see getDimensions  
  

### DIM_FLAGS_SIZE_INNER ###
  
Flag indicates that the size of the inner area is required/specified.  
  
@note The inner and outer flags are mutually exclusive and it is  
      invalid to combine them.  
  
@see setDimensions  
@see getDimensions  
@see DIM_FLAGS_SIZE_OUTER  
  

### DIM_FLAGS_SIZE_OUTER ###
  
Flag indicates that the size of the outer area is required/specified.  
  
@see setDimensions  
@see getDimensions  
@see DIM_FLAGS_SIZE_INNER  
  
