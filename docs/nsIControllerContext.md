---
layout: default
---

# nsIControllerContext #

## Methods ##

### init ###
  
 Init the controller, optionally passing a controller  
 command table.  
  
@param aCommandTable  a command table, used internally  
                      by this controller. May be null, in  
                      which case the controller will create  
                      a new, empty table.  
  

### setCommandContext ###
   
 Set a context on this controller, which is passed  
 to commands to give them some context when they execute.  
  
@param aCommandContext  the context passed to commands.  
                       Note that this is *not* addreffed by the  
                       controller, and so needs to outlive it,  
                       or be nulled out.  
  
