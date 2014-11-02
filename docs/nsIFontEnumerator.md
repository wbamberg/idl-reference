---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/gfx/src/nsIFontEnumerator.idl">Source file</a>
</div>
# nsIFontEnumerator #

## Methods ##

### EnumerateAllFonts(aCount, aResult) ###
  
Return a sorted array of the names of all installed fonts.  
  
@param  aCount     returns number of names returned  
@param  aResult    returns array of names  
@return void  
  

#### Parameters ####

<table>

<tr>
<td>aCount</td>
<td>returns number of names returned  
</td>
</tr>

<tr>
<td>aResult</td>
<td>returns array of names  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>void  
</td>
</tr>

</table>

### EnumerateFonts(aLangGroup, aGeneric, aCount, aResult) ###
  
Return a sorted array of names of fonts that support the given language  
group and are suitable for use as the given CSS generic font.  
  
@param  aLangGroup language group  
@param  aGeneric   CSS generic font  
@param  aCount     returns number of names returned  
@param  aResult    returns array of names  
@return void  
  

#### Parameters ####

<table>

<tr>
<td>aLangGroup</td>
<td>language group  
</td>
</tr>

<tr>
<td>aGeneric</td>
<td>CSS generic font  
</td>
</tr>

<tr>
<td>aCount</td>
<td>returns number of names returned  
</td>
</tr>

<tr>
<td>aResult</td>
<td>returns array of names  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>void  
</td>
</tr>

</table>

### HaveFontFor(aLangGroup, aResult) ###
  
@param  aLangGroup language group  
@return bool do we have a font for this language group  
  

#### Parameters ####

<table>

<tr>
<td>aLangGroup</td>
<td>language group  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>bool do we have a font for this language group  
</td>
</tr>

</table>

### getDefaultFont(aLangGroup, aGeneric) ###
  
@param  aLangGroup language group  
@param  aGeneric CSS generic font  
@return suggested default font for this language group and generic family  
  

#### Parameters ####

<table>

<tr>
<td>aLangGroup</td>
<td>language group  
</td>
</tr>

<tr>
<td>aGeneric</td>
<td>CSS generic font  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>suggested default font for this language group and generic family  
</td>
</tr>

</table>

### updateFontList() ###
  
update the global font list  
return true if font list is changed  
  

### getStandardFamilyName(aName) ###
  
get the standard family name on the system from given family  
@param  aName family name which may be alias  
@return the standard family name on the system, if given name does not  
        exist, returns empty string  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>family name which may be alias  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the standard family name on the system, if given name does not  
        exist, returns empty string  
</td>
</tr>

</table>
