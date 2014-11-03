---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIReflowObserver.idl">Source file</a>
</div>

# nsIReflowObserver #

## Methods ##

### reflow(start, end) ###
  
Called when an uninterruptible reflow has occurred.  
  
@param start timestamp when reflow ended, in milliseconds since  
             navigationStart (accurate to 1/1000 of a ms)  
@param end   timestamp when reflow ended, in milliseconds since  
             navigationStart (accurate to 1/1000 of a ms)  
  

#### Parameters ####

<table>

<tr>
<td>start</td>
<td>timestamp when reflow ended, in milliseconds since  
             navigationStart (accurate to 1/1000 of a ms)  
</td>
</tr>

<tr>
<td>end</td>
<td>timestamp when reflow ended, in milliseconds since  
             navigationStart (accurate to 1/1000 of a ms)  
</td>
</tr>

</table>

### reflowInterruptible(start, end) ###
  
Called when an interruptible reflow has occurred.  
  
@param start timestamp when reflow ended, in milliseconds since  
             navigationStart (accurate to 1/1000 of a ms)  
@param end   timestamp when reflow ended, in milliseconds since  
             navigationStart (accurate to 1/1000 of a ms)  
  

#### Parameters ####

<table>

<tr>
<td>start</td>
<td>timestamp when reflow ended, in milliseconds since  
             navigationStart (accurate to 1/1000 of a ms)  
</td>
</tr>

<tr>
<td>end</td>
<td>timestamp when reflow ended, in milliseconds since  
             navigationStart (accurate to 1/1000 of a ms)  
</td>
</tr>

</table>
