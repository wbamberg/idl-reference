---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIDocShellTreeItem.idl">Source file</a>
</div>

# nsIDocShellTreeItem #
<code>  
The nsIDocShellTreeItem supplies the methods that are required of any item  
that wishes to be able to live within the docshell tree either as a middle  
node or a leaf.   
  
</code>
## Methods ##

### nameEquals(name) ###
<code>  
Compares the provided name against the item's name and  
returns the appropriate result.  
  
@return <CODE>PR_TRUE</CODE> if names match;  
        <CODE>PR_FALSE</CODE> otherwise.  
  
</code>
#### Returns ####

<table>

<tr>
<td><CODE>PR_TRUE</CODE> if names match;  
        <CODE>PR_FALSE</CODE> otherwise.  
</td>
</tr>

</table>

### ItemType() ###

### findItemWithName(name, aRequestor, aOriginalRequestor) ###

### setTreeOwner(treeOwner) ###

### addChild(child) ###

### removeChild(child) ###

### getChildAt(index) ###
<code>  
Return the child at the index requested.  This is 0-based.  
  
@throws NS_ERROR_UNEXPECTED if the index is out of range  
  
</code>
### findChildWithName(aName, aRecurse, aSameType, aRequestor, aOriginalRequestor) ###

### getDocument() ###

### getWindow() ###

## Attributes ##

### name ###

### itemType ###

### parent ###

### sameTypeParent ###

### rootTreeItem ###

### sameTypeRootTreeItem ###

### treeOwner ###

### childCount ###

## Constants ##

### typeChrome ###

### typeContent ###

### typeContentWrapper ###

### typeChromeWrapper ###

### typeAll ###
