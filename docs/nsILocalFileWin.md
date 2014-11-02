---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsILocalFileWin.idl">Source file</a>
</div>

# nsILocalFileWin #

## Methods ##

### getVersionInfoField(aField) ###
  
getVersionInfoValue  
  
Retrieve a metadata field from the file's VERSIONINFO block.  
Throws NS_ERROR_FAILURE if no value is found, or the value is empty.  
  
@param   aField         The field to look up.  
  
  

#### Parameters ####

<table>

<tr>
<td>aField</td>
<td>The field to look up.  
</td>
</tr>

</table>

### setShortcut(targetFile, workingDir, args, description, iconFile, iconIndex) ###
  
setShortcut  
  
Creates the specified shortcut, or updates it if it already exists.  
  
If the shortcut is being updated (i.e. the shortcut already exists),  
any excluded parameters will remain unchanged in the shortcut file.  
For example, if you want to change the description of a specific  
shortcut but keep the target, working dir, args, and icon the same,  
pass null for those parameters and only pass in a value for the  
description.  
  
If the shortcut does not already exist and targetFile is not specified,  
setShortcut will throw NS_ERROR_FILE_TARGET_DOES_NOT_EXIST.  
  
@param targetFile      the path that the shortcut should target  
@param workingDir      the working dir that should be set for the shortcut  
@param args            the args string that should be set for the shortcut  
@param description     the description that should be set for the shortcut  
@param iconFile        the file containing an icon to be used for this  
shortcut  
@param iconIndex       this value selects a specific icon from within  
iconFile.  If iconFile contains only one icon, this  
value should be 0.  
  

#### Parameters ####

<table>

<tr>
<td>targetFile</td>
<td>the path that the shortcut should target  
</td>
</tr>

<tr>
<td>workingDir</td>
<td>the working dir that should be set for the shortcut  
</td>
</tr>

<tr>
<td>args</td>
<td>the args string that should be set for the shortcut  
</td>
</tr>

<tr>
<td>description</td>
<td>the description that should be set for the shortcut  
</td>
</tr>

<tr>
<td>iconFile</td>
<td>the file containing an icon to be used for this  
shortcut  
</td>
</tr>

<tr>
<td>iconIndex</td>
<td>this value selects a specific icon from within  
iconFile.  If iconFile contains only one icon, this  
value should be 0.  
</td>
</tr>

</table>

### openNSPRFileDescShareDelete(flags, mode) ###
  
Identical to nsIFile::openNSPRFileDesc except it also uses the  
FILE_SHARE_DELETE flag.  
  

## Attributes ##

### canonicalPath ###
  
The canonical path of the file, which avoids short/long  
pathname inconsistencies. The nsIFile persistent  
descriptor is not guaranteed to be canonicalized (it may  
persist either the long or the short path name). The format of  
the canonical path will vary with the underlying file system:  
it will typically be the short pathname on filesystems that  
support both short and long path forms.  
  

### nativeCanonicalPath ###

### fileAttributesWin ###
  
fileAttributesWin  
  
Set or get windows specific file attributes.  
  
Throws NS_ERROR_FILE_INVALID_PATH for an invalid file.  
Throws NS_ERROR_FAILURE if the set or get fails.  
  

## Constants ##

### WFA_SEARCH_INDEXED ###
  
Windows specific file attributes.  
  

### WFA_READONLY ###

### WFA_READWRITE ###
