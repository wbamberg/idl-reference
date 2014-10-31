---
layout: default
---

# nsIContentPrefService #
  
@deprecated Please use nsIContentPrefService2 instead.  
  

## Methods ##

### getPref(aGroup, aName, aPrivacyContext, aCallback) ###
  
Get a pref.  
  
Besides the regular string, integer, boolean, etc. values, this method  
may return null (nsIDataType::VTYPE_EMPTY), which means the pref is set  
to NULL in the database, as well as undefined (nsIDataType::VTYPE_VOID),  
which means there is no record for this pref in the database.  
  
This method can be called from content processes in electrolysis builds.  
We have a whitelist of values that can be read in such a way.  
  
@param    aGroup      the group for which to get the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null   
                      to get the global pref (applies to all sites)  
@param    aName       the name of the pref to get  
@param    aPrivacyContext  
                      a context from which to determine the privacy status  
                      of the pref (ie. whether to search in memory or in  
                      permanent storage for it), obtained from a relevant  
                      window or channel.  
@param    aCallback   an optional nsIContentPrefCallback to receive the  
                      result. If desired, JavaScript callers can instead  
                      provide a function to call upon completion  
  
@returns  the value of the pref  
@throws   NS_ERROR_ILLEGAL_VALUE if aGroup is not a string, nsIURI, or null  
@throws   NS_ERROR_ILLEGAL_VALUE if aName is null or an empty string  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aGroup      the group for which to get the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null   
                      to get the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to get the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null   
                      to get the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to get the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null   
                      to get the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to get the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null   
                      to get the global pref (applies to all sites)  
</td>
</tr>

</table>

### setPref(aGroup, aName, aValue, aPrivacyContext) ###
  
Set a pref.  
  
This method can be called from content processes in electrolysis builds.  
We have a whitelist of values that can be set in such a way.  
  
@param    aGroup      the group for which to set the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to set the global pref (applies to all sites)  
@param    aName       the name of the pref to set  
@param    aValue      the new value of the pref  
@param    aPrivacyContext  
                      a context from which to determine the privacy status  
                      of the pref (ie. whether to store it in memory or in  
                      permanent storage), obtained from a relevant  
                      window or channel.  
@throws   NS_ERROR_ILLEGAL_VALUE if aGroup is not a string, nsIURI, or null  
@throws   NS_ERROR_ILLEGAL_VALUE if aName is null or an empty string  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aGroup      the group for which to set the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to set the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to set the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to set the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to set the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to set the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to set the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to set the global pref (applies to all sites)  
</td>
</tr>

</table>

### hasPref(aGroup, aName, aContext) ###
  
Check whether or not a pref exists.  
  
@param    aGroup      the group for which to check for the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to check for the global pref (applies to all sites)  
@param    aName       the name of the pref to check for  
@param    aPrivacyContext  
                      a context from which to determine the privacy status  
                      of the pref (ie. whether to search in memory or in  
                      permanent storage for it), obtained from a relevant  
                      window or channel.  
@throws   NS_ERROR_ILLEGAL_VALUE if aGroup is not a string, nsIURI, or null  
@throws   NS_ERROR_ILLEGAL_VALUE if aName is null or an empty string  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aGroup      the group for which to check for the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to check for the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to check for the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to check for the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to check for the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to check for the global pref (applies to all sites)  
</td>
</tr>

</table>

### hasCachedPref(aGroup, aName, aContext) ###
  
Check whether or not the value of a pref (or its non-existance) is cached.  
  
@param    aGroup      the group for which to check for the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to check for the global pref (applies to all sites)  
@param    aName       the name of the pref to check for  
@param    aPrivacyContext  
                      a context from which to determine the privacy status  
                      of the pref (ie. whether to search in memory or in  
                      permanent storage for it), obtained from a relevant  
                      window or channel.  
@throws   NS_ERROR_ILLEGAL_VALUE if aGroup is not a string, nsIURI, or null  
@throws   NS_ERROR_ILLEGAL_VALUE if aName is null or an empty string  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aGroup      the group for which to check for the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to check for the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to check for the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to check for the global pref (applies to all sites)  
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to check for the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to check for the global pref (applies to all sites)  
</td>
</tr>

</table>

### removePref(aGroup, aName, aContext) ###
  
Remove a pref.  
  
@param    aGroup      the group for which to remove the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to remove the global pref (applies to all sites)   
@param    aName       the name of the pref to remove  
@param    aPrivacyContext  
                      a context from which to determine the privacy status  
                      of the pref (ie. whether to search in memory or in  
                      permanent storage for it), obtained from a relevant  
                      window or channel.  
