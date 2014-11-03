---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/composer/nsIEditingSession.idl">Source file</a>
</div>

# nsIEditingSession #

## Methods ##

### makeWindowEditable(window, aEditorType, doAfterUriLoad, aMakeWholeDocumentEditable, aInteractive) ###
<code>  
 Make this window editable  
 @param aWindow nsIDOMWindow, the window the embedder needs to make editable  
 @param aEditorType string, "html" "htmlsimple" "text" "textsimple"  
 @param aMakeWholeDocumentEditable if PR_TRUE make the whole document in  
                                   aWindow editable, otherwise it's the  
                                   embedder who should make the document  
                                   (or part of it) editable.  
 @param aInteractive if PR_FALSE turn off scripting and plugins  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>nsIDOMWindow, the window the embedder needs to make editable  
</td>
</tr>

<tr>
<td>aEditorType</td>
<td>string, "html" "htmlsimple" "text" "textsimple"  
</td>
</tr>

<tr>
<td>aMakeWholeDocumentEditable</td>
<td>if PR_TRUE make the whole document in  
                                   aWindow editable, otherwise it's the  
                                   embedder who should make the document  
                                   (or part of it) editable.  
</td>
</tr>

<tr>
<td>aInteractive</td>
<td>if PR_FALSE turn off scripting and plugins  
</td>
</tr>

</table>

### windowIsEditable(window) ###
<code>  
 Test whether a specific window has had its editable flag set; it may have an editor  
 now, or will get one after the uri load.  
   
 Use this, passing the content root window, to test if we've set up editing  
 for this content.  
  
</code>
### getEditorForWindow(window) ###
<code>  
 Get the editor for this window. May return null  
  
</code>
### setupEditorOnWindow(window) ###
<code>   
 Setup editor and related support objects  
  
</code>
### tearDownEditorOnWindow(window) ###
<code>   
  Destroy editor and related support objects  
  
</code>
### setEditorOnControllers(aWindow, aEditor) ###

### disableJSAndPlugins(aWindow) ###
<code>  
Disable scripts and plugins in aWindow.  
  
</code>
### restoreJSAndPlugins(aWindow) ###
<code>  
Restore JS and plugins (enable/disable them) according to the state they  
were before the last call to disableJSAndPlugins.  
  
</code>
### detachFromWindow(aWindow) ###
<code>  
Removes all the editor's controllers/listeners etc and makes the window  
uneditable.  
  
</code>
### reattachToWindow(aWindow) ###
<code>  
Undos detachFromWindow(), reattaches this editing session/editor  
to the window.  
  
</code>
## Attributes ##

### editorStatus ###
  
 Status after editor creation and document loading  
 Value is one of the above error codes  
  

### jsAndPluginsDisabled ###
  
Whether this session has disabled JS and plugins.  
  

## Constants ##

### eEditorOK ###
  
 Error codes when we fail to create an editor  
 is placed in attribute editorStatus  
  

### eEditorCreationInProgress ###

### eEditorErrorCantEditMimeType ###

### eEditorErrorFileNotFound ###

### eEditorErrorCantEditFramesets ###

### eEditorErrorUnknown ###
