---
layout: default
---

# nsIDOMChromeWindow #

## Methods ##

### getAttention ###

### getAttentionWithCycleCount ###

### setCursor ###

### maximize ###

### minimize ###

### restore ###

### notifyDefaultButtonLoaded ###
  
Notify a default button is loaded on a dialog or a wizard.  
defaultButton is the default button.  
  

### getGroupMessageManager ###
  
Returns the message manager identified by the given group name that  
manages all frame loaders belonging to that group.  
  

### beginWindowMove ###
  
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
