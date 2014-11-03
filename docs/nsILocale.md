---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/locale/nsILocale.idl">Source file</a>
</div>

# nsILocale #
<pre>  
Represents one locale, which can be used for things like sorting text strings  
and formatting numbers, dates and times.  
  
</pre>
## Methods ##

### getCategory(category) ###
<pre>  
Get the locale code for a given category.  
  
A locale code is of the form language[-COUNTRY[-region]], where  
"language" is an ISO 639 language code (two letter codes preferred over  
three letter codes when available), "COUNTRY" is an ISO 3166 two letter  
country code, and "region" is a string of up to 5 letters.  
  
A category is one of the following:  
NSILOCALE_CTYPE: Character classification and case conversion.  
NSILOCALE_COLLATE: Collation order. How strings are sorted.  
NSILOCALE_MONETARY: Monetary formatting.  
NSILOCALE_NUMERIC: Numeric, non-monetary formatting.  
NSILOCALE_TIME: Date and time formats.  
NSILOCALE_MESSAGES: Related to fonts, character encodings etc.  
  
@param category  
       The category of interest.  
@return The locale code to be used for the given category.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>category</td>
<td>       The category of interest.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The locale code to be used for the given category.  
</td>
</tr>

</table>
