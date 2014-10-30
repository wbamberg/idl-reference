---
layout: default
---

# nsIFontEnumerator #

## Methods ##

### EnumerateAllFonts(aCount, aResult) ###
  
Return a sorted array of the names of all installed fonts.  
  
@param  aCount     returns number of names returned  
@param  aResult    returns array of names  
@return void  
  

### EnumerateFonts(aLangGroup, aGeneric, aCount, aResult) ###
  
Return a sorted array of names of fonts that support the given language  
group and are suitable for use as the given CSS generic font.  
  
@param  aLangGroup language group  
@param  aGeneric   CSS generic font  
@param  aCount     returns number of names returned  
@param  aResult    returns array of names  
@return void  
  

### HaveFontFor(aLangGroup, aResult) ###
  
@param  aLangGroup language group  
@return bool do we have a font for this language group  
  

### getDefaultFont(aLangGroup, aGeneric) ###
  
@param  aLangGroup language group  
@param  aGeneric CSS generic font  
@return suggested default font for this language group and generic family  
  

### updateFontList() ###
  
update the global font list  
return true if font list is changed  
  

### getStandardFamilyName(aName) ###
  
get the standard family name on the system from given family  
@param  aName family name which may be alias  
@return the standard family name on the system, if given name does not  
        exist, returns empty string  
  
