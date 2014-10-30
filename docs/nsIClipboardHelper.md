---
layout: default
---

# nsIClipboardHelper #
  
helper service for common uses of nsIClipboard.  
  

## Methods ##

### copyStringToClipboard ###
  
copy string to given clipboard  
  
@param aString, the string to copy to the clipboard  
@param aDoc, the source document for the string, if available  
@param aClipboardID, the ID of the clipboard to copy to  
       (eg. kSelectionClipboard -- see nsIClipboard.idl)  
  

### copyString ###
  
copy string to (default) clipboard  
  
@param aString, the string to copy to the clipboard  
@param aDoc, the source document for the string, if available  
  
