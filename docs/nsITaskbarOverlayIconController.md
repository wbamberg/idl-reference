---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarOverlayIconController.idl">Source file</a>
</div>

# nsITaskbarOverlayIconController #
  
Starting in Windows 7, applications can display an overlay on the icon in  
the taskbar. This class wraps around the native functionality to do this.  
  

## Methods ##

### setOverlayIcon(statusIcon, statusDescription) ###
  
Sets the overlay icon and its corresponding alt text.  
  
  
@note The behavior for window groups is managed by Windows.  
- If an overlay icon is set for any window in a window group and another  
  overlay icon is already applied to the corresponding taskbar button, that  
  existing overlay is replaced.  
- If null is passed in to replace the overlay currently being displayed,  
  and if a previous overlay set for a different window in the group is  
  still available, then that previous overlay is displayed.  
  

#### Parameters ####

<table>

<tr>
<td>statusIcon</td>
<td>The handle to the overlay icon. The icon will be scaled  
                  to the small icon size (16x16 at 96 dpi). Can be null, in  
                  which case if the taskbar button represents a single window  
                  the icon is removed.  
</td>
</tr>

<tr>
<td>statusDescription</td>
<td>The alt text version of the information  
                         conveyed by the overlay, for accessibility  
                         purposes.  
</td>
</tr>

</table>
