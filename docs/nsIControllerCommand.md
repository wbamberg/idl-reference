---
layout: default
---

# nsIControllerCommand #

nsIControllerCommand

A generic command interface. You can register an nsIControllerCommand
with the nsIControllerCommandTable.


## Methods ##

### isCommandEnabled ###

Returns true if the command is currently enabled. An nsIControllerCommand
can implement more than one commands; say, a group of related commands
(e.g. delete left/delete right). Because of this, the command name is
passed to each method.

@param aCommandName  the name of the command for which we want the enabled
                     state.
@param aCommandContext    a cookie held by the nsIControllerCommandTable,
                 allowing the command to get some context information.
                 The contents of this cookie are implementation-defined.


### getCommandStateParams ###

### doCommand ###

Execute the name command.

@param aCommandName  the name of the command to execute.

@param aCommandContext    a cookie held by the nsIControllerCommandTable,
                 allowing the command to get some context information.
                 The contents of this cookie are implementation-defined.


### doCommandParams ###
