---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIRedirectResultListener.idl">Source file</a>
</div>

# nsIRedirectResultListener #

## Methods ##

### onRedirectResult(proceeding) ###
  
 When an HTTP redirect has been processed (either successfully or not)  
 nsIHttpChannel will call this function if its callbacks implement this  
 interface.  
  
 @param proceeding  
        Indicated whether the redirect will be proceeding, or not (i.e.  
        has been canceled, or failed).  
  

#### Parameters ####

<table>

<tr>
<td>m</td>
<td>proceeding  
        Indicated whether the redirect will be proceeding, or not (i.e.  
        has been canceled, or failed).  
</td>
</tr>

</table>
