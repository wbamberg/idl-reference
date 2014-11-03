---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/nsIWindowCreator2.idl">Source file</a>
</div>

# nsIWindowCreator2 #

## Methods ##

### createChromeWindow2(parent, chromeFlags, contextFlags, uri, aOpeningTab, cancel) ###
 Create a new window. Gecko will/may call this method, if made  
available to it, to create new windows.  
@param parent Parent window, if any. Null if not. The newly created  
window should be made a child/dependent window of  
the parent, if any (and if the concept applies  
to the underlying OS).  
@param chromeFlags Chrome features from nsIWebBrowserChrome  
@param contextFlags Flags about the context of the window being created.  
@param uri The URL for which this window is intended. It can be null  
or zero-length. The implementation of this interface  
may use the URL to help determine what sort of window  
to open or whether to cancel window creation. It will not  
load the URL.  
@param aOpeningTab The TabParent that is trying to open this new chrome  
window. Can be nullptr.  
@param cancel Return |true| to reject window creation. If true the  
implementation has determined the window should not  
be created at all. The caller should not default  
to any possible backup scheme for creating the window.  
@return the new window. Will be null if canceled or an error occurred.  
  

#### Parameters ####

<table>

<tr>
<td>parent</td>
<td>Parent window, if any. Null if not. The newly created  
window should be made a child/dependent window of  
the parent, if any (and if the concept applies  
to the underlying OS).  
</td>
</tr>

<tr>
<td>chromeFlags</td>
<td>Chrome features from nsIWebBrowserChrome  
</td>
</tr>

<tr>
<td>contextFlags</td>
<td>Flags about the context of the window being created.  
</td>
</tr>

<tr>
<td>uri</td>
<td>The URL for which this window is intended. It can be null  
or zero-length. The implementation of this interface  
may use the URL to help determine what sort of window  
to open or whether to cancel window creation. It will not  
load the URL.  
</td>
</tr>

<tr>
<td>aOpeningTab</td>
<td>The TabParent that is trying to open this new chrome  
window. Can be nullptr.  
</td>
</tr>

<tr>
<td>cancel</td>
<td>Return |true| to reject window creation. If true the  
implementation has determined the window should not  
be created at all. The caller should not default  
to any possible backup scheme for creating the window.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the new window. Will be null if canceled or an error occurred.  
</td>
</tr>

</table>

## Constants ##

### PARENT_IS_LOADING_OR_RUNNING_TIMEOUT ###
  
Definitions for contextFlags  
  
