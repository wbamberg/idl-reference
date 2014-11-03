---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsICellInfo.idl">Source file</a>
</div>

# nsIGsmCellInfo #

## Attributes ##

### mcc ###
<pre>  
3-digit Mobile Country Code, 0..999, INT_MAX if unknown.  
  
</pre>
### mnc ###
<pre>  
2 or 3-digit Mobile Network Code, 0..999, INT_MAX if unknown.  
  
</pre>
### lac ###
<pre>  
16-bit Location Area Code, 0..65535, INT_MAX if unknown.  
  
</pre>
### cid ###
<pre>  
16-bit GSM Cell Identity described in TS 27.007, 0..65535, INT_MAX if unknown.  
  
</pre>
### signalStrength ###
<pre>  
Valid values are 0-31 as defined in TS 27.007 8.5, 99 if unknown.  
  
</pre>
### bitErrorRate ###
<pre>  
Bit error rate 0-7 as defined in TS 27.007 8.5, 99 if unknown.  
  
</pre>