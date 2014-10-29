---
layout: default
---

# nsIPrinterEnumerator #

## defaultPrinterName ##

The name of the system default printer. This name should also be
present in printerNameList below. This is not necessarily gecko's
default printer; see nsIPrintSettingsService.defaultPrinterName
for that.


## initPrintSettingsFromPrinter ##

Initializes certain settings from the native printer into the PrintSettings
These settings include, but are not limited to:
  Page Orientation
  Page Size
  Number of Copies


## printerNameList ##

The list of printer names


## displayPropertiesDlg ##
