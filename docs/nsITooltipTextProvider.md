---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsITooltipTextProvider.idl">Source file</a>
</div>

# nsITooltipTextProvider #
  
An interface implemented by a tooltip text provider service. This  
service is called to discover what tooltip text is associated  
with the node that the pointer is positioned over.  
  
Embedders may implement and register their own tooltip text provider  
service if they wish to provide different tooltip text.   
  
The default service returns the text stored in the TITLE  
attribute of the node or a containing parent.  
  
@note  
The tooltip text provider service is registered with the contract  
defined in NS_TOOLTIPTEXTPROVIDER_CONTRACTID.  
  
@see nsITooltipListener  
@see nsIComponentManager  
@see nsIDOMNode  
  

## Methods ##

### getNodeText(aNode, aText) ###
  
Called to obtain the tooltip text for a node.  
  
@arg aNode The node to obtain the text from.  
@arg aText The tooltip text.  
  
@return <CODE>PR_TRUE</CODE> if tooltip text is associated  
        with the node and was returned in the aText argument;  
        <CODE>PR_FALSE</CODE> otherwise.  
  

#### Returns ####

<table>

<tr>
<td><CODE>PR_TRUE</CODE> if tooltip text is associated  
        with the node and was returned in the aText argument;  
        <CODE>PR_FALSE</CODE> otherwise.  
</td>
</tr>

</table>
