---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIDocShellTreeItem.idl">Source file</a>
</div>
# nsIDocShellTreeItem #
  
The nsIDocShellTreeItem supplies the methods that are required of any item  
that wishes to be able to live within the docshell tree either as a middle  
node or a leaf.   
  

## Methods ##

### nameEquals(name) ###
  
Compares the provided name against the item's name and  
returns the appropriate result.  
  
@return <CODE>PR_TRUE</CODE> if names match;  
        <CODE>PR_FALSE</CODE> otherwise.  
  

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
  
Return the child at the index requested.  This is 0-based.  
  
@throws NS_ERROR_UNEXPECTED if the index is out of range  
  

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
