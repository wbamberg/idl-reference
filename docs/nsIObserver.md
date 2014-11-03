---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIObserver.idl">Source file</a>
</div>

# nsIObserver #
<code>  
This interface is implemented by an object that wants  
to observe an event corresponding to a topic.  
  
</code>
## Methods ##

### observe(aSubject, aTopic, aData) ###
<code>  
Observe will be called when there is a notification for the  
topic |aTopic|.  This assumes that the object implementing  
this interface has been registered with an observer service  
such as the nsIObserverService.   
  
If you expect multiple topics/subjects, the impl is   
responsible for filtering.  
  
You should not modify, add, remove, or enumerate   
notifications in the implemention of observe.   
  
@param aSubject : Notification specific interface pointer.  
@param aTopic   : The notification topic or subject.  
@param aData    : Notification specific wide string.  
                   subject event.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aSubject</td>
<td>: Notification specific interface pointer.  
</td>
</tr>

<tr>
<td>aTopic</td>
<td>: The notification topic or subject.  
</td>
</tr>

<tr>
<td>aData</td>
<td>: Notification specific wide string.  
                   subject event.  
</td>
</tr>

</table>
