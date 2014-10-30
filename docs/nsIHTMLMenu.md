---
layout: default
---

# nsIHTMLMenu #
  
A private interface.  
All methods throw NS_ERROR_DOM_SECURITY_ERR if the caller is not chrome.  
  

## Methods ##

### sendShowEvent() ###
  
Creates and dispatches a trusted event named "show".  
The event is not cancelable and does not bubble.  
See http://www.whatwg.org/specs/web-apps/current-work/multipage/interactive-elements.html#context-menus  
  

### createBuilder() ###
  
Creates a native menu builder. The builder type is dependent on menu type.  
Currently, it returns nsXULContextMenuBuilder for context menus.  
Toolbar menus are not yet supported (the method returns null).  
  

### build(aBuilder) ###
