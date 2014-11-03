---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsICellInfo.idl">Source file</a>
</div>

# nsILteCellInfo #

## Attributes ##

### mcc ###
<pre>  
3-digit Mobile Country Code, 0..999, INT_MAX if unknown.  
  
</pre>
### mnc ###
<pre>  
2 or 3-digit Mobile Network Code, 0..999, INT_MAX if unknown.  
  
</pre>
### cid ###
<pre>  
28-bit Cell Identity, 0..268435455, INT_MAX if unknown.  
  
</pre>
### pcid ###
<pre>  
Physical cell id, 0..503, INT_MAX if unknown.  
  
</pre>
### tac ###
<pre>  
16-bit tracking area code, 0..65535, INT_MAX if unknown.  
  
</pre>
### signalStrength ###
<pre>  
Valid values are 0-31 as defined in TS 27.007 8.5, 99 if unknown.  
  
</pre>
### rsrp ###
<pre>  
The current Reference Signal Receive Power in dBm multipled by -1.  
Range: 44 to 140 dBm, INT_MAX if unknown.  
  
</pre>
### rsrq ###
<pre>  
The current Reference Signal Receive Quality in dB multiplied by -1.  
Range: 3 to 20 dB, INT_MAX if unknown.  
  
</pre>
### rssnr ###
<pre>  
The current reference signal signal-to-noise ratio in 0.1 dB units.  
Range: -200 to +300 (-200 = -20.0 dB, +300 = 30dB), INT_MAX if unknown.  
  
</pre>
### cqi ###
<pre>  
The current Channel Quality Indicator. Range: 0 to 15, INT_MAX if unknown.  
  
</pre>
### timingAdvance ###
<pre>  
Timing advance in micro seconds for a one way trip from cell to device.  
Approximate distance can be calculated using 300m/us * timingAdvance.  
Range: 0 to 0x7FFFFFFE, INT_MAX if unknown.  
  
</pre>