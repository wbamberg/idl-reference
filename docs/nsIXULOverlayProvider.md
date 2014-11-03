---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xul/nsIXULOverlayProvider.idl">Source file</a>
</div>

# nsIXULOverlayProvider #
<pre>  
The chrome registry implements this interface to give overlays  
to the gecko XUL engine.  
  
</pre>
## Methods ##

### getXULOverlays(aURI) ###
<pre>  
Get the XUL overlays for a particular chrome URI.  
  
@param aURI  The URI being loaded  
@return      An enumerator of nsIURI for the overlays of this URI   
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>The URI being loaded  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An enumerator of nsIURI for the overlays of this URI   
</td>
</tr>

</table>

### getStyleOverlays(aURI) ###
<pre>  
Get the style overlays for a particular chrome URI.  
  
@param aURI  The URI being loaded  
@return      An enumerator of nsIURI for the overlays of this URI   
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>The URI being loaded  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An enumerator of nsIURI for the overlays of this URI   
</td>
</tr>

</table>
