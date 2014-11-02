---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIWebBrowserChrome2.idl">Source file</a>
</div>

# nsIWebBrowserChrome2 #
  
nsIWebBrowserChrome2 is an extension to nsIWebBrowserChrome.  
  

## Methods ##

### setStatusWithContext(statusType, statusText, statusContext) ###
  
Called when the status text in the chrome needs to be updated.  This  
method may be called instead of nsIWebBrowserChrome::SetStatus.  An  
implementor of this method, should still implement SetStatus.  
  
@param statusType  
       Indicates what is setting the text.  
@param status  
       Status string.  Null is an acceptable value meaning no status.  
@param contextNode   
       An object that provides context pertaining to the status type.  
       If statusType is STATUS_LINK, then statusContext may be a DOM  
       node corresponding to the source of the link.  This value can  
       be null if there is no context.  
  

#### Parameters ####

<table>

<tr>
<td>statusType</td>
<td>       Indicates what is setting the text.  
</td>
</tr>

<tr>
<td>status</td>
<td>       Status string.  Null is an acceptable value meaning no status.  
</td>
</tr>

<tr>
<td>contextNode</td>
<td>       An object that provides context pertaining to the status type.  
       If statusType is STATUS_LINK, then statusContext may be a DOM  
       node corresponding to the source of the link.  This value can  
       be null if there is no context.  
</td>
</tr>

</table>
