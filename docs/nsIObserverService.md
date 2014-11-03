---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIObserverService.idl">Source file</a>
</div>

# nsIObserverService #
<pre>  
nsIObserverService  
  
Service allows a client listener (nsIObserver) to register and unregister for   
notifications of specific string referenced topic. Service also provides a   
way to notify registered listeners and a way to enumerate registered client   
listeners.  
  
</pre>
## Methods ##

### addObserver(anObserver, aTopic, ownsWeak) ###
<pre>  
AddObserver  
  
Registers a given listener for a notifications regarding the specified  
topic.  
  
@param anObserve : The interface pointer which will receive notifications.  
@param aTopic    : The notification topic or subject.  
@param ownsWeak  : If set to false, the nsIObserverService will hold a   
                   strong reference to |anObserver|.  If set to true and   
                   |anObserver| supports the nsIWeakReference interface,  
                   a weak reference will be held.  Otherwise an error will be  
                   returned.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>anObserve</td>
<td>: The interface pointer which will receive notifications.  
</td>
</tr>

<tr>
<td>aTopic</td>
<td>: The notification topic or subject.  
</td>
</tr>

<tr>
<td>ownsWeak</td>
<td>: If set to false, the nsIObserverService will hold a   
                   strong reference to |anObserver|.  If set to true and   
                   |anObserver| supports the nsIWeakReference interface,  
                   a weak reference will be held.  Otherwise an error will be  
                   returned.  
</td>
</tr>

</table>

### removeObserver(anObserver, aTopic) ###
<pre>  
removeObserver  
  
Unregisters a given listener from notifications regarding the specified  
topic.  
  
@param anObserver : The interface pointer which will stop recieving  
                    notifications.  
@param aTopic     : The notification topic or subject.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>anObserver</td>
<td>: The interface pointer which will stop recieving  
                    notifications.  
</td>
</tr>

<tr>
<td>aTopic</td>
<td>: The notification topic or subject.  
</td>
</tr>

</table>

### notifyObservers(aSubject, aTopic, someData) ###
<pre>  
notifyObservers  
  
Notifies all registered listeners of the given topic.  
  
@param aSubject : Notification specific interface pointer.  
@param aTopic   : The notification topic or subject.  
@param someData : Notification specific wide string.  
  
</pre>
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
<td>someData</td>
<td>: Notification specific wide string.  
</td>
</tr>

</table>

### enumerateObservers(aTopic) ###
<pre>  
enumerateObservers  
  
Returns an enumeration of all registered listeners.  
  
@param aTopic   : The notification topic or subject.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aTopic</td>
<td>: The notification topic or subject.  
</td>
</tr>

</table>
