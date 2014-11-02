---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/profile/nsIProfileMigrator.idl">Source file</a>
</div>
# nsIProfileMigrator #
  
Migrate application settings from an outside source.  
  
@provider Application (Profile-migration code)  
@client   Toolkit (Startup code)  
@obtainable service, contractid("@mozilla.org/toolkit/profile-migrator;1")  
  

## Methods ##

### migrate(aStartup, aKey) ###
  
Migrate data from an outside source, if possible.  Does nothing  
otherwise.  
  
When this method is called, a default profile has been created;  
XPCOM has been initialized such that compreg.dat is in the  
profile; the directory service does *not* return a key for  
NS_APP_USER_PROFILE_50_DIR or any of the keys depending on an active  
profile. To figure out the directory of the "current" profile, use  
aStartup.directory.  
  
If your migrator needs to access services that use the profile (to  
set profile prefs or bookmarks, for example), use aStartup.doStartup.  
  
@param  aStartup nsIProfileStartup object to use during migration.  
@param  aKey     optional key of a migrator to use to skip source selection.  
  
@note The startup code ignores COM exceptions thrown from this method.  
  

#### Parameters ####

<table>

<tr>
<td>aStartup</td>
<td>nsIProfileStartup object to use during migration.  
</td>
</tr>

<tr>
<td>aKey</td>
<td>optional key of a migrator to use to skip source selection.  
</td>
</tr>

</table>
