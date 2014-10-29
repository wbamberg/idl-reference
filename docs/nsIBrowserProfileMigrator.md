---
layout: default
---

# nsIBrowserProfileMigrator #

## Methods ##

### migrate ###

Copy user profile information to the current active profile.
@param aItems   list of data items to migrate. see above for values.
@param aStartup helper interface which is non-null if called during startup. 
@param aProfile profile to migrate from, if there is more than one.


### getMigrateData ###

A bit field containing profile items that this migrator
offers for import. 
@param   aProfile the profile that we are looking for available data
         to import
@param   aDoingStartup "true" if the profile is not currently being used.
@return  bit field containing profile items (see above)
@note    a return value of 0 represents no items rather than ALL.


## Attributes ##

### sourceExists ###
 
Whether or not there is any data that can be imported from this 
browser (i.e. whether or not it is installed, and there exists
a user profile)


### sourceProfiles ###
 
An enumeration of available profiles. If the import source does 
not support profiles, this attribute is null.


### sourceHomePageURL ###

The import source homepage.  Returns null if not present/available


## Constants ##

### ALL ###

profile items to migrate. use with migrate().


### SETTINGS ###

### COOKIES ###

### HISTORY ###

### FORMDATA ###

### PASSWORDS ###

### BOOKMARKS ###

### OTHERDATA ###

### SESSION ###
