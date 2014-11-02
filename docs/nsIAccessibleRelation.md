---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleRelation.idl">Source file</a>
</div>

# nsIAccessibleRelation #
  
This interface gives access to an accessible's set of relations.  
  

## Methods ##

### getTarget(index) ###
  
Returns one accessible relation target.  
@param index - 0 based index of relation target.  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>- 0 based index of relation target.  
</td>
</tr>

</table>

### getTargets() ###
  
Returns multiple accessible relation targets.  
  

## Attributes ##

### relationType ###
  
Returns the type of the relation.  
  

### targetsCount ###
  
Returns the number of targets for this relation.  
  

## Constants ##

### RELATION_LABELLED_BY ###
  
This object is labelled by a target object.  
  

### RELATION_LABEL_FOR ###
  
This object is label for a target object.  
  

### RELATION_DESCRIBED_BY ###
  
This object is described by the target object.  
  

### RELATION_DESCRIPTION_FOR ###
  
This object is describes the target object.  
  

### RELATION_NODE_CHILD_OF ###
  
This object is a child of a target object.  
  

### RELATION_NODE_PARENT_OF ###
  
This object is a parent of a target object. A dual relation to  
RELATION_NODE_CHILD_OF  
  

### RELATION_CONTROLLED_BY ###
  
Some attribute of this object is affected by a target object.  
  

### RELATION_CONTROLLER_FOR ###
  
This object is interactive and controls some attribute of a target object.  
  

### RELATION_FLOWS_TO ###
  
Content flows from this object to a target object, i.e. has content that  
flows logically to another object in a sequential way, e.g. text flow.  
  

### RELATION_FLOWS_FROM ###
  
Content flows to this object from a target object, i.e. has content that  
flows logically from another object in a sequential way, e.g. text flow.  
  

### RELATION_MEMBER_OF ###
  
This object is a member of a group of one or more objects. When there is  
more than one object in the group each member may have one and the same  
target, e.g. a grouping object.  It is also possible that each member has  
multiple additional targets, e.g. one for every other member in the group.  
  

### RELATION_SUBWINDOW_OF ###
  
This object is a sub window of a target object.  
  

### RELATION_EMBEDS ###
  
This object embeds a target object. This relation can be used on the  
OBJID_CLIENT accessible for a top level window to show where the content  
areas are.  
  

### RELATION_EMBEDDED_BY ###
  
This object is embedded by a target object.  
  

### RELATION_POPUP_FOR ###
  
This object is a transient component related to the target object. When  
this object is activated the target object doesn't lose focus.  
  

### RELATION_PARENT_WINDOW_OF ###
  
This object is a parent window of the target object.  
  

### RELATION_DEFAULT_BUTTON ###
  
Part of a form/dialog with a related default button. It is used for  
MSAA/XPCOM, it isn't for IA2 or ATK.  
  

### RELATION_CONTAINING_DOCUMENT ###
  
The target object is the containing document object.  
  

### RELATION_CONTAINING_TAB_PANE ###
  
The target object is the topmost containing document object in the tab pane.  
  

### RELATION_CONTAINING_APPLICATION ###
  
The target object is the containing application object.  
  
