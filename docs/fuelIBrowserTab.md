---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIBrowserTab #
<pre>  
Interface representing a browser tab.  
  
</pre>
## Methods ##

### load(aURI) ###
<pre>  
Load a new URI into this browser tab.  
@param   aURI  
         The uri to load into the browser tab  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>         The uri to load into the browser tab  
</td>
</tr>

</table>

### focus() ###
<pre>  
Give focus to this browser tab, and bring it to the front.  
  
</pre>
### close() ###
<pre>  
Close the browser tab. This may not actually close the tab  
as script may abort the close operation.  
  
</pre>
### moveBefore(aBefore) ###
<pre>  
Moves this browser tab before another browser tab within the window.  
@param   aBefore  
         The tab before which the target tab will be moved  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aBefore</td>
<td>         The tab before which the target tab will be moved  
</td>
</tr>

</table>

### moveToEnd() ###
<pre>  
Move this browser tab to the last tab within the window.  
  
</pre>
## Attributes ##

### uri ###
<pre>  
The current uri of this tab.  
  
</pre>
### index ###
<pre>  
The current index of this tab in the browser window.  
  
</pre>
### window ###
<pre>  
The browser window that is holding the tab.  
  
</pre>
### document ###
<pre>  
The content document of the browser tab.  
  
</pre>
### events ###
<pre>  
The events object for the browser tab.  
supports: "load"  
  
</pre>