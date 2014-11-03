---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISerializationHelper.idl">Source file</a>
</div>

# nsISerializationHelper #

## Methods ##

### serializeToString(serializable) ###
<code>  
Serialize the object to a base64 string. This string can be later passed  
as an input to deserializeObject method.  
  
</code>
### deserializeObject(input) ###
<code>  
Takes base64 encoded string that cointains serialization of a single  
object. Most commonly, input is result of previous call to  
serializeToString.  
  
</code>