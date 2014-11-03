---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/profile/nsIToolkitProfileService.idl">Source file</a>
</div>

# nsIToolkitProfileService #

## Methods ##

### getProfileByName(aName) ###
<code>  
Get a profile by name. This is mainly for use by the -P  
commandline flag.  
  
@param aName The profile name to find.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>The profile name to find.  
</td>
</tr>

</table>

### lockProfilePath(aDirectory, aTempDirectory) ###
<code>  
Lock an arbitrary path as a profile. If the path does not exist, it  
will be created and the defaults copied from the application directory.  
  
</code>
### createProfile(aRootDir, aName) ###
<code>  
Create a new profile.  
  
The profile temporary directory will be chosen based on where the  
profile directory is located.  
  
@param aRootDir  
       The profile directory. May be null, in which case a suitable  
       default will be chosen based on the profile name.  
@param aName  
       The profile name.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aRootDir</td>
<td>       The profile directory. May be null, in which case a suitable  
       default will be chosen based on the profile name.  
</td>
</tr>

<tr>
<td>aName</td>
<td>       The profile name.  
</td>
</tr>

</table>

### createDefaultProfileForApp(aProfileName, aAppName, aVendorName, aProfileDefaultsDir) ###
<code>  
Create the default profile for an application.  
  
The profile will be typically in  
{Application Data}/.profilename/{salt}.default or  
{Application Data}/.appname/{salt}.default  
or if aVendorName is provided  
{Application Data}/.vendor/appname/{salt}.default  
  
@note Either aProfileName or aAppName must be non-empty  
  
The contents of aProfileDefaultsDir will be copied to the  
new profile directory.  
  
@param  aProfileName  
        The name of the profile  
@param  aAppName  
        The name of the application  
@param  aVendorName  
        The name of the vendor  
@param  aProfileDefaultsDir  
        The location where the profile defaults are.  
@return The created profile.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aProfileName</td>
<td>        The name of the profile  
</td>
</tr>

<tr>
<td>aAppName</td>
<td>        The name of the application  
</td>
</tr>

<tr>
<td>aVendorName</td>
<td>        The name of the vendor  
</td>
</tr>

<tr>
<td>aProfileDefaultsDir</td>
<td>        The location where the profile defaults are.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The created profile.  
</td>
</tr>

</table>

### flush() ###
<code>  
Flush the profiles list file.  
  
</code>
## Attributes ##

### startWithLastProfile ###

### startOffline ###

### profiles ###

### selectedProfile ###
  
The currently selected profile (the one used or about to be used by the  
browser).  
  

### defaultProfile ###
  
The default profile (the one used or about to be used by the  
browser if no other profile is specified at runtime). This is the profile  
marked with Default=1 in profiles.ini and is usually the same as  
selectedProfile, except on Developer Edition.  
  
Developer Edition uses a profile named "dev-edition-default" as the  
default profile (which it creates if it doesn't exist), unless a special  
empty file named "ignore-dev-edition-profile" is present next to  
profiles.ini. In that case Developer Edition behaves the same as any  
other build of Firefox.  
  

### profileCount ###
  
Returns the number of profiles.  
@return 0, 1, or 2. More than 2 profiles will always return 2.  
  
