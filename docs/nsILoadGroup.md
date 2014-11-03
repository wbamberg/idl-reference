---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsILoadGroup.idl">Source file</a>
</div>

# nsILoadGroup #
<pre>  
A load group maintains a collection of nsIRequest objects.   
  
</pre>
## Methods ##

### addRequest(aRequest, aContext) ###
<pre>  
Adds a new request to the group.  This will cause the default load  
flags to be applied to the request.  If this is a foreground  
request then the groupObserver's onStartRequest will be called.  
  
If the request is the default load request or if the default load  
request is null, then the load group will inherit its load flags from  
the request.  
  
</pre>
### removeRequest(aRequest, aContext, aStatus) ###
<pre>  
Removes a request from the group.  If this is a foreground request  
then the groupObserver's onStopRequest will be called.  
  
By the time this call ends, aRequest will have been removed from the  
loadgroup, even if this function throws an exception.  
  
</pre>
## Attributes ##

### groupObserver ###
<pre>  
The group observer is notified when requests are added to and removed  
from this load group.  The groupObserver is weak referenced.  
  
</pre>
### defaultLoadRequest ###
<pre>  
Accesses the default load request for the group.  Each time a number  
of requests are added to a group, the defaultLoadRequest may be set  
to indicate that all of the requests are related to a base request.  
  
The load group inherits its load flags from the default load request.  
If the default load request is NULL, then the group's load flags are  
not changed.  
  
</pre>
### requests ###
<pre>  
Returns the requests contained directly in this group.  
Enumerator element type: nsIRequest.  
  
</pre>
### activeCount ###
<pre>  
Returns the count of "active" requests (ie. requests without the  
LOAD_BACKGROUND bit set).  
  
</pre>
### notificationCallbacks ###
<pre>  
Notification callbacks for the load group.  
  
</pre>
### connectionInfo ###
<pre>  
Connection information for managing things like js/css  
connection blocking, and per-tab connection grouping  
  
</pre>
### defaultLoadFlags ###
<pre>  
The set of load flags that will be added to all new requests added to  
this group. Any existing requests in the load group are not modified,  
so it is expected these flags will be added before requests are added  
to the group - typically via nsIDocShell::defaultLoadFlags on a new  
docShell.  
Note that these flags are *not* added to the default request for the  
load group; it is expected the default request will already have these  
flags (again, courtesy of setting nsIDocShell::defaultLoadFlags before  
the docShell has created the default request.)  
  
</pre>