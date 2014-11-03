---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/modules/libpref/nsIRelativeFilePref.idl">Source file</a>
</div>

# nsIRelativeFilePref #
<code>  
The nsIRelativeFilePref interface is a wrapper for an nsIFile and  
and a directory service key. When used as a pref value, it stores a  
relative path to the file from the location pointed to by the directory  
service key. The path has the same syntax across all platforms.  
  
@see nsIPrefBranch::getComplexValue  
@see nsIPrefBranch::setComplexValue  
  
  
</code>
## Attributes ##

### file ###
  
file  
  
The file whose location is stored or retrieved.  
  

### relativeToKey ###
  
relativeToKey  
  
A directory service key for the directory  
from which the file path is relative.  
  
