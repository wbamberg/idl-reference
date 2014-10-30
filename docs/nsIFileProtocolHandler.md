---
layout: default
---

# nsIFileProtocolHandler #

## Methods ##

### newFileURI(aFile) ###
  
This method constructs a new file URI   
  
@param aFile nsIFile  
@return reference to a new nsIURI object  
  

### getURLSpecFromFile(file) ###
  
Converts the nsIFile to the corresponding URL string.  NOTE: under  
some platforms this is a lossy conversion (e.g., Mac Carbon build).  
If the nsIFile is a local file, then the result will be a file://  
URL string.  
  
The resulting string may contain URL-escaped characters.  
NOTE: Callers should use getURLSpecFromActualFile or  
getURLSpecFromDirFile if possible, for performance reasons.  
  

### getURLSpecFromActualFile(file) ###
  
Converts the nsIFile to the corresponding URL string. Should  
only be called on files which are not directories. Otherwise  
identical to getURLSpecFromFile, but is usually more efficient.  
WARNING: This restriction may not be enforced at runtime!   
  

### getURLSpecFromDir(file) ###
  
Converts the nsIFile to the corresponding URL string. Should  
only be called on files which are directories. Otherwise  
identical to getURLSpecFromFile, but is usually more efficient.  
WARNING: This restriction may not be enforced at runtime!   
  

### getFileFromURLSpec(url) ###
  
Converts the URL string into the corresponding nsIFile if possible.  
A local file will be created if the URL string begins with file://.  
  

### readURLFile(file) ###
  
Takes a local file and tries to interpret it as an internet shortcut  
(e.g. .url files on windows).  
@param file The local file to read  
@return The URI the file refers to  
  
@throw NS_ERROR_NOT_AVAILABLE if the OS does not support such files.  
@throw NS_ERROR_NOT_AVAILABLE if this file is not an internet shortcut.  
  
