---
layout: default
---

# nsIWebBrowserPrint #

nsIWebBrowserPrint corresponds to the main interface
for printing an embedded Gecko web browser window/document


## Methods ##

### print ###

Print the specified DOM window

@param aThePrintSettings - Printer Settings for the print job, if aThePrintSettings is null
                           then the global PS will be used.
@param aWPListener - is updated during the print
@return void


### printPreview ###

Print Preview the specified DOM window

@param aThePrintSettings - Printer Settings for the print preview, if aThePrintSettings is null
                           then the global PS will be used.
@param aChildDOMWin - DOM Window to be print previewed.
@param aWPListener - is updated during the printpreview
@return void


### printPreviewNavigate ###

Print Preview - Navigates within the window

@param aNavType - navigation enum
@param aPageNum - page num to navigate to when aNavType = ePrintPreviewGoToPageNum
@return void


### cancel ###

Cancels the current print 
@return void


### enumerateDocumentNames ###

Returns an array of the names of all documents names (Title or URL)
and sub-documents. This will return a single item if the attr "isFramesetDocument" is false
and may return any number of items is "isFramesetDocument" is true

@param  aCount - returns number of printers returned
@param  aResult - returns array of names
@return void


### exitPrintPreview ###

This exists PrintPreview mode and returns browser window to galley mode
@return void


## Attributes ##

### globalPrintSettings ###

Returns a "global" PrintSettings object 
Creates a new the first time, if one doesn't exist.

Then returns the same object each time after that.

Initializes the globalPrintSettings from the default printer


### currentPrintSettings ###

Returns a pointer to the PrintSettings object that
that was passed into either "print" or "print preview"

This enables any consumers of the interface to have access
to the "current" PrintSetting at later points in the execution


### currentChildDOMWindow ###

Returns a pointer to the current child DOMWindow
that is being print previewed. (FrameSet Frames)

Returns null if parent document is not a frameset or the entire FrameSet 
document is being print previewed

This enables any consumers of the interface to have access
to the "current" child DOMWindow at later points in the execution


### doingPrint ###

Returns whether it is in Print mode


### doingPrintPreview ###

Returns whether it is in Print Preview mode


### isFramesetDocument ###

This returns whether the current document is a frameset document


### isFramesetFrameSelected ###

This returns whether the current document is a frameset document


### isIFrameSelected ###

This returns whether there is an IFrame selected


### isRangeSelection ###

This returns whether there is a "range" selection


### printPreviewNumPages ###

This returns the total number of pages for the Print Preview


## Constants ##

### PRINTPREVIEW_GOTO_PAGENUM ###

PrintPreview Navigation Constants


### PRINTPREVIEW_PREV_PAGE ###

### PRINTPREVIEW_NEXT_PAGE ###

### PRINTPREVIEW_HOME ###

### PRINTPREVIEW_END ###
