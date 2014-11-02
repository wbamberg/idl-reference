---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/nsIWindowCreator.idl">Source file</a>
</div>
# nsIWindowCreator #

## Methods ##

### createChromeWindow(parent, chromeFlags) ###
 Create a new window. Gecko will/may call this method, if made  
available to it, to create new windows.  
@param parent parent window, if any. null if not. the newly created  
window should be made a child/dependent window of  
the parent, if any (and if the concept applies  
to the underlying OS).  
@param chromeFlags chrome features from nsIWebBrowserChrome  
@return the new window  
  

#### Parameters ####

<table>

<tr>
<td>parent</td>
<td>parent window, if any. null if not. the newly created  
window should be made a child/dependent window of  
the parent, if any (and if the concept applies  
to the underlying OS).  
</td>
</tr>

<tr>
<td>chromeFlags</td>
<td>chrome features from nsIWebBrowserChrome  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the new window  
</td>
</tr>

</table>
