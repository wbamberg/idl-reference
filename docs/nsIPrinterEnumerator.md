---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIPrintOptions.idl">Source file</a>
</div>

# nsIPrinterEnumerator #

## Methods ##

### initPrintSettingsFromPrinter(aPrinterName, aPrintSettings) ###
<pre>  
Initializes certain settings from the native printer into the PrintSettings  
These settings include, but are not limited to:  
  Page Orientation  
  Page Size  
  Number of Copies  
  
</pre>
### displayPropertiesDlg(aPrinter, aPrintSettings) ###

## Attributes ##

### defaultPrinterName ###
<pre>  
The name of the system default printer. This name should also be  
present in printerNameList below. This is not necessarily gecko's  
default printer; see nsIPrintSettingsService.defaultPrinterName  
for that.  
  
</pre>
### printerNameList ###
<pre>  
The list of printer names  
  
</pre>