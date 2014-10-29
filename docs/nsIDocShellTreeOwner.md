---
layout: default
---

# nsIDocShellTreeOwner #

## findItemWithName ##

## contentShellAdded ##

Called when a content shell is added to the docshell tree.  This is
_only_ called for "root" content shells (that is, ones whose parent is a
chrome shell).

@param aContentShell the shell being added.
@param aPrimary whether the shell is primary.
@param aTargetable whether the shell can be a target for named window
				targeting.
@param aID the "id" of the shell.  What this actually means is
		undefined. Don't rely on this for anything.


## contentShellRemoved ##

Called when a content shell is removed from the docshell tree.  This is
_only_ called for "root" content shells (that is, ones whose parent is a
chrome shell).  Note that if aContentShell was never added,
contentShellRemoved should just do nothing.

@param aContentShell the shell being removed.


## primaryContentShell ##

## sizeShellTo ##

## setPersistence ##

## getPersistence ##

## targetableShellCount ##
