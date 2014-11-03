---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobilemessage/interfaces/nsIWapPushApplication.idl">Source file</a>
</div>

# nsIWapPushApplication #
<pre>  
Handle WAP Push notifications.  
  
</pre>
## Methods ##

### receiveWapPush(aData, aLength, aOffset, aOptions) ###
<pre>  
Receive WAP Push message.  
  
@param aData  
       An array containing raw PDU data.  
@param aLength  
       Length of aData.  
@param aOffset  
       Start offset of aData containing message body of the Push PDU.  
@param options  
       An object containing various attributes from lower transport layer.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aData</td>
<td>       An array containing raw PDU data.  
</td>
</tr>

<tr>
<td>aLength</td>
<td>       Length of aData.  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>       Start offset of aData containing message body of the Push PDU.  
</td>
</tr>

<tr>
<td>options</td>
<td>       An object containing various attributes from lower transport layer.  
</td>
</tr>

</table>
