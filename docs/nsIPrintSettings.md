---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIPrintSettings.idl">Source file</a>
</div>
# nsIPrintSettings #
  
Simplified graphics interface for JS rendering.  
  

## Methods ##

### SetPrintOptions(aType, aTurnOnOff) ###
  
Set PrintOptions   
  

### GetPrintOptions(aType) ###
  
Get PrintOptions   
  

### GetPrintOptionsBits() ###
  
Set PrintOptions Bit field  
  

### GetEffectivePageSize(aWidth, aHeight) ###
  
Get the page size in twips, considering the  
orientation (portrait or landscape).  
  

### clone() ###
  
Makes a new copy  
  

### assign(aPS) ###
  
Assigns the internal values from the "in" arg to the current object  
  

### SetMarginInTwips(aMargin) ###

### SetEdgeInTwips(aEdge) ###

### GetMarginInTwips(aMargin) ###

### GetEdgeInTwips(aEdge) ###

### SetupSilentPrinting() ###
  
We call this function so that anything that requires a run of the event loop  
can do so safely. The print dialog runs the event loop but in silent printing  
that doesn't happen.  
  
Either this or ShowPrintDialog (but not both) MUST be called by the print engine  
before printing, otherwise printing can fail on some platforms.  
  

### SetUnwriteableMarginInTwips(aEdge) ###
  
Sets/Gets the "unwriteable margin" for the page format.  This defines  
the boundary from which we'll measure the EdgeInTwips and MarginInTwips   
attributes, to place the headers and content, respectively.  
  
Note: Implementations of SetUnwriteableMarginInTwips should handle  
negative margin values by falling back on the system default for  
that margin.  
  

### GetUnwriteableMarginInTwips(aEdge) ###

### GetPageRanges(aPages) ###
  
Get more accurate print ranges from the superior interval   
(startPageRange, endPageRange). The aPages array is populated with a   
list of pairs (start, end), where the endpoints are included. The print   
ranges (start, end), must not overlap and must be in the   
(startPageRange, endPageRange) scope.  
  
If there are no print ranges the aPages array is cleared.  
  

## Attributes ##

### printSession ###
  
Data Members  
  

### startPageRange ###

### endPageRange ###

### edgeTop ###
  
The edge measurements define the positioning of the headers  
and footers on the page. They're measured as an offset from  
the "unwriteable margin" (described below).  
  

### edgeLeft ###

### edgeBottom ###

### edgeRight ###

### marginTop ###
  
The margins define the positioning of the content on the page.  
They're treated as an offset from the "unwriteable margin"  
(described below).  
  

### marginLeft ###

### marginBottom ###

### marginRight ###

### unwriteableMarginTop ###
  
The unwriteable margin defines the printable region of the paper, creating  
an invisible border from which the edge and margin attributes are measured.  
  

### unwriteableMarginLeft ###

### unwriteableMarginBottom ###

### unwriteableMarginRight ###

### scaling ###

### printBGColors ###

### printBGImages ###

### printRange ###

### title ###

### docURL ###

### headerStrLeft ###

### headerStrCenter ###

### headerStrRight ###

### footerStrLeft ###

### footerStrCenter ###

### footerStrRight ###

### howToEnableFrameUI ###

### isCancelled ###

### printFrameTypeUsage ###

### printFrameType ###

### printSilent ###

### shrinkToFit ###

### showPrintProgress ###

### paperName ###

### paperSizeType ###

### paperData ###

### paperWidth ###

### paperHeight ###

### paperSizeUnit ###

### plexName ###

### colorspace ###

### resolutionName ###

### downloadFonts ###

### printReversed ###

### printInColor ###

### orientation ###

### printCommand ###

### numCopies ###

### printerName ###

### printToFile ###

### toFileName ###

### outputFormat ###

### printPageDelay ###

### resolution ###

### duplex ###

### isInitializedFromPrinter ###
  
This attribute tracks whether the PS has been initialized   
from a printer specified by the "printerName" attr.   
If a different name is set into the "printerName"   
attribute than the one it was initialized with the PS  
will then get intialized from that printer.  
  

### isInitializedFromPrefs ###
  
This attribute tracks whether the PS has been initialized   
from prefs. If a different name is set into the "printerName"   
attribute than the one it was initialized with the PS  
will then get intialized from prefs again.  
  

### persistMarginBoxSettings ###
  
This attribute tracks if the settings made on the margin box is  
stored in the prefs or not.  
  

## Constants ##

### kInitSaveOddEvenPages ###
  
PrintSettings to be Saved Navigation Constants  
  

### kInitSaveHeaderLeft ###

### kInitSaveHeaderCenter ###

### kInitSaveHeaderRight ###

### kInitSaveFooterLeft ###

### kInitSaveFooterCenter ###

### kInitSaveFooterRight ###

### kInitSaveBGColors ###

### kInitSaveBGImages ###

### kInitSavePaperSize ###

### kInitSaveResolution ###

### kInitSaveDuplex ###

### kInitSavePaperData ###

### kInitSaveUnwriteableMargins ###

### kInitSaveEdges ###

### kInitSaveReversed ###

### kInitSaveInColor ###

### kInitSaveOrientation ###

### kInitSavePrintCommand ###

### kInitSavePrinterName ###

### kInitSavePrintToFile ###

### kInitSaveToFileName ###

### kInitSavePageDelay ###

### kInitSaveMargins ###

### kInitSaveNativeData ###

### kInitSavePlexName ###

### kInitSaveShrinkToFit ###

### kInitSaveScaling ###

### kInitSaveColorspace ###

### kInitSaveResolutionName ###

### kInitSaveDownloadFonts ###

### kInitSaveAll ###

### kPrintOddPages ###

### kPrintEvenPages ###

### kEnableSelectionRB ###

### kRangeAllPages ###

### kRangeSpecifiedPageRange ###

### kRangeSelection ###

### kRangeFocusFrame ###

### kJustLeft ###

### kJustCenter ###

### kJustRight ###

### kUseInternalDefault ###
  
FrameSet Default Type Constants  
  

### kUseSettingWhenPossible ###

### kPaperSizeNativeData ###
  
Page Size Type Constants  
  

### kPaperSizeDefined ###

### kPaperSizeInches ###
  
Page Size Unit Constants  
  

### kPaperSizeMillimeters ###

### kPortraitOrientation ###
  
Orientation Constants  
  

### kLandscapeOrientation ###

### kNoFrames ###
  
Print Frame Constants  
  

### kFramesAsIs ###

### kSelectedFrame ###

### kEachFrameSep ###

### kFrameEnableNone ###
  
How to Enable Frame Set Printing Constants  
  

### kFrameEnableAll ###

### kFrameEnableAsIsAndEach ###

### kOutputFormatNative ###
  
Output file format  
  

### kOutputFormatPS ###

### kOutputFormatPDF ###
