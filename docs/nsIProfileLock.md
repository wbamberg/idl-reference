---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/profile/nsIToolkitProfile.idl">Source file</a>
</div>

# nsIProfileLock #
<pre>  
Hold on to a profile lock. Once you release the last reference to this  
interface, the profile lock is released.  
  
</pre>
## Methods ##

### unlock() ###
<pre>  
Unlock the profile.  
  
</pre>
## Attributes ##

### directory ###
<pre>  
The main profile directory.  
  
</pre>
### localDirectory ###
<pre>  
A directory corresponding to the main profile directory that exists for  
the purpose of storing data on the local filesystem, including cache  
files or other data files that may not represent critical user data.  
(e.g., this directory may not be included as part of a backup scheme.)  
  
In some cases, this directory may just be the main profile directory.  
  
</pre>
### replacedLockTime ###
<pre>  
The timestamp of an existing profile lock at lock time.  
  
</pre>