@throws   NS_ERROR_ILLEGAL_VALUE if aGroup is not a string, nsIURI, or null  
@throws   NS_ERROR_ILLEGAL_VALUE if aName is null or an empty string  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aGroup      the group for which to remove the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to remove the global pref (applies to all sites)   
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to remove the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to remove the global pref (applies to all sites)   
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to remove the pref, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to remove the global pref (applies to all sites)   
</td>
</tr>

</table>

### removeGroupedPrefs(aContext) ###
  
Remove all grouped prefs.  Useful for removing references to the sites  
the user has visited when the user clears their private data.  
  
@param    aPrivacyContext  
                      a context from which to determine the privacy status  
                      of the pref (ie. whether to remove prefs in memory or  
                      in permanent storage), obtained from a relevant  
                      window or channel.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aPrivacyContext  
                      a context from which to determine the privacy status  
                      of the pref (ie. whether to remove prefs in memory or  
                      in permanent storage), obtained from a relevant  
                      window or channel.  
</td>
</tr>

</table>

### removePrefsByName(aName, aContext) ###
  
Remove all prefs with the given name.  
  
@param    aName        the setting name for which to remove prefs  
@param    aPrivacyContext  
                       a context from which to determine the privacy status  
                       of the prefs (ie. whether to remove prefs in memory or  
                       in permanent storage), obtained from a relevant  
                       window or channel.  
@throws   NS_ERROR_ILLEGAL_VALUE if aName is null or an empty string  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName        the setting name for which to remove prefs  
</td>
</tr>

<tr>
<td></td>
<td>aName        the setting name for which to remove prefs  
</td>
</tr>

</table>

### getPrefs(aGroup, aContext) ###
  
Get the prefs that apply to the given site.  
  
@param    aGroup      the group for which to retrieve prefs, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to get the global prefs (apply to all sites)   
@param    aPrivacyContext  
                      a context from which to determine the privacy status  
                      of the pref (ie. whether to search for prefs in memory  
                      or in permanent storage), obtained from a relevant  
                      window or channel.  
  
@returns  a property bag of prefs  
@throws   NS_ERROR_ILLEGAL_VALUE if aGroup is not a string, nsIURI, or null  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aGroup      the group for which to retrieve prefs, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to get the global prefs (apply to all sites)   
</td>
</tr>

<tr>
<td></td>
<td>aGroup      the group for which to retrieve prefs, as an nsIURI  
                      from which the hostname will be used, a string  
                      (typically in the format of a hostname), or null  
                      to get the global prefs (apply to all sites)   
</td>
</tr>

</table>

### getPrefsByName(aName, aContext) ###
  
Get the prefs with the given name.  
  
@param    aName        the setting name for which to retrieve prefs  
@param    aPrivacyContext  
                       a context from which to determine the privacy status  
                       of the pref (ie. whether to search for prefs in memory  
                       or in permanent storage), obtained from a relevant  
                       window or channel.  
  
@returns  a property bag of prefs  
@throws   NS_ERROR_ILLEGAL_VALUE if aName is null or an empty string  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName        the setting name for which to retrieve prefs  
</td>
</tr>

<tr>
<td></td>
<td>aName        the setting name for which to retrieve prefs  
</td>
</tr>

</table>

### addObserver(aName, aObserver) ###
  
Add an observer.  
  
@param    aName       the setting to observe, or null to add  
                      a generic observer that observes all settings  
@param    aObserver   the observer to add  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName       the setting to observe, or null to add  
                      a generic observer that observes all settings  
</td>
</tr>

<tr>
<td></td>
<td>aName       the setting to observe, or null to add  
                      a generic observer that observes all settings  
</td>
</tr>

</table>

### removeObserver(aName, aObserver) ###
  
Remove an observer.  
  
@param    aName       the setting being observed, or null to remove  
                      a generic observer that observes all settings  
@param    aObserver   the observer to remove  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName       the setting being observed, or null to remove  
                      a generic observer that observes all settings  
</td>
</tr>

<tr>
<td></td>
<td>aName       the setting being observed, or null to remove  
                      a generic observer that observes all settings  
</td>
</tr>

</table>

## Attributes ##

### grouper ###
  
The component that the service uses to determine the groups to which  
URIs belong.  By default this is the "hostname grouper", which groups  
URIs by full hostname (a.k.a. site).  
  

### DBConnection ###
  
The database connection to the content preferences database.  
Useful for accessing and manipulating preferences in ways that are caller-  
specific or for which there is not yet a generic method, although generic  
functionality useful to multiple callers should generally be added to this  
unfrozen interface.  Also useful for testing the database creation  
and migration code.  
  
