---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIEditorObserver.idl">Source file</a>
</div>
# nsIEditorObserver #
  
A generic editor observer interface.   
<P>  
nsIEditorObserver is the interface used by applications wishing to be notified  
when the editor has completed a user action.   
  
  

## Methods ##

### EditAction() ###
   
Called after the editor completes a user action.  
  

### BeforeEditAction() ###
  
Called when editor starts to handle a user action.  I.e., This must be  
called before the first DOM change.  
  

### CancelEditAction() ###
  
Called after BeforeEditAction() is called but EditorAction() won't be  
called.  
  
