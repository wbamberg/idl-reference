---
layout: default
---

# nsILocaleService #
  
The Locale service interface. This is a singleton object, and should be  
obtained from the <tt>nsServiceManager</tt>.  
  

## Methods ##

### newLocale(aLocale) ###
  
Create a new nsILocale from a locale string.  
  
@param aLocale  
       A locale code as described in nsILocale.  
@return A nsILocale representing the given locale.  
  

#### Parameters ####

<table>

<tr>
<td>aLocale</td>
<td>       A locale code as described in nsILocale.  
</td>
</tr>

</table>

### getSystemLocale() ###
  
Get the user preference for locale from the operating system.  
  
@return User's OS setting for preferred locale.  
  

### getApplicationLocale() ###
  
Get the user preference for locale from the operating system.  
  
NOTE: This has nothing to do with the locale used for localization of  
the application (UI text strings etc.). This method returns something  
similar to getSystemLocale.  
  
@return User's OS setting for preferred locale.  
  

### getLocaleFromAcceptLanguage(acceptLanguage) ###
  
Get the most preferred locale from a list of locale preferences.  
  
@param acceptLanguage  
       Locale preference in the same format as the Accept-Language HTTP  
       header.  
@return The most preferred locale according to the acceptLanguage  
        parameter.  
  

#### Parameters ####

<table>

<tr>
<td>acceptLanguage</td>
<td>       Locale preference in the same format as the Accept-Language HTTP  
       header.  
</td>
</tr>

</table>

### getLocaleComponentForUserAgent() ###
  
Get the user preference for locale from the operating system.  
  
NOTE: This has nothing to do with any HTTP User-Agent. This method  
returns the same as getSystemLocale, but as a string.  
  
@return User's OS setting for preferred locale in the format described  
        in nsILocale.  
  
