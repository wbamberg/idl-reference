---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xul/nsIXULContextMenuBuilder.idl">Source file</a>
</div>

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
  

#### Parameters ####

<table>

<tr>
<td>aDocumentFragment</td>
<td>the fragment that will be used to append top  
       level elements  
</td>
</tr>

<tr>
<td>aGeneratedItemIdAttrName</td>
<td>the name of the attribute that will be  
       used to mark elements as generated and for menuitem identification  
</td>
</tr>

</table>

### click(aGeneratedItemId) ###
  
Invoke the action of the menuitem with assigned id aGeneratedItemId.  
  
@param aGeneratedItemId the menuitem id  
  

#### Parameters ####

<table>

<tr>
<td>aGeneratedItemId</td>
<td>the menuitem id  
</td>
</tr>

</table>
