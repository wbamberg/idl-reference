---
layout: default
---

# extIEvents #
  
Interface for supporting custom events.  
  

## Methods ##

### addListener(aEvent, aListener) ###
  
Adds an event listener to the list. If multiple identical event listeners  
are registered on the same event target with the same parameters the  
duplicate instances are discarded. They do not cause the EventListener  
to be called twice and since they are discarded they do not need to be  
removed with the removeListener method.  
  
@param   aEvent  
         The name of an event  
@param   aListener  
         The reference to a listener  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aEvent  
         The name of an event  
</td>
</tr>

<tr>
<td></td>
<td>aListener  
         The reference to a listener  
</td>
</tr>

</table>

### removeListener(aEvent, aListener) ###
  
Removes an event listener from the list. Calling remove  
with arguments which do not identify any currently registered  
event listener has no effect.  
@param   aEvent  
         The name of an event  
@param   aListener  
         The reference to a listener  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aEvent  
         The name of an event  
</td>
</tr>

<tr>
<td></td>
<td>aListener  
         The reference to a listener  
</td>
</tr>

</table>
