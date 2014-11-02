---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIDOMWindowUtils.idl">Source file</a>
</div>
# nsIJSRAIIHelper #
  
JS doesn't do RAII very well. We can use this interface to make remembering  
to destruct an object in a finally clause easier.  
  

## Methods ##

### destruct() ###
