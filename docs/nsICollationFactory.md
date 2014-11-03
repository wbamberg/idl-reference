---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/locale/nsICollation.idl">Source file</a>
</div>

# nsICollationFactory #

## Methods ##

### CreateCollation(locale) ###
  
Create the collation for a given locale.  
  
Use NULL as the locale parameter to use the user's locale preference  
from the operating system.  
  
@param locale  
       The locale for which to create the collation or null to use  
       user preference.  
@return A collation for the given locale.  
  

#### Parameters ####

<table>

<tr>
<td>locale</td>
<td>       The locale for which to create the collation or null to use  
       user preference.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A collation for the given locale.  
</td>
</tr>

</table>
