---
layout: default
---

# nsIPrintOptions #
  
Print options interface  
  
Do not attempt to freeze this API - it still needs lots of work. Consult  
John Keiser <jkeiser@netscape.com> and Roland Mainz  
<roland.mainz@informatik.med.uni-giessen.de> for futher details.  
  

## Methods ##

### ShowPrintSetupDialog(aThePrintSettings) ###
  
Show Native Print Options dialog, this may not be supported on all platforms  
  

### CreatePrintSettings() ###
  
Creates a new PrintSettnigs Object  
and initializes it from prefs  
  

### getPrinterPrefInt(aPrintSettings, aPrefName) ###
  
Get a prefixed integer pref   
  

### displayJobProperties(aPrinter, aPrintSettings, aDisplayed) ###
  
display Printer Job Properties dialog  
  

### GetNativeData(aDataType) ###

## Constants ##

### kNativeDataPrintRecord ###
  
Native data constants  
  
