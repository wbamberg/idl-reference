---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIDocumentEncoder.idl">Source file</a>
</div>

# nsIDocumentEncoderNodeFixup #

## Methods ##

### fixupNode(aNode, aSerializeCloneKids) ###
  
Create a fixed up version of a node. This method is called before  
each node in a document is about to be persisted. The implementor  
may return a new node with fixed up attributes or null. If null is  
returned the node should be used as-is.  
@param aNode Node to fixup.  
@param [OUT] aSerializeCloneKids True if the document encoder should  
apply recursive serialization to the children of the fixed up node  
instead of the children of the original node.  
@return The resulting fixed up node.  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>Node to fixup.  
</td>
</tr>

<tr>
<td>[OUT]</td>
<td>aSerializeCloneKids True if the document encoder should  
apply recursive serialization to the children of the fixed up node  
instead of the children of the original node.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The resulting fixed up node.  
</td>
</tr>

</table>
