---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/update/nsIUpdateService.idl">Source file</a>
</div>

# nsIUpdatePatch #
  
An interface that describes an object representing a patch file that can  
be downloaded and applied to a version of this application so that it  
can be updated.  
  

## Methods ##

### serialize(updates) ###
  
Serializes this patch object into a DOM Element  
@param   updates  
         The document to serialize into  
@returns The DOM Element created by the serialization process  
  

#### Parameters ####

<table>

<tr>
<td>updates</td>
<td>         The document to serialize into  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The DOM Element created by the serialization process  
</td>
</tr>

</table>

## Attributes ##

### type ###
  
The type of this patch:  
"partial"      A binary difference between two application versions  
"complete"     A complete patch containing all of the replacement files  
               to update to the new version  
  

### URL ###
  
The URL this patch was being downloaded from  
  

### finalURL ###
  
The final URL this patch was being downloaded from  
  

### hashFunction ###
  
The hash function to use when determining this file's integrity  
  

### hashValue ###
  
The value of the hash function named above that should be computed if  
this file is not corrupt.  
  

### size ###
  
The size of this file, in bytes.  
  

### state ###
  
The state of this patch  
  

### selected ###
  
true if this patch is currently selected as the patch to be downloaded and  
installed for this update transaction, false if another patch from this  
update has been selected.  
  
