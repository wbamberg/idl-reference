---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIColorAnalyzer.idl">Source file</a>
</div>

# mozIColorAnalyzer #

## Methods ##

### findRepresentativeColor(imageURI, callback) ###
  
Given an image URI, find the most representative color for that image  
based on the frequency of each color.  Preference is given to colors that  
are more interesting.  Avoids the background color if it can be  
discerned.  Ignores sufficiently transparent colors.  
  
This is intended to be used on favicon images.  Larger images take longer  
to process, especially those with a larger number of unique colors.  If  
imageURI points to an image that has more than 128^2 pixels, this method  
will fail before analyzing it for performance reasons.  
  
  

#### Parameters ####

<table>

<tr>
<td>imageURI</td>
<td>       A URI pointing to the image - ideally a data: URI, but any scheme  
       that will load when setting the src attribute of a DOM img element  
       should work.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Function to call when the representative color is found or an  
       error occurs.  
</td>
</tr>

</table>
