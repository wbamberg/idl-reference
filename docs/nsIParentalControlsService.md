---
layout: default
---

# nsIParentalControlsService #

## Methods ##

### isAllowed(aAction, aUri) ###
  
Check if the user can do the prescibed action for this uri.  
  
@param aAction             Action being performed  
@param aUri                The uri requesting this action  
@param aWindow             The window generating this event.  
  

### requestURIOverride(aTarget, aWindowContext) ###
  
Request that blocked URI(s) be allowed through parental  
control filters. Returns true if the URI was successfully  
overriden. Note, may block while native UI is shown.  
  
@param aTarget(s)          URI to be overridden. In the case of  
                           multiple URI, the first URI in the array  
                           should be the root URI of the site.  
@param window              Window that generates the event.  
  

### requestURIOverrides(aTargets, aWindowContext) ###

### log(aEntryType, aFlag, aSource, aTarget) ###
  
Log an application specific parental controls  
event.  
  
@param aEntryType       Constant defining the type of event.  
@param aFlag            A flag indicating if the subject content  
                        was blocked.  
@param aSource          The URI source of the subject content.  
@param aTarget          The location the content was saved to if  
                        no blocking occurred.  
  

## Attributes ##

### parentalControlsEnabled ###
  
@returns true if the current user account has parental controls  
restrictions enabled.  
  

### blockFileDownloadsEnabled ###
  
@returns true if the current user account parental controls  
restrictions include the blocking of all file downloads.  
  

### loggingEnabled ###
  
@returns true if the current user account has parental controls  
logging enabled. If true, applications should log relevent events  
using 'log'.  
  

## Constants ##

### DOWNLOAD ###
  
Action types that can be blocked for users.  
  

### INSTALL_EXTENSION ###

### INSTALL_APP ###

### VISIT_FILE_URLS ###

### SHARE ###

### BOOKMARK ###

### ADD_CONTACT ###

### SET_IMAGE ###

### MODIFY_ACCOUNTS ###

### REMOTE_DEBUGGING ###

### IMPORT_SETTINGS ###

### ePCLog_URIVisit ###
  
Log entry types. Additional types can be defined and implemented  
as needed. Other possible event types might include email events,  
media related events, and IM events.   
  

### ePCLog_FileDownload ###
