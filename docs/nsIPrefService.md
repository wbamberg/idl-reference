---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/modules/libpref/nsIPrefService.idl">Source file</a>
</div>

# nsIPrefService #
<pre>  
The nsIPrefService interface is the main entry point into the back end  
preferences management library. The preference service is directly  
responsible for the management of the preferences files and also facilitates  
access to the preference branch object which allows the direct manipulation  
of the preferences themselves.  
  
@see nsIPrefBranch  
  
</pre>
## Methods ##

### readUserPrefs(aFile) ###
<pre>  
Called to read in the preferences specified in a user preference file.  
  
@param aFile The file to be read.  
  
@note  
If nullptr is passed in for the aFile parameter the default preferences  
file(s) [prefs.js, user.js] will be read and processed.  
  
@throws Error File failed to read or contained invalid data.  
  
@see savePrefFile  
@see nsIFile  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aFile</td>
<td>The file to be read.  
</td>
</tr>

</table>

### resetPrefs() ###
<pre>  
Called to completely flush and re-initialize the preferences system.  
  
@throws Error The preference service failed to restart correctly.  
  
</pre>
### resetUserPrefs() ###
<pre>  
Called to reset all preferences with user set values back to the  
application default values.  
  
</pre>
### savePrefFile(aFile) ###
<pre>  
Called to write current preferences state to a file.  
  
@param aFile The file to be written.  
  
@note  
If nullptr is passed in for the aFile parameter the preference data is  
written out to the current preferences file (usually prefs.js.)  
  
@throws Error File failed to write.  
  
@see readUserPrefs  
@see nsIFile  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aFile</td>
<td>The file to be written.  
</td>
</tr>

</table>

### getBranch(aPrefRoot) ###
<pre>  
Call to get a Preferences "Branch" which accesses user preference data.  
Using a Set method on this object will always create or set a user  
preference value. When using a Get method a user set value will be  
returned if one exists, otherwise a default value will be returned.  
  
@param aPrefRoot The preference "root" on which to base this "branch".  
                 For example, if the root "browser.startup." is used, the  
                 branch will be able to easily access the preferences  
                 "browser.startup.page", "browser.startup.homepage", or  
                 "browser.startup.homepage_override" by simply requesting  
                 "page", "homepage", or "homepage_override". nullptr or ""   
                 may be used to access to the entire preference "tree".  
  
@return nsIPrefBranch The object representing the requested branch.  
  
@see getDefaultBranch  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aPrefRoot</td>
<td>The preference "root" on which to base this "branch".  
                 For example, if the root "browser.startup." is used, the  
                 branch will be able to easily access the preferences  
                 "browser.startup.page", "browser.startup.homepage", or  
                 "browser.startup.homepage_override" by simply requesting  
                 "page", "homepage", or "homepage_override". nullptr or ""   
                 may be used to access to the entire preference "tree".  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>nsIPrefBranch The object representing the requested branch.  
</td>
</tr>

</table>

### getDefaultBranch(aPrefRoot) ###
<pre>  
Call to get a Preferences "Branch" which accesses only the default   
preference data. Using a Set method on this object will always create or  
set a default preference value. When using a Get method a default value  
will always be returned.  
  
@param aPrefRoot The preference "root" on which to base this "branch".  
                 For example, if the root "browser.startup." is used, the  
                 branch will be able to easily access the preferences  
                 "browser.startup.page", "browser.startup.homepage", or  
                 "browser.startup.homepage_override" by simply requesting  
                 "page", "homepage", or "homepage_override". nullptr or ""   
                 may be used to access to the entire preference "tree".  
  
@note  
Few consumers will want to create default branch objects. Many of the  
branch methods do nothing on a default branch because the operations only  
make sense when applied to user set preferences.  
  
@return nsIPrefBranch The object representing the requested default branch.  
  
@see getBranch  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aPrefRoot</td>
<td>The preference "root" on which to base this "branch".  
                 For example, if the root "browser.startup." is used, the  
                 branch will be able to easily access the preferences  
                 "browser.startup.page", "browser.startup.homepage", or  
                 "browser.startup.homepage_override" by simply requesting  
                 "page", "homepage", or "homepage_override". nullptr or ""   
                 may be used to access to the entire preference "tree".  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>nsIPrefBranch The object representing the requested default branch.  
</td>
</tr>

</table>

## Attributes ##

### dirty ###
<pre>  
The preference service is 'dirty' if there are changes to user preferences  
that have not been written to disk  
  
</pre>