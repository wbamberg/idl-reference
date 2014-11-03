---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/feeds/nsIFeedListener.idl">Source file</a>
</div>

# nsIFeedResultListener #
<pre>  
nsIFeedResultListener defines a callback used when feed processing  
completes.  
  
</pre>
## Methods ##

### handleResult(result) ###
<pre>   
Always called, even after an error. There could be new feed-level  
data available at this point, if it followed or was interspersed  
with the items. Fire-and-Forget implementations only need this.  
  
@param result  
       An object implementing nsIFeedResult representing the feed   
       and its metadata.   
  
</pre>
#### Parameters ####

<table>

<tr>
<td>result</td>
<td>       An object implementing nsIFeedResult representing the feed   
       and its metadata.   
</td>
</tr>

</table>
