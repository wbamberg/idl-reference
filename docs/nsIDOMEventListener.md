---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/events/nsIDOMEventListener.idl">Source file</a>
</div>
# nsIDOMEventListener #
  
The nsIDOMEventListener interface is a callback interface for  
listening to events in the Document Object Model.  
  
For more information on this interface please see   
http://www.w3.org/TR/DOM-Level-2-Events/  
  

## Methods ##

### handleEvent(event) ###
  
This method is called whenever an event occurs of the type for which   
the EventListener interface was registered.  
  
@param   evt The Event contains contextual information about the   
             event. It also contains the stopPropagation and   
             preventDefault methods which are used in determining the   
             event's flow and default action.  
  

#### Parameters ####

<table>

<tr>
<td>evt</td>
<td>The Event contains contextual information about the   
             event. It also contains the stopPropagation and   
             preventDefault methods which are used in determining the   
             event's flow and default action.  
</td>
</tr>

</table>
