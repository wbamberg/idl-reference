---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIWindow #
<pre>  
Interface representing a browser window.  
  
</pre>
## Methods ##

### open(aURI) ###
<pre>  
Open a new browser tab, pointing to the specified URI.  
@param   aURI  
         The uri to open the browser tab to  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>         The uri to open the browser tab to  
</td>
</tr>

</table>

## Attributes ##

### tabs ###
<pre>  
A collection of browser tabs within the browser window.  
  
</pre>
### activeTab ###
<pre>  
The currently-active tab within the browser window.  
  
</pre>
### events ###
<pre>  
The events object for the browser window.  
supports: "TabOpen", "TabClose", "TabMove", "TabSelect"  
  
</pre>