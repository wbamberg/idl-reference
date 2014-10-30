---
layout: default
---

# nsILocalHandlerApp #
  
nsILocalHandlerApp is a local OS-level executable  
  

## Methods ##

### clearParameters() ###
  
Clears the current list of command line parameters.  
  

### appendParameter(param) ###
  
Appends a command line parameter to the command line  
parameter list.  
  
@param param the parameter to add.  
  

### getParameter(parameterIndex) ###
  
Retrieves a specific command line parameter.  
  
@param param the index of the parameter to return.  
  
@return the parameter string.  
  
@throw NS_ERROR_INVALID_ARG if the index is out of range.  
  

### parameterExists(param) ###
  
Checks to see if a parameter exists in the command line  
parameter list.  
  
@param param the parameter to search for.  
  
@return TRUE if the parameter exists in the current list.   
  

## Attributes ##

### executable ###
  
Pointer to the executable file used to handle content  
  

### parameterCount ###
  
Returns the current number of command line parameters.  
  
