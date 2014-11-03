---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/html/nsIMenuBuilder.idl">Source file</a>
</div>

# nsIMenuBuilder #
<code>  
An interface used to construct native toolbar or context menus from <menu>  
  
</code>
## Methods ##

### openContainer(aLabel) ###
<code>  
Create the top level menu or a submenu. The implementation should create  
a new context for this menu, so all subsequent methods will add new items  
to this newly created menu.  
  
</code>
### addItemFor(aElement, aCanLoadIcon) ###
<code>  
Add a new menu item. All menu item details can be obtained from  
the element. This method is not called for hidden elements or elements  
with no or empty label. The icon should be loaded only if aCanLoadIcon  
is true.  
  
</code>
### addSeparator() ###
<code>  
Create a new separator.  
  
</code>
### undoAddSeparator() ###
<code>  
Remove last added separator.  
Sometimes it's needed to remove last added separator, otherwise it's not  
possible to implement the postprocessing in one pass.  
See http://www.whatwg.org/specs/web-apps/current-work/multipage/interactive-elements.html#building-menus-and-toolbars  
  
</code>
### closeContainer() ###
<code>  
Set the context to the parent menu.  
  
</code>