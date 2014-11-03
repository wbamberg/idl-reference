---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/components/migration/nsIBrowserProfileMigrator.idl">Source file</a>
</div>

# nsIBrowserProfileMigrator #

## Methods ##

### migrate(aItems, aStartup, aProfile) ###
<pre>  
Copy user profile information to the current active profile.  
@param aItems   list of data items to migrate. see above for values.  
@param aStartup helper interface which is non-null if called during startup.   
@param aProfile profile to migrate from, if there is more than one.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aItems</td>
<td>list of data items to migrate. see above for values.  
</td>
</tr>

<tr>
<td>aStartup</td>
<td>helper interface which is non-null if called during startup.   
</td>
</tr>

<tr>
<td>aProfile</td>
<td>profile to migrate from, if there is more than one.  
</td>
</tr>

</table>

### getMigrateData(aProfile, aDoingStartup) ###
<pre>  
A bit field containing profile items that this migrator  
offers for import.   
@param   aProfile the profile that we are looking for available data  
         to import  
@param   aDoingStartup "true" if the profile is not currently being used.  
@return  bit field containing profile items (see above)  
@note    a return value of 0 represents no items rather than ALL.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aProfile</td>
<td>the profile that we are looking for available data  
         to import  
</td>
</tr>

<tr>
<td>aDoingStartup</td>
<td>"true" if the profile is not currently being used.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>bit field containing profile items (see above)  
@note    a return value of 0 represents no items rather than ALL.  
</td>
</tr>

</table>

## Attributes ##

### sourceExists ###
<pre>   
Whether or not there is any data that can be imported from this   
browser (i.e. whether or not it is installed, and there exists  
a user profile)  
  
</pre>
### sourceProfiles ###
<pre>   
An enumeration of available profiles. If the import source does   
not support profiles, this attribute is null.  
  
</pre>
### sourceHomePageURL ###
<pre>  
The import source homepage.  Returns null if not present/available  
  
</pre>
## Constants ##

### ALL ###
<pre>  
profile items to migrate. use with migrate().  
  
</pre>
### SETTINGS ###

### COOKIES ###

### HISTORY ###

### FORMDATA ###

### PASSWORDS ###

### BOOKMARKS ###

### OTHERDATA ###

### SESSION ###
