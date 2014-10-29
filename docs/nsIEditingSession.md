---
layout: default
---

# nsIEditingSession #

## eEditorOK ##

 Error codes when we fail to create an editor
 is placed in attribute editorStatus


## eEditorCreationInProgress ##

## eEditorErrorCantEditMimeType ##

## eEditorErrorFileNotFound ##

## eEditorErrorCantEditFramesets ##

## eEditorErrorUnknown ##

## editorStatus ##

 Status after editor creation and document loading
 Value is one of the above error codes


## makeWindowEditable ##

 Make this window editable
 @param aWindow nsIDOMWindow, the window the embedder needs to make editable
 @param aEditorType string, "html" "htmlsimple" "text" "textsimple"
 @param aMakeWholeDocumentEditable if PR_TRUE make the whole document in
                                   aWindow editable, otherwise it's the
                                   embedder who should make the document
                                   (or part of it) editable.
 @param aInteractive if PR_FALSE turn off scripting and plugins


## windowIsEditable ##

 Test whether a specific window has had its editable flag set; it may have an editor
 now, or will get one after the uri load.
 
 Use this, passing the content root window, to test if we've set up editing
 for this content.


## getEditorForWindow ##

 Get the editor for this window. May return null


## setupEditorOnWindow ##
 
 Setup editor and related support objects


## tearDownEditorOnWindow ##
 
  Destroy editor and related support objects


## setEditorOnControllers ##

## disableJSAndPlugins ##

Disable scripts and plugins in aWindow.


## restoreJSAndPlugins ##

Restore JS and plugins (enable/disable them) according to the state they
were before the last call to disableJSAndPlugins.


## detachFromWindow ##

Removes all the editor's controllers/listeners etc and makes the window
uneditable.


## reattachToWindow ##

Undos detachFromWindow(), reattaches this editing session/editor
to the window.


## jsAndPluginsDisabled ##

Whether this session has disabled JS and plugins.

