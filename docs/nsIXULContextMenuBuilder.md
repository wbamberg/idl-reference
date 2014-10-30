---
layout: default
---

# nsIXULContextMenuBuilder #
  
An interface for initialization of XUL context menu builder  
and for triggering of menuitem actions with assigned identifiers.  
  

## Methods ##

### init(aDocumentFragment, aGeneratedItemIdAttrName) ###
  
Initialize builder before building.  
  
@param aDocumentFragment the fragment that will be used to append top  
       level elements  
  
@param aGeneratedItemIdAttrName the name of the attribute that will be  
       used to mark elements as generated and for menuitem identification  
  

### click(aGeneratedItemId) ###
  
Invoke the action of the menuitem with assigned id aGeneratedItemId.  
  
@param aGeneratedItemId the menuitem id  
  
