---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsPILoadGroupInternal.idl">Source file</a>
</div>

# nsPILoadGroupInternal #
<pre>  
Dumping ground for load group experimental work.  
This interface will never be frozen.  If you are  
using any feature exposed by this interface, be aware that this interface  
will change and you will be broken.  You have been warned.  
  
</pre>
## Methods ##

### OnEndPageLoad(aDefaultChannel) ###
<pre>  
Called when the load group has loaded main page and  
subresources. (i.e.essentially DOMComplete)  
  
@param aDefaultChanel  
       The request channel for the base apge  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aDefaultChanel</td>
<td>       The request channel for the base apge  
</td>
</tr>

</table>
