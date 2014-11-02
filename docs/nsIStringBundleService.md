---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/strres/nsIStringBundle.idl">Source file</a>
</div>
# nsIStringBundleService #

## Methods ##

### createBundle(aURLSpec) ###

### createExtensibleBundle(aRegistryKey) ###

### formatStatusMessage(aStatus, aStatusArg) ###
  
Formats a message string from a status code and status arguments.  
@param aStatus - The status code. This is mapped into a string ID and  
           and used in the string lookup process (see nsIErrorService).  
@param aStatusArg - The status message argument(s). Multiple arguments  
           can be separated by newline ('\n') characters.  
@return the formatted message  
  

#### Parameters ####

<table>

<tr>
<td>aStatus</td>
<td>- The status code. This is mapped into a string ID and  
           and used in the string lookup process (see nsIErrorService).  
</td>
</tr>

<tr>
<td>aStatusArg</td>
<td>- The status message argument(s). Multiple arguments  
           can be separated by newline ('\n') characters.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the formatted message  
</td>
</tr>

</table>

### flushBundles() ###
  
flushes the string bundle cache - useful when the locale changes or  
when we need to get some extra memory back  
  
at some point, we might want to make this flush all the bundles,  
because any bundles that are floating around when the locale changes  
will suddenly contain bad data  
  
  
