---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/components/commandhandler/nsIControllerCommand.idl">Source file</a>
</div>

# nsIControllerCommand #
<code>  
nsIControllerCommand  
  
A generic command interface. You can register an nsIControllerCommand  
with the nsIControllerCommandTable.  
  
</code>
## Methods ##

### isCommandEnabled(aCommandName, aCommandContext) ###
<code>  
Returns true if the command is currently enabled. An nsIControllerCommand  
can implement more than one commands; say, a group of related commands  
(e.g. delete left/delete right). Because of this, the command name is  
passed to each method.  
  
@param aCommandName  the name of the command for which we want the enabled  
                     state.  
@param aCommandContext    a cookie held by the nsIControllerCommandTable,  
                 allowing the command to get some context information.  
                 The contents of this cookie are implementation-defined.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aCommandName</td>
<td>the name of the command for which we want the enabled  
                     state.  
</td>
</tr>

<tr>
<td>aCommandContext</td>
<td>a cookie held by the nsIControllerCommandTable,  
                 allowing the command to get some context information.  
                 The contents of this cookie are implementation-defined.  
</td>
</tr>

</table>

### getCommandStateParams(aCommandName, aParams, aCommandContext) ###

### doCommand(aCommandName, aCommandContext) ###
<code>  
Execute the name command.  
  
@param aCommandName  the name of the command to execute.  
  
@param aCommandContext    a cookie held by the nsIControllerCommandTable,  
                 allowing the command to get some context information.  
                 The contents of this cookie are implementation-defined.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aCommandName</td>
<td>the name of the command to execute.  
</td>
</tr>

<tr>
<td>aCommandContext</td>
<td>a cookie held by the nsIControllerCommandTable,  
                 allowing the command to get some context information.  
                 The contents of this cookie are implementation-defined.  
</td>
</tr>

</table>

### doCommandParams(aCommandName, aParams, aCommandContext) ###
