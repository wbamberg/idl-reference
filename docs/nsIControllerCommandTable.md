---
layout: default
---

# nsIControllerCommandTable #
  
nsIControllerCommandTable  
  
An interface via which a controller can maintain a series of commands,  
and efficiently dispatch commands to their respective handlers.  
  
Controllers that use an nsIControllerCommandTable should support  
nsIInterfaceRequestor, and be able to return an interface to their  
controller command table via getInterface().  
  
  

## Methods ##

### makeImmutable() ###
  
Make this command table immutable, so that commands cannot  
be registered or unregistered. Some command tables are made  
mutable after command registration so that they can be   
used as singletons.  
  

### registerCommand(aCommandName, aCommand) ###
  
Register and unregister commands with the command table.  
  
@param aCommandName  the name of the command under which to register or  
                     unregister the given command handler.  
  
@param aCommand      the handler for this command.  
  

#### Parameters ####

<table>

<tr>
<td>aCommandName</td>
<td>the name of the command under which to register or  
                     unregister the given command handler.  
</td>
</tr>

<tr>
<td>aCommand</td>
<td>the handler for this command.  
</td>
</tr>

</table>

### unregisterCommand(aCommandName, aCommand) ###

### findCommandHandler(aCommandName) ###
  
Find the command handler which has been registered to handle the named command.  
  
@param aCommandName  the name of the command to find the handler for.  
  

#### Parameters ####

<table>

<tr>
<td>aCommandName</td>
<td>the name of the command to find the handler for.  
</td>
</tr>

</table>

### isCommandEnabled(aCommandName, aCommandRefCon) ###
  
Get whether the named command is enabled.  
  
@param aCommandName    the name of the command to test  
@param aCommandRefCon  the command context data  
  

#### Parameters ####

<table>

<tr>
<td>aCommandName</td>
<td>the name of the command to test  
</td>
</tr>

<tr>
<td>aCommandRefCon</td>
<td>the command context data  
</td>
</tr>

</table>

### updateCommandState(aCommandName, aCommandRefCon) ###
  
Tell the command to update its state (if it is a state updating command)  
  
@param aCommandName    the name of the command to update  
@param aCommandRefCon  the command context data  
  

#### Parameters ####

<table>

<tr>
<td>aCommandName</td>
<td>the name of the command to update  
</td>
</tr>

<tr>
<td>aCommandRefCon</td>
<td>the command context data  
</td>
</tr>

</table>

### supportsCommand(aCommandName, aCommandRefCon) ###
  
Get whether the named command is supported.  
  
@param aCommandName    the name of the command to test  
@param aCommandRefCon  the command context data  
  

#### Parameters ####

<table>

<tr>
<td>aCommandName</td>
<td>the name of the command to test  
</td>
</tr>

<tr>
<td>aCommandRefCon</td>
<td>the command context data  
</td>
</tr>

</table>

### doCommand(aCommandName, aCommandRefCon) ###
  
Execute the named command.  
  
@param aCommandName    the name of the command to execute  
@param aCommandRefCon  the command context data  
  

#### Parameters ####

<table>

<tr>
<td>aCommandName</td>
<td>the name of the command to execute  
</td>
</tr>

<tr>
<td>aCommandRefCon</td>
<td>the command context data  
</td>
</tr>

</table>

### doCommandParams(aCommandName, aParam, aCommandRefCon) ###

### getCommandState(aCommandName, aParam, aCommandRefCon) ###
