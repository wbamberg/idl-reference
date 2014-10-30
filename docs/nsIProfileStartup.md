---
layout: default
---

# nsIProfileStartup #
  
Helper interface for nsIProfileMigrator.  
  
@provider Toolkit (Startup code)  
@client   Application (Profile-migration code)  
@obtainable nsIProfileMigrator.migrate  
  

## Methods ##

### doStartup() ###
  
Do profile-startup by setting NS_APP_USER_PROFILE_50_DIR in the directory  
service and notifying the profile-startup observer topics.  
  

## Attributes ##

### directory ###
  
The root directory of the semi-current profile, during profile migration.  
After nsIProfileMigrator.migrate has returned, this object will not be  
useful.  
  
