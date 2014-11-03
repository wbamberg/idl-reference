---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIBrowserTab #
<code>  
Interface representing a browser tab.  
  
</code>
## Methods ##

### load(aURI) ###
<code>  
Load a new URI into this browser tab.  
@param   aURI  
         The uri to load into the browser tab  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>         The uri to load into the browser tab  
</td>
</tr>

</table>

### focus() ###
<code>  
Give focus to this browser tab, and bring it to the front.  
  
</code>
### close() ###
<code>  
Close the browser tab. This may not actually close the tab  
as script may abort the close operation.  
  
</code>
### moveBefore(aBefore) ###
<code>  
Moves this browser tab before another browser tab within the window.  
@param   aBefore  
         The tab before which the target tab will be moved  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aBefore</td>
<td>         The tab before which the target tab will be moved  
</td>
</tr>

</table>

### moveToEnd() ###
<code>  
Move this browser tab to the last tab within the window.  
  
</code>
## Attributes ##

### uri ###
  
The current uri of this tab.  
  

### index ###
  
The current index of this tab in the browser window.  
  

### window ###
  
The browser window that is holding the tab.  
  

### document ###
  
The content document of the browser tab.  
  

### events ###
  
The events object for the browser tab.  
supports: "load"  
  
