---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIColorAnalyzer.idl">Source file</a>
</div>

# mozIRepresentativeColorCallback #

## Methods ##

### onComplete(success, color) ###
  
Will be called when color analysis finishes.  
  
@param success  
       True if analysis was successful, false otherwise.  
       Analysis can fail if the image is transparent, imageURI doesn't  
       resolve to a valid image, or the image is too big.  
  
@param color  
       The representative color as an integer in RGB form.  
       e.g. 0xFF0102 == rgb(255,1,2)  
       If success is false, color is not provided.  
  

#### Parameters ####

<table>

<tr>
<td>success</td>
<td>       True if analysis was successful, false otherwise.  
       Analysis can fail if the image is transparent, imageURI doesn't  
       resolve to a valid image, or the image is too big.  
</td>
</tr>

<tr>
<td>color</td>
<td>       The representative color as an integer in RGB form.  
       e.g. 0xFF0102 == rgb(255,1,2)  
       If success is false, color is not provided.  
</td>
</tr>

</table>
