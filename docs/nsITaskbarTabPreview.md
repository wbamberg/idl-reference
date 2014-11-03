---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarTabPreview.idl">Source file</a>
</div>

# nsITaskbarTabPreview #

## Methods ##

### move(aNext) ###
<pre>  
Rearranges the preview relative to another tab preview from the same window  
@param aNext The preview to the right of this one. A value of null  
             indicates that the preview is the rightmost one.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aNext</td>
<td>The preview to the right of this one. A value of null  
             indicates that the preview is the rightmost one.  
</td>
</tr>

</table>

### GetHWND() ###
<pre>  
Used internally to grab the handle to the proxy window.  
  
</pre>
### EnsureRegistration() ###
<pre>  
Used internally to ensure that the taskbar knows about this preview. If a  
preview is not registered, then the API call to set its sibling (via move)  
will silently fail.  
  
This method is only invoked when it is safe to make taskbar API calls.  
  
</pre>
## Attributes ##

### title ###
<pre>  
The title displayed above the thumbnail  
  
Default: an empty string  
  
</pre>
### icon ###
<pre>  
The icon displayed next to the title in the preview  
  
Default: null  
  
</pre>