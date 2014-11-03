---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIPrintOptions.idl">Source file</a>
</div>

# nsIPrinterEnumerator #

## Methods ##

### initPrintSettingsFromPrinter(aPrinterName, aPrintSettings) ###
<code>  
Initializes certain settings from the native printer into the PrintSettings  
These settings include, but are not limited to:  
  Page Orientation  
  Page Size  
  Number of Copies  
  
</code>
### displayPropertiesDlg(aPrinter, aPrintSettings) ###

## Attributes ##

### defaultPrinterName ###
  
The name of the system default printer. This name should also be  
present in printerNameList below. This is not necessarily gecko's  
default printer; see nsIPrintSettingsService.defaultPrinterName  
for that.  
  

### printerNameList ###
  
The list of printer names  
  
