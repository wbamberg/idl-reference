---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIEvents #
<code>  
Interface for supporting custom events.  
  
</code>
## Methods ##

### addListener(aEvent, aListener) ###
<code>  
Adds an event listener to the list. If multiple identical event listeners  
are registered on the same event target with the same parameters the  
duplicate instances are discarded. They do not cause the EventListener  
to be called twice and since they are discarded they do not need to be  
removed with the removeListener method.  
  
@param   aEvent  
         The name of an event  
@param   aListener  
         The reference to a listener  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aEvent</td>
<td>         The name of an event  
</td>
</tr>

<tr>
<td>aListener</td>
<td>         The reference to a listener  
</td>
</tr>

</table>

### removeListener(aEvent, aListener) ###
<code>  
Removes an event listener from the list. Calling remove  
with arguments which do not identify any currently registered  
event listener has no effect.  
@param   aEvent  
         The name of an event  
@param   aListener  
         The reference to a listener  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aEvent</td>
<td>         The name of an event  
</td>
</tr>

<tr>
<td>aListener</td>
<td>         The reference to a listener  
</td>
</tr>

</table>
