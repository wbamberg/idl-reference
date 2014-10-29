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

### makeImmutable ###

Make this command table immutable, so that commands cannot
be registered or unregistered. Some command tables are made
mutable after command registration so that they can be 
used as singletons.


### registerCommand ###

Register and unregister commands with the command table.

@param aCommandName  the name of the command under which to register or
                     unregister the given command handler.

@param aCommand      the handler for this command.


### unregisterCommand ###

### findCommandHandler ###

Find the command handler which has been registered to handle the named command.

@param aCommandName  the name of the command to find the handler for.


### isCommandEnabled ###

Get whether the named command is enabled.

@param aCommandName    the name of the command to test
@param aCommandRefCon  the command context data


### updateCommandState ###

Tell the command to update its state (if it is a state updating command)

@param aCommandName    the name of the command to update
@param aCommandRefCon  the command context data


### supportsCommand ###

Get whether the named command is supported.

@param aCommandName    the name of the command to test
@param aCommandRefCon  the command context data


### doCommand ###

Execute the named command.

@param aCommandName    the name of the command to execute
@param aCommandRefCon  the command context data


### doCommandParams ###

### getCommandState ###
