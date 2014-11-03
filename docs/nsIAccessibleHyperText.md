---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleHyperText.idl">Source file</a>
</div>

# nsIAccessibleHyperText #
<pre>  
A cross-platform interface that deals with text which contains hyperlinks.  
Each link is an embedded object representing exactly 1 character within  
the hypertext.  
  
Current implementation assumes every embedded object is a link.  
  
</pre>
## Methods ##

### getLinkAt(index) ###
<pre>  
Return link accessible at the given index.  
  
@param index  [in] 0-based index of the link that is to be retrieved  
  
@return       link accessible or null if there is no link at that index  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>index</td>
<td>[in] 0-based index of the link that is to be retrieved  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>link accessible or null if there is no link at that index  
</td>
</tr>

</table>

### getLinkIndex(link) ###
<pre>  
Return index of the given link.  
  
@param link  [in] link accessible the index is requested for  
  
@return      index of the given link or null if there's no link within  
               hypertext accessible  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>link</td>
<td>[in] link accessible the index is requested for  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>index of the given link or null if there's no link within  
               hypertext accessible  
</td>
</tr>

</table>

### getLinkIndexAtOffset(offset) ###

## Attributes ##

### linkCount ###
<pre>  
Return the number of links contained within this hypertext object.  
  
</pre>