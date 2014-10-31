---
layout: default
---

# fuelIWindow #
  
Interface representing a browser window.  
  

## Methods ##

### open(aURI) ###
  
Open a new browser tab, pointing to the specified URI.  
@param   aURI  
         The uri to open the browser tab to  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aURI  
         The uri to open the browser tab to  
</td>
</tr>

</table>

## Attributes ##

### tabs ###
  
A collection of browser tabs within the browser window.  
  

### activeTab ###
  
The currently-active tab within the browser window.  
  

### events ###
  
The events object for the browser window.  
supports: "TabOpen", "TabClose", "TabMove", "TabSelect"  
  
