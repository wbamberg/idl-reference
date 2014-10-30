---
layout: default
---

# nsIWebBrowserFocus #
  
nsIWebBrowserFocus  
Interface that embedders use for controlling and interacting  
with the browser focus management. The embedded browser can be focused by  
clicking in it or tabbing into it. If the browser is currently focused and  
the embedding application's top level window is disabled, deactivate() must  
be called, and activate() called again when the top level window is  
reactivated for the browser's focus memory to work correctly.  
  

## Methods ##

### activate ###
  
MANDATORY  
activate() is a mandatory call that must be made to the browser  
when the embedding application's window is activated *and* the   
browser area was the last thing in focus.  This method can also be called  
if the embedding application wishes to give the browser area focus,  
without affecting the currently focused element within the browser.  
  
@note  
If you fail to make this call, mozilla focus memory will not work  
correctly.  
  

### deactivate ###
  
MANDATORY  
deactivate() is a mandatory call that must be made to the browser  
when the embedding application's window is deactivated *and* the  
browser area was the last thing in focus.  On non-windows platforms,  
deactivate() should also be called when focus moves from the browser  
to the embedding chrome.  
  
@note  
If you fail to make this call, mozilla focus memory will not work  
correctly.  
  

### setFocusAtFirstElement ###
  
Give the first element focus within mozilla  
(i.e. TAB was pressed and focus should enter mozilla)  
  

### setFocusAtLastElement ###
  
Give the last element focus within mozilla  
(i.e. SHIFT-TAB was pressed and focus should enter mozilla)  
  

## Attributes ##

### focusedWindow ###
  
The currently focused nsDOMWindow when the browser is active,  
or the last focused nsDOMWindow when the browser is inactive.  
  

### focusedElement ###
  
The currently focused nsDOMElement when the browser is active,  
or the last focused nsDOMElement when the browser is inactive.  
  
