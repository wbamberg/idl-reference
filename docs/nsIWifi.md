---
layout: default
---

# nsIWifi #

## shutdown ##

Shutdown the wifi system.


## getWifiScanResults ##

Returns the list of currently available networks as well as the list of
currently configured networks.

On success a callback is notified with the list of networks.
On failure after 3 scan retry attempts a callback is notified of failure.

