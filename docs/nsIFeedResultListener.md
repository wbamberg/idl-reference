---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/feeds/nsIFeedListener.idl">Source file</a>
</div>

# nsIFeedResultListener #
  
nsIFeedResultListener defines a callback used when feed processing  
completes.  
  

## Methods ##

### handleResult(result) ###
   
Always called, even after an error. There could be new feed-level  
data available at this point, if it followed or was interspersed  
with the items. Fire-and-Forget implementations only need this.  
  
@param result  
       An object implementing nsIFeedResult representing the feed   
       and its metadata.   
  

#### Parameters ####

<table>

<tr>
<td>result</td>
<td>       An object implementing nsIFeedResult representing the feed   
       and its metadata.   
</td>
</tr>

</table>
