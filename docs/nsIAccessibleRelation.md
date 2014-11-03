---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleRelation.idl">Source file</a>
</div>

# nsIAccessibleRelation #
<pre>  
This interface gives access to an accessible's set of relations.  
  
</pre>
## Methods ##

### getTarget(index) ###
<pre>  
Returns one accessible relation target.  
@param index - 0 based index of relation target.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>index</td>
<td>- 0 based index of relation target.  
</td>
</tr>

</table>

### getTargets() ###
<pre>  
Returns multiple accessible relation targets.  
  
</pre>
## Attributes ##

### relationType ###
<pre>  
Returns the type of the relation.  
  
</pre>
### targetsCount ###
<pre>  
Returns the number of targets for this relation.  
  
</pre>
## Constants ##

### RELATION_LABELLED_BY ###
<pre>  
This object is labelled by a target object.  
  
</pre>
### RELATION_LABEL_FOR ###
<pre>  
This object is label for a target object.  
  
</pre>
### RELATION_DESCRIBED_BY ###
<pre>  
This object is described by the target object.  
  
</pre>
### RELATION_DESCRIPTION_FOR ###
<pre>  
This object is describes the target object.  
  
</pre>
### RELATION_NODE_CHILD_OF ###
<pre>  
This object is a child of a target object.  
  
</pre>
### RELATION_NODE_PARENT_OF ###
<pre>  
This object is a parent of a target object. A dual relation to  
RELATION_NODE_CHILD_OF  
  
</pre>
### RELATION_CONTROLLED_BY ###
<pre>  
Some attribute of this object is affected by a target object.  
  
</pre>
### RELATION_CONTROLLER_FOR ###
<pre>  
This object is interactive and controls some attribute of a target object.  
  
</pre>
### RELATION_FLOWS_TO ###
<pre>  
Content flows from this object to a target object, i.e. has content that  
flows logically to another object in a sequential way, e.g. text flow.  
  
</pre>
### RELATION_FLOWS_FROM ###
<pre>  
Content flows to this object from a target object, i.e. has content that  
flows logically from another object in a sequential way, e.g. text flow.  
  
</pre>
### RELATION_MEMBER_OF ###
<pre>  
This object is a member of a group of one or more objects. When there is  
more than one object in the group each member may have one and the same  
target, e.g. a grouping object.  It is also possible that each member has  
multiple additional targets, e.g. one for every other member in the group.  
  
</pre>
### RELATION_SUBWINDOW_OF ###
<pre>  
This object is a sub window of a target object.  
  
</pre>
### RELATION_EMBEDS ###
<pre>  
This object embeds a target object. This relation can be used on the  
OBJID_CLIENT accessible for a top level window to show where the content  
areas are.  
  
</pre>
### RELATION_EMBEDDED_BY ###
<pre>  
This object is embedded by a target object.  
  
</pre>
### RELATION_POPUP_FOR ###
<pre>  
This object is a transient component related to the target object. When  
this object is activated the target object doesn't lose focus.  
  
</pre>
### RELATION_PARENT_WINDOW_OF ###
<pre>  
This object is a parent window of the target object.  
  
</pre>
### RELATION_DEFAULT_BUTTON ###
<pre>  
Part of a form/dialog with a related default button. It is used for  
MSAA/XPCOM, it isn't for IA2 or ATK.  
  
</pre>
### RELATION_CONTAINING_DOCUMENT ###
<pre>  
The target object is the containing document object.  
  
</pre>
### RELATION_CONTAINING_TAB_PANE ###
<pre>  
The target object is the topmost containing document object in the tab pane.  
  
</pre>
### RELATION_CONTAINING_APPLICATION ###
<pre>  
The target object is the containing application object.  
  
</pre>