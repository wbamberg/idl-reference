---
layout: default
---

# nsILocalFileMac #

## Methods ##

### initWithCFURL ###
  
initWithCFURL  
  
Init this object with a CFURLRef  
  
NOTE: Supported only for XP_MACOSX  
NOTE: If the path of the CFURL is /a/b/c, at least a/b must exist beforehand.  
  
@param   aCFURL         the CoreFoundation URL  
  
  

### initWithFSRef ###
  
initWithFSRef  
  
Init this object with an FSRef  
  
NOTE: Supported only for XP_MACOSX  
  
@param   aFSRef         the native FSRef  
  
  

### getCFURL ###
  
getCFURL  
  
Returns the CFURLRef of the file object. The caller is  
responsible for calling CFRelease() on it.  
  
NOTE: Observes the state of the followLinks attribute.  
If the file object is an alias and followLinks is TRUE, returns  
the target of the alias. If followLinks is FALSE, returns  
the unresolved alias file.  
  
NOTE: Supported only for XP_MACOSX  
  
@return  
   
  

### getFSRef ###
  
getFSRef  
  
Returns the FSRef of the file object.  
  
NOTE: Observes the state of the followLinks attribute.  
If the file object is an alias and followLinks is TRUE, returns  
the target of the alias. If followLinks is FALSE, returns  
the unresolved alias file.  
  
NOTE: Supported only for XP_MACOSX  
  
@return  
   
  

### getFSSpec ###
  
getFSSpec  
  
Returns the FSSpec of the file object.  
  
NOTE: Observes the state of the followLinks attribute.  
If the file object is an alias and followLinks is TRUE, returns  
the target of the alias. If followLinks is FALSE, returns  
the unresolved alias file.  
  
@return  
   
  

### launchWithDoc ###
  
launchWithDoc  
  
Launch the application that this file points to with a document.  
  
@param   aDocToLoad          Must not be NULL. If no document, use nsIFile::launch  
@param   aLaunchInBackground TRUE if the application should not come to the front.  
  
  

### openDocWithApp ###
  
openDocWithApp  
  
Open the document that this file points to with the given application.  
  
@param   aAppToOpenWith      The application with  which to open the document.  
                             If NULL, the creator code of the document is used  
                             to determine the application.  
@param   aLaunchInBackground TRUE if the application should not come to the front.  
  
  

### isPackage ###
  
isPackage  
  
returns true if a directory is determined to be a package under Mac OS 9/X  
  
  

## Attributes ##

### fileSizeWithResFork ###
  
fileSizeWithResFork  
  
Returns the combined size of both the data fork and the resource  
fork (if present) rather than just the size of the data fork  
as returned by GetFileSize()  
  
  

### fileType ###
  
fileType, creator  
  
File type and creator attributes  
  
  

### fileCreator ###

### bundleDisplayName ###
  
bundleDisplayName  
  
returns the display name of the application bundle (usually the human   
readable name of the application)  
  

### bundleIdentifier ###
  
bundleIdentifier  
  
returns the identifier of the bundle  
  

### bundleContentsLastModifiedTime ###
  
Last modified time of a bundle's contents (as opposed to its package  
directory).  Our convention is to make the bundle's Info.plist file  
stand in for the rest of its contents -- since this file contains the  
bundle's version information and other identifiers.  For non-bundles  
this is the same as lastModifiedTime.  
  
