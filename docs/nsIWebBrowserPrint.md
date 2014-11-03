---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIWebBrowserPrint.idl">Source file</a>
</div>

# nsIWebBrowserPrint #
<pre>  
nsIWebBrowserPrint corresponds to the main interface  
for printing an embedded Gecko web browser window/document  
  
</pre>
## Methods ##

### print(aThePrintSettings, aWPListener) ###
<pre>  
Print the specified DOM window  
  
@param aThePrintSettings - Printer Settings for the print job, if aThePrintSettings is null  
                           then the global PS will be used.  
@param aWPListener - is updated during the print  
@return void  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aThePrintSettings</td>
<td>- Printer Settings for the print job, if aThePrintSettings is null  
                           then the global PS will be used.  
</td>
</tr>

<tr>
<td>aWPListener</td>
<td>- is updated during the print  
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

### printPreview(aThePrintSettings, aChildDOMWin, aWPListener) ###
<pre>  
Print Preview the specified DOM window  
  
@param aThePrintSettings - Printer Settings for the print preview, if aThePrintSettings is null  
                           then the global PS will be used.  
@param aChildDOMWin - DOM Window to be print previewed.  
@param aWPListener - is updated during the printpreview  
@return void  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aThePrintSettings</td>
<td>- Printer Settings for the print preview, if aThePrintSettings is null  
                           then the global PS will be used.  
</td>
</tr>

<tr>
<td>aChildDOMWin</td>
<td>- DOM Window to be print previewed.  
</td>
</tr>

<tr>
<td>aWPListener</td>
<td>- is updated during the printpreview  
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

### printPreviewNavigate(aNavType, aPageNum) ###
<pre>  
Print Preview - Navigates within the window  
  
@param aNavType - navigation enum  
@param aPageNum - page num to navigate to when aNavType = ePrintPreviewGoToPageNum  
@return void  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aNavType</td>
<td>- navigation enum  
</td>
</tr>

<tr>
<td>aPageNum</td>
<td>- page num to navigate to when aNavType = ePrintPreviewGoToPageNum  
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

### cancel() ###
<pre>  
Cancels the current print   
@return void  
  
</pre>
#### Returns ####

<table>

<tr>
<td>void  
</td>
</tr>

</table>

### enumerateDocumentNames(aCount, aResult) ###
<pre>  
Returns an array of the names of all documents names (Title or URL)  
and sub-documents. This will return a single item if the attr "isFramesetDocument" is false  
and may return any number of items is "isFramesetDocument" is true  
  
@param  aCount - returns number of printers returned  
@param  aResult - returns array of names  
@return void  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aCount</td>
<td>- returns number of printers returned  
</td>
</tr>

<tr>
<td>aResult</td>
<td>- returns array of names  
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

### exitPrintPreview() ###
<pre>  
This exists PrintPreview mode and returns browser window to galley mode  
@return void  
  
</pre>
#### Returns ####

<table>

<tr>
<td>void  
</td>
</tr>

</table>

## Attributes ##

### globalPrintSettings ###
<pre>  
Returns a "global" PrintSettings object   
Creates a new the first time, if one doesn't exist.  
  
Then returns the same object each time after that.  
  
Initializes the globalPrintSettings from the default printer  
  
</pre>
### currentPrintSettings ###
<pre>  
Returns a pointer to the PrintSettings object that  
that was passed into either "print" or "print preview"  
  
This enables any consumers of the interface to have access  
to the "current" PrintSetting at later points in the execution  
  
</pre>
### currentChildDOMWindow ###
<pre>  
Returns a pointer to the current child DOMWindow  
that is being print previewed. (FrameSet Frames)  
  
Returns null if parent document is not a frameset or the entire FrameSet   
document is being print previewed  
  
This enables any consumers of the interface to have access  
to the "current" child DOMWindow at later points in the execution  
  
</pre>
### doingPrint ###
<pre>  
Returns whether it is in Print mode  
  
</pre>
### doingPrintPreview ###
<pre>  
Returns whether it is in Print Preview mode  
  
</pre>
### isFramesetDocument ###
<pre>  
This returns whether the current document is a frameset document  
  
</pre>
### isFramesetFrameSelected ###
<pre>  
This returns whether the current document is a frameset document  
  
</pre>
### isIFrameSelected ###
<pre>  
This returns whether there is an IFrame selected  
  
</pre>
### isRangeSelection ###
<pre>  
This returns whether there is a "range" selection  
  
</pre>
### printPreviewNumPages ###
<pre>  
This returns the total number of pages for the Print Preview  
  
</pre>
## Constants ##

### PRINTPREVIEW_GOTO_PAGENUM ###
<pre>  
PrintPreview Navigation Constants  
  
</pre>
### PRINTPREVIEW_PREV_PAGE ###

### PRINTPREVIEW_NEXT_PAGE ###

### PRINTPREVIEW_HOME ###

### PRINTPREVIEW_END ###
