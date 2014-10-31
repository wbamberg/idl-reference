---
layout: default
---

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
<td>parent</td>
<td>parent window, if any. null if not. the newly created  
window should be made a child/dependent window of  
the parent, if any (and if the concept applies  
to the underlying OS).  
</td>
</tr>

</table>
