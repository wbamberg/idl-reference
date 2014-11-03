---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/events/nsIDOMEventListener.idl">Source file</a>
</div>

# nsIDOMEventListener #
<code>  
The nsIDOMEventListener interface is a callback interface for  
listening to events in the Document Object Model.  
  
For more information on this interface please see   
http://www.w3.org/TR/DOM-Level-2-Events/  
  
</code>
## Methods ##

### handleEvent(event) ###
<code>  
This method is called whenever an event occurs of the type for which   
the EventListener interface was registered.  
  
@param   evt The Event contains contextual information about the   
             event. It also contains the stopPropagation and   
             preventDefault methods which are used in determining the   
             event's flow and default action.  
  
</code>
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
