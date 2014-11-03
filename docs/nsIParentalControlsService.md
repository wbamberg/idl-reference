---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/parentalcontrols/nsIParentalControlsService.idl">Source file</a>
</div>

# nsIParentalControlsService #

## Methods ##

### isAllowed(aAction, aUri) ###
  
Check if the user can do the prescibed action for this uri.  
  
  

#### Parameters ####

<table>

<tr>
<td>aAction</td>
<td>Action being performed  
</td>
</tr>

<tr>
<td>aUri</td>
<td>The uri requesting this action  
</td>
</tr>

<tr>
<td>aWindow</td>
<td>The window generating this event.  
</td>
</tr>

</table>

### requestURIOverride(aTarget, aWindowContext) ###
  
Request that blocked URI(s) be allowed through parental  
control filters. Returns true if the URI was successfully  
overriden. Note, may block while native UI is shown.  
  
  

#### Parameters ####

<table>

<tr>
<td>aTarget(s)</td>
<td>URI to be overridden. In the case of  
                           multiple URI, the first URI in the array  
                           should be the root URI of the site.  
</td>
</tr>

<tr>
<td>window</td>
<td>Window that generates the event.  
</td>
</tr>

</table>

### requestURIOverrides(aTargets, aWindowContext) ###

### log(aEntryType, aFlag, aSource, aTarget) ###
  
Log an application specific parental controls  
event.  
  
  

#### Parameters ####

<table>

<tr>
<td>aEntryType</td>
<td>Constant defining the type of event.  
</td>
</tr>

<tr>
<td>aFlag</td>
<td>A flag indicating if the subject content  
                        was blocked.  
</td>
</tr>

<tr>
<td>aSource</td>
<td>The URI source of the subject content.  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>The location the content was saved to if  
                        no blocking occurred.  
</td>
</tr>

</table>

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
