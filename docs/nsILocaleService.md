---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/locale/nsILocaleService.idl">Source file</a>
</div>

# nsILocaleService #
  
The Locale service interface. This is a singleton object, and should be  
obtained from the <tt>nsServiceManager</tt>.  
  

## Methods ##

### newLocale(aLocale) ###
  
Create a new nsILocale from a locale string.  
  
  

#### Parameters ####

<table>

<tr>
<td>aLocale</td>
<td>       A locale code as described in nsILocale.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A nsILocale representing the given locale.  
</td>
</tr>

</table>

### getSystemLocale() ###
  
Get the user preference for locale from the operating system.  
  
  

#### Returns ####

<table>

<tr>
<td>User's OS setting for preferred locale.  
</td>
</tr>

</table>

### getApplicationLocale() ###
  
Get the user preference for locale from the operating system.  
  
NOTE: This has nothing to do with the locale used for localization of  
the application (UI text strings etc.). This method returns something  
similar to getSystemLocale.  
  
  

#### Returns ####

<table>

<tr>
<td>User's OS setting for preferred locale.  
</td>
</tr>

</table>

### getLocaleFromAcceptLanguage(acceptLanguage) ###
  
Get the most preferred locale from a list of locale preferences.  
  
  

#### Parameters ####

<table>

<tr>
<td>acceptLanguage</td>
<td>       Locale preference in the same format as the Accept-Language HTTP  
       header.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The most preferred locale according to the acceptLanguage  
        parameter.  
</td>
</tr>

</table>

### getLocaleComponentForUserAgent() ###
  
Get the user preference for locale from the operating system.  
  
NOTE: This has nothing to do with any HTTP User-Agent. This method  
returns the same as getSystemLocale, but as a string.  
  
  

#### Returns ####

<table>

<tr>
<td>User's OS setting for preferred locale in the format described  
        in nsILocale.  
</td>
</tr>

</table>
