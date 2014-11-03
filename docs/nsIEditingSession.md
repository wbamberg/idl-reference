---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/composer/nsIEditingSession.idl">Source file</a>
</div>

# nsIEditingSession #

## Methods ##

### makeWindowEditable(window, aEditorType, doAfterUriLoad, aMakeWholeDocumentEditable, aInteractive) ###
<pre>  
 Make this window editable  
 @param aWindow nsIDOMWindow, the window the embedder needs to make editable  
 @param aEditorType string, "html" "htmlsimple" "text" "textsimple"  
 @param aMakeWholeDocumentEditable if PR_TRUE make the whole document in  
                                   aWindow editable, otherwise it's the  
                                   embedder who should make the document  
                                   (or part of it) editable.  
 @param aInteractive if PR_FALSE turn off scripting and plugins  
  
</pre>
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
<pre>  
 Test whether a specific window has had its editable flag set; it may have an editor  
 now, or will get one after the uri load.  
   
 Use this, passing the content root window, to test if we've set up editing  
 for this content.  
  
</pre>
### getEditorForWindow(window) ###
<pre>  
 Get the editor for this window. May return null  
  
</pre>
### setupEditorOnWindow(window) ###
<pre>   
 Setup editor and related support objects  
  
</pre>
### tearDownEditorOnWindow(window) ###
<pre>   
  Destroy editor and related support objects  
  
</pre>
### setEditorOnControllers(aWindow, aEditor) ###

### disableJSAndPlugins(aWindow) ###
<pre>  
Disable scripts and plugins in aWindow.  
  
</pre>
### restoreJSAndPlugins(aWindow) ###
<pre>  
Restore JS and plugins (enable/disable them) according to the state they  
were before the last call to disableJSAndPlugins.  
  
</pre>
### detachFromWindow(aWindow) ###
<pre>  
Removes all the editor's controllers/listeners etc and makes the window  
uneditable.  
  
</pre>
### reattachToWindow(aWindow) ###
<pre>  
Undos detachFromWindow(), reattaches this editing session/editor  
to the window.  
  
</pre>
## Attributes ##

### editorStatus ###
<pre>  
 Status after editor creation and document loading  
 Value is one of the above error codes  
  
</pre>
### jsAndPluginsDisabled ###
<pre>  
Whether this session has disabled JS and plugins.  
  
</pre>
## Constants ##

### eEditorOK ###
<pre>  
 Error codes when we fail to create an editor  
 is placed in attribute editorStatus  
  
</pre>
### eEditorCreationInProgress ###

### eEditorErrorCantEditMimeType ###

### eEditorErrorFileNotFound ###

### eEditorErrorCantEditFramesets ###

### eEditorErrorUnknown ###
