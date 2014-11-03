---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsIMobileCallForwardingOptions.idl">Source file</a>
</div>

# nsIMobileCallForwardingOptions #

## Attributes ##

### active ###
<pre>  
Call forwarding rule status.  
  
It will be either not active (false), or active (true).  
  
Note: Unused for setting call forwarding options. It reports  
      the status of the rule when getting how the rule is  
      configured.  
  
@see 3GPP TS 27.007 7.11 "status".  
  
</pre>
### action ###
<pre>  
Indicates what to do with the rule. It shall be one of the  
nsIMobileConnection.CALL_FORWARD_ACTION_* values.  
  
</pre>
### reason ###
<pre>  
Indicates the reason the call is being forwarded. It shall be one of the  
nsIMobileConnection.CALL_FORWARD_REASON_* values.  
  
</pre>
### number ###
<pre>  
Phone number of forwarding address.  
  
</pre>
### timeSeconds ###
<pre>  
When "no reply" is enabled or queried, this gives the time in  
seconds to wait before call is forwarded.  
  
</pre>
### serviceClass ###
<pre>  
Service for which the call forward is set up. It should be one of the  
nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
  
</pre>