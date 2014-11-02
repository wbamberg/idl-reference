---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIUnicharStreamLoader.idl">Source file</a>
</div>

# nsIUnicharStreamLoader #
  
Asynchronously load a channel, converting the data to UTF-16.  
  
To use this interface, first call init() with a  
nsIUnicharStreamLoaderObserver that will be notified when the data has been  
loaded. Then call asyncOpen() on the channel with the nsIUnicharStreamLoader  
as the listener. The context argument in the asyncOpen() call will be  
passed to the onStreamComplete() callback.  
  

## Methods ##

### init(aObserver) ###
  
Initializes the unichar stream loader  
  
@param aObserver the observer to notify when a charset is needed and when  
                 the load is complete  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>the observer to notify when a charset is needed and when  
                 the load is complete  
</td>
</tr>

</table>

## Attributes ##

### channel ###
  
The channel attribute is only valid inside the onDetermineCharset  
and onStreamComplete callbacks.  Otherwise it will be null.  
  

### charset ###
  
The charset that onDetermineCharset returned, if that's been  
called.  
  
