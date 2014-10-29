---
layout: default
---

# nsIDocShellTreeItem #

The nsIDocShellTreeItem supplies the methods that are required of any item
that wishes to be able to live within the docshell tree either as a middle
node or a leaf. 


## name ##

## nameEquals ##

Compares the provided name against the item's name and
returns the appropriate result.

@return <CODE>PR_TRUE</CODE> if names match;
        <CODE>PR_FALSE</CODE> otherwise.


## typeChrome ##

## typeContent ##

## typeContentWrapper ##

## typeChromeWrapper ##

## typeAll ##

## itemType ##

## ItemType ##

## parent ##

## sameTypeParent ##

## rootTreeItem ##

## sameTypeRootTreeItem ##

## findItemWithName ##

## treeOwner ##

## setTreeOwner ##

## childCount ##

## addChild ##

## removeChild ##

## getChildAt ##

Return the child at the index requested.  This is 0-based.

@throws NS_ERROR_UNEXPECTED if the index is out of range


## findChildWithName ##

## getDocument ##

## getWindow ##
