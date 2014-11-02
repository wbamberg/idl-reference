---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIDOMChromeWindow.idl">Source file</a>
</div>
# nsIDOMChromeWindow #

## Methods ##

### getAttention() ###

### getAttentionWithCycleCount(aCycleCount) ###

### setCursor(cursor) ###

### maximize() ###

### minimize() ###

### restore() ###

### notifyDefaultButtonLoaded(defaultButton) ###
  
Notify a default button is loaded on a dialog or a wizard.  
defaultButton is the default button.  
  

### getGroupMessageManager(group) ###
  
Returns the message manager identified by the given group name that  
manages all frame loaders belonging to that group.  
  

### beginWindowMove(mouseDownEvent, panel) ###
  
On some operating systems, we must allow the window manager to  
handle window dragging. This function tells the window manager to  
start dragging the window. This function will fail unless called  
while the left mouse button is held down, callers must check this.  
  
The optional panel argument should be set when moving a panel.  
  
Returns NS_ERROR_NOT_IMPLEMENTED (and thus throws in JS) if the OS  
doesn't support this.  
  

## Attributes ##

### windowState ###

### browserDOMWindow ###
  
browserDOMWindow provides access to yet another layer of  
utility functions implemented by chrome script. It will be null  
for DOMWindows not corresponding to browsers.  
  

### messageManager ###

## Constants ##

### STATE_MAXIMIZED ###

### STATE_MINIMIZED ###

### STATE_NORMAL ###

### STATE_FULLSCREEN ###
