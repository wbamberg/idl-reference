---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/urlformatter/nsIURLFormatter.idl">Source file</a>
</div>

# nsIURLFormatter #

## Methods ##

### formatURL(aFormat) ###
<code>   
formatURL - Formats a string URL  
  
The set of known variables is predefined.  
If a variable is unknown, it is left unchanged and a non-fatal error is reported.  
  
@param aFormat string Unformatted URL.  
  
@return The formatted URL.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aFormat</td>
<td>string Unformatted URL.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The formatted URL.  
</td>
</tr>

</table>

### formatURLPref(aPref) ###
<code>   
formatURLPref - Formats a string URL stored in a preference  
  
If the preference value cannot be retrieved, a fatal error is reported  
and the "about:blank" URL is returned.  
  
@param aPref string Preference name.  
  
@return The formatted URL returned by formatURL(), or "about:blank".  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aPref</td>
<td>string Preference name.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The formatted URL returned by formatURL(), or "about:blank".  
</td>
</tr>

</table>
