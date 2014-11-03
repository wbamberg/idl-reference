---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/profile/nsIProfileMigrator.idl">Source file</a>
</div>

# nsIProfileStartup #
<pre>  
Helper interface for nsIProfileMigrator.  
  
@provider Toolkit (Startup code)  
@client   Application (Profile-migration code)  
@obtainable nsIProfileMigrator.migrate  
  
</pre>
## Methods ##

### doStartup() ###
<pre>  
Do profile-startup by setting NS_APP_USER_PROFILE_50_DIR in the directory  
service and notifying the profile-startup observer topics.  
  
</pre>
## Attributes ##

### directory ###
<pre>  
The root directory of the semi-current profile, during profile migration.  
After nsIProfileMigrator.migrate has returned, this object will not be  
useful.  
  
</pre>