---
layout: default
---

# nsIControllerContext #

## Methods ##

### init(aCommandTable) ###
  
 Init the controller, optionally passing a controller  
 command table.  
  
@param aCommandTable  a command table, used internally  
                      by this controller. May be null, in  
                      which case the controller will create  
                      a new, empty table.  
  

#### Parameters ####

<table>

<tr>
<td>aCommandTable</td>
<td>a command table, used internally  
                      by this controller. May be null, in  
                      which case the controller will create  
                      a new, empty table.  
</td>
</tr>

</table>

### setCommandContext(aCommandContext) ###
   
 Set a context on this controller, which is passed  
 to commands to give them some context when they execute.  
  
@param aCommandContext  the context passed to commands.  
                       Note that this is *not* addreffed by the  
                       controller, and so needs to outlive it,  
                       or be nulled out.  
  

#### Parameters ####

<table>

<tr>
<td>aCommandContext</td>
<td>the context passed to commands.  
                       Note that this is *not* addreffed by the  
                       controller, and so needs to outlive it,  
                       or be nulled out.  
</td>
</tr>

</table>
