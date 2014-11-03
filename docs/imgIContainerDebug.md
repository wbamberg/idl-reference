---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/image/public/imgIContainerDebug.idl">Source file</a>
</div>

# imgIContainerDebug #
<pre>  
This interface is used in debug builds (and only there) in  
order to let automatic tests running JavaScript access  
internal state of imgContainers. This lets us test  
things like animation.  
  
</pre>
## Attributes ##

### framesNotified ###
<pre>  
The # of frames this imgContainer has been notified about.  
That is equal to the # of times the animation timer has  
fired, and is usually equal to the # of frames actually  
drawn (but actual drawing might be disabled).  
  
</pre>