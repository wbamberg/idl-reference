---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIPrintOptions.idl">Source file</a>
</div>

# nsIPrintOptions #
<code>  
Print options interface  
  
Do not attempt to freeze this API - it still needs lots of work. Consult  
John Keiser <jkeiser@netscape.com> and Roland Mainz  
<roland.mainz@informatik.med.uni-giessen.de> for futher details.  
  
</code>
## Methods ##

### ShowPrintSetupDialog(aThePrintSettings) ###
<code>  
Show Native Print Options dialog, this may not be supported on all platforms  
  
</code>
### CreatePrintSettings() ###
<code>  
Creates a new PrintSettnigs Object  
and initializes it from prefs  
  
</code>
### getPrinterPrefInt(aPrintSettings, aPrefName) ###
<code>  
Get a prefixed integer pref   
  
</code>
### displayJobProperties(aPrinter, aPrintSettings, aDisplayed) ###
<code>  
display Printer Job Properties dialog  
  
</code>
### GetNativeData(aDataType) ###

## Constants ##

### kNativeDataPrintRecord ###
  
Native data constants  
  
