---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIPrintSettings.idl">Source file</a>
</div>

# nsIPrintSettings #
<pre>  
Simplified graphics interface for JS rendering.  
  
</pre>
## Methods ##

### SetPrintOptions(aType, aTurnOnOff) ###
<pre>  
Set PrintOptions   
  
</pre>
### GetPrintOptions(aType) ###
<pre>  
Get PrintOptions   
  
</pre>
### GetPrintOptionsBits() ###
<pre>  
Set PrintOptions Bit field  
  
</pre>
### GetEffectivePageSize(aWidth, aHeight) ###
<pre>  
Get the page size in twips, considering the  
orientation (portrait or landscape).  
  
</pre>
### clone() ###
<pre>  
Makes a new copy  
  
</pre>
### assign(aPS) ###
<pre>  
Assigns the internal values from the "in" arg to the current object  
  
</pre>
### SetMarginInTwips(aMargin) ###

### SetEdgeInTwips(aEdge) ###

### GetMarginInTwips(aMargin) ###

### GetEdgeInTwips(aEdge) ###

### SetupSilentPrinting() ###
<pre>  
We call this function so that anything that requires a run of the event loop  
can do so safely. The print dialog runs the event loop but in silent printing  
that doesn't happen.  
  
Either this or ShowPrintDialog (but not both) MUST be called by the print engine  
before printing, otherwise printing can fail on some platforms.  
  
</pre>
### SetUnwriteableMarginInTwips(aEdge) ###
<pre>  
Sets/Gets the "unwriteable margin" for the page format.  This defines  
the boundary from which we'll measure the EdgeInTwips and MarginInTwips   
attributes, to place the headers and content, respectively.  
  
Note: Implementations of SetUnwriteableMarginInTwips should handle  
negative margin values by falling back on the system default for  
that margin.  
  
</pre>
### GetUnwriteableMarginInTwips(aEdge) ###

### GetPageRanges(aPages) ###
<pre>  
Get more accurate print ranges from the superior interval   
(startPageRange, endPageRange). The aPages array is populated with a   
list of pairs (start, end), where the endpoints are included. The print   
ranges (start, end), must not overlap and must be in the   
(startPageRange, endPageRange) scope.  
  
If there are no print ranges the aPages array is cleared.  
  
</pre>
## Attributes ##

### printSession ###
<pre>  
Data Members  
  
</pre>
### startPageRange ###

### endPageRange ###

### edgeTop ###
<pre>  
The edge measurements define the positioning of the headers  
and footers on the page. They're measured as an offset from  
the "unwriteable margin" (described below).  
  
</pre>
### edgeLeft ###

### edgeBottom ###

### edgeRight ###

### marginTop ###
<pre>  
The margins define the positioning of the content on the page.  
They're treated as an offset from the "unwriteable margin"  
(described below).  
  
</pre>
### marginLeft ###

### marginBottom ###

### marginRight ###

### unwriteableMarginTop ###
<pre>  
The unwriteable margin defines the printable region of the paper, creating  
an invisible border from which the edge and margin attributes are measured.  
  
</pre>
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
<pre>  
This attribute tracks whether the PS has been initialized   
from a printer specified by the "printerName" attr.   
If a different name is set into the "printerName"   
attribute than the one it was initialized with the PS  
will then get intialized from that printer.  
  
</pre>
### isInitializedFromPrefs ###
<pre>  
This attribute tracks whether the PS has been initialized   
from prefs. If a different name is set into the "printerName"   
attribute than the one it was initialized with the PS  
will then get intialized from prefs again.  
  
</pre>
### persistMarginBoxSettings ###
<pre>  
This attribute tracks if the settings made on the margin box is  
stored in the prefs or not.  
  
</pre>
## Constants ##

### kInitSaveOddEvenPages ###
<pre>  
PrintSettings to be Saved Navigation Constants  
  
</pre>
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
<pre>  
FrameSet Default Type Constants  
  
</pre>
### kUseSettingWhenPossible ###

### kPaperSizeNativeData ###
<pre>  
Page Size Type Constants  
  
</pre>
### kPaperSizeDefined ###

### kPaperSizeInches ###
<pre>  
Page Size Unit Constants  
  
</pre>
### kPaperSizeMillimeters ###

### kPortraitOrientation ###
<pre>  
Orientation Constants  
  
</pre>
### kLandscapeOrientation ###

### kNoFrames ###
<pre>  
Print Frame Constants  
  
</pre>
### kFramesAsIs ###

### kSelectedFrame ###

### kEachFrameSep ###

### kFrameEnableNone ###
<pre>  
How to Enable Frame Set Printing Constants  
  
</pre>
### kFrameEnableAll ###

### kFrameEnableAsIsAndEach ###

### kOutputFormatNative ###
<pre>  
Output file format  
  
</pre>
### kOutputFormatPS ###

### kOutputFormatPDF ###
