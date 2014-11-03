---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/mime/nsIMIMEInfo.idl">Source file</a>
</div>

# nsILocalHandlerApp #
  
nsILocalHandlerApp is a local OS-level executable  
  

## Methods ##

### clearParameters() ###
  
Clears the current list of command line parameters.  
  

### appendParameter(param) ###
  
Appends a command line parameter to the command line  
parameter list.  
  
@param param the parameter to add.  
  

#### Parameters ####

<table>

<tr>
<td>param</td>
<td>the parameter to add.  
</td>
</tr>

</table>

### getParameter(parameterIndex) ###
  
Retrieves a specific command line parameter.  
  
@param param the index of the parameter to return.  
  
@return the parameter string.  
  
@throw NS_ERROR_INVALID_ARG if the index is out of range.  
  

#### Parameters ####

<table>

<tr>
<td>param</td>
<td>the index of the parameter to return.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the parameter string.  
</td>
</tr>

</table>

### parameterExists(param) ###
  
Checks to see if a parameter exists in the command line  
parameter list.  
  
@param param the parameter to search for.  
  
@return TRUE if the parameter exists in the current list.   
  

#### Parameters ####

<table>

<tr>
<td>param</td>
<td>the parameter to search for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>TRUE if the parameter exists in the current list.   
</td>
</tr>

</table>

## Attributes ##

### executable ###
  
Pointer to the executable file used to handle content  
  

### parameterCount ###
  
Returns the current number of command line parameters.  
  
