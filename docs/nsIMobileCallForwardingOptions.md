---
layout: default
---

# nsIMobileCallForwardingOptions #

## Attributes ##

### active ###

Call forwarding rule status.

It will be either not active (false), or active (true).

Note: Unused for setting call forwarding options. It reports
      the status of the rule when getting how the rule is
      configured.

@see 3GPP TS 27.007 7.11 "status".


### action ###

Indicates what to do with the rule. It shall be one of the
nsIMobileConnection.CALL_FORWARD_ACTION_* values.


### reason ###

Indicates the reason the call is being forwarded. It shall be one of the
nsIMobileConnection.CALL_FORWARD_REASON_* values.


### number ###

Phone number of forwarding address.


### timeSeconds ###

When "no reply" is enabled or queried, this gives the time in
seconds to wait before call is forwarded.


### serviceClass ###

Service for which the call forward is set up. It should be one of the
nsIMobileConnection.ICC_SERVICE_CLASS_* values.

