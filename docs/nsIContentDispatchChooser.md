---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/exthandler/nsIContentDispatchChooser.idl">Source file</a>
</div>

# nsIContentDispatchChooser #
  
This is used to ask a user what they would like to do with a given piece of  
content.  
  

## Methods ##

### ask(aHandler, aWindowContext, aURI, aReason) ###
  
Asks the user what to do with the content.  
  
@param aHander  
       The interface describing the details of how this content should or  
       can be handled.  
@param aWindowContext  
       The parent window context to show this chooser.  This can be null,  
       and some implementations may not care about it.  Generally, you'll  
       want to pass an nsIDOMWindow in so the chooser can be properly  
       parented when opened.  
@param aURI  
       The URI of the resource that we are asking about.  
@param aReason  
       The reason why we are asking (see above).  
  

#### Parameters ####

<table>

<tr>
<td>aHander</td>
<td>       The interface describing the details of how this content should or  
       can be handled.  
</td>
</tr>

<tr>
<td>aWindowContext</td>
<td>       The parent window context to show this chooser.  This can be null,  
       and some implementations may not care about it.  Generally, you'll  
       want to pass an nsIDOMWindow in so the chooser can be properly  
       parented when opened.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       The URI of the resource that we are asking about.  
</td>
</tr>

<tr>
<td>aReason</td>
<td>       The reason why we are asking (see above).  
</td>
</tr>

</table>

## Constants ##

### REASON_CANNOT_HANDLE ###
  
This request is passed to the helper app dialog because Gecko can not  
handle content of this type.  
  
