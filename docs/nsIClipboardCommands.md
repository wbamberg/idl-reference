---
layout: default
---

# nsIClipboardCommands #

An interface for embedding clients who wish to interact with
the system-wide OS clipboard. Mozilla does not use a private
clipboard, instead it places its data directly onto the system 
clipboard. The webshell implements this interface.


## canCutSelection ##

Returns whether there is a selection and it is not read-only.

@return <code>true</code> if the current selection can be cut,
         <code>false</code> otherwise.


## canCopySelection ##

Returns whether there is a selection and it is copyable.

@return <code>true</code> if there is a selection,
         <code>false</code> otherwise.


## canCopyLinkLocation ##

Returns whether we can copy a link location.

@return <code>true</code> if a link is selected,
          <code>false</code> otherwise.


## canCopyImageLocation ##

Returns whether we can copy an image location.

@return <code>true</code> if an image is selected,
<code>false</code> otherwise.


## canCopyImageContents ##

Returns whether we can copy an image's contents.

@return <code>true</code> if an image is selected,
         <code>false</code> otherwise


## canPaste ##

Returns whether the current contents of the clipboard can be
pasted and if the current selection is not read-only.

@return <code>true</code> there is data to paste on the clipboard
         and the current selection is not read-only,
         <code>false</code> otherwise


## cutSelection ##

Cut the current selection onto the clipboard.


## copySelection ##

Copy the current selection onto the clipboard.


## copyLinkLocation ##

Copy the link location of the current selection (e.g.,
the |href| attribute of a selected |a| tag).


## copyImageLocation ##

Copy the location of the selected image.


## copyImageContents ##

Copy the contents of the selected image.


## paste ##

Paste the contents of the clipboard into the current selection.


## selectAll ##

Select the entire contents.


## selectNone ##

Clear the current selection (if any). Insertion point ends up
at beginning of current selection.

