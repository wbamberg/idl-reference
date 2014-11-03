---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIPrintOptions.idl">Source file</a>
</div>

# nsIPrintOptions #
<pre>  
Print options interface  
  
Do not attempt to freeze this API - it still needs lots of work. Consult  
John Keiser <jkeiser@netscape.com> and Roland Mainz  
<roland.mainz@informatik.med.uni-giessen.de> for futher details.  
  
</pre>
## Methods ##

### ShowPrintSetupDialog(aThePrintSettings) ###
<pre>  
Show Native Print Options dialog, this may not be supported on all platforms  
  
</pre>
### CreatePrintSettings() ###
<pre>  
Creates a new PrintSettnigs Object  
and initializes it from prefs  
  
</pre>
### getPrinterPrefInt(aPrintSettings, aPrefName) ###
<pre>  
Get a prefixed integer pref   
  
</pre>
### displayJobProperties(aPrinter, aPrintSettings, aDisplayed) ###
<pre>  
display Printer Job Properties dialog  
  
</pre>
### GetNativeData(aDataType) ###

## Constants ##

### kNativeDataPrintRecord ###
<pre>  
Native data constants  
  
</pre>