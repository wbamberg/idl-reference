---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/profile/nsIToolkitProfile.idl">Source file</a>
</div>

# nsIToolkitProfile #
<pre>  
A interface representing a profile.  
@note THIS INTERFACE SHOULD BE IMPLEMENTED BY THE TOOLKIT CODE ONLY! DON'T  
      EVEN THINK ABOUT IMPLEMENTING THIS IN JAVASCRIPT!  
  
</pre>
## Methods ##

### remove(removeFiles) ###
<pre>  
Removes the profile from the registry of profiles.  
  
@param removeFiles  
       Indicates whether or not the profile directory should be  
       removed in addition.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>removeFiles</td>
<td>       Indicates whether or not the profile directory should be  
       removed in addition.  
</td>
</tr>

</table>

### lock(aUnlocker) ###
<pre>  
Lock this profile using platform-specific locking methods.  
  
@param lockFile If locking fails, this may return a lockFile object  
                which can be used in platform-specific ways to  
                determine which process has the file locked. Null  
                may be passed.  
@return An interface which holds a profile lock as long as you reference  
        it.  
@throws NS_ERROR_FILE_ACCESS_DENIED if the profile was already locked.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>lockFile</td>
<td>If locking fails, this may return a lockFile object  
                which can be used in platform-specific ways to  
                determine which process has the file locked. Null  
                may be passed.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An interface which holds a profile lock as long as you reference  
        it.  
@throws NS_ERROR_FILE_ACCESS_DENIED if the profile was already locked.  
</td>
</tr>

</table>

## Attributes ##

### rootDir ###
<pre>  
The location of the profile directory.  
  
</pre>
### localDir ###
<pre>  
The location of the profile local directory, which may be the same as  
the root directory.  See nsIProfileLock::localDirectory.  
  
</pre>
### name ###
<pre>  
The name of the profile.  
  
</pre>