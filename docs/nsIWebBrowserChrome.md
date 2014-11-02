---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIWebBrowserChrome.idl">Source file</a>
</div>

# nsIWebBrowserChrome #
  
nsIWebBrowserChrome corresponds to the top-level, outermost window  
containing an embedded Gecko web browser.  
  

## Methods ##

### setStatus(statusType, status) ###
  
Called when the status text in the chrome needs to be updated.  
@param statusType indicates what is setting the text  
@param status status string. null is an acceptable value meaning  
              no status.  
  

#### Parameters ####

<table>

<tr>
<td>statusType</td>
<td>indicates what is setting the text  
</td>
</tr>

<tr>
<td>status</td>
<td>status string. null is an acceptable value meaning  
              no status.  
</td>
</tr>

</table>

### destroyBrowserWindow() ###
  
Asks the implementer to destroy the window associated with this  
WebBrowser object.  
  

### sizeBrowserTo(aCX, aCY) ###
  
Tells the chrome to size itself such that the browser will be the   
specified size.  
@param aCX new width of the browser  
@param aCY new height of the browser  
  

#### Parameters ####

<table>

<tr>
<td>aCX</td>
<td>new width of the browser  
</td>
</tr>

<tr>
<td>aCY</td>
<td>new height of the browser  
</td>
</tr>

</table>

### showAsModal() ###
  
Shows the window as a modal window.  
@return (the function error code) the status value specified by  
        in exitModalEventLoop.  
  

#### Returns ####

<table>

<tr>
<td>(the function error code) the status value specified by  
        in exitModalEventLoop.  
</td>
</tr>

</table>

### isWindowModal() ###
  
Is the window modal (that is, currently executing a modal loop)?  
@return true if it's a modal window  
  

#### Returns ####

<table>

<tr>
<td>true if it's a modal window  
</td>
</tr>

</table>

### exitModalEventLoop(aStatus) ###
  
Exit a modal event loop if we're in one. The implementation  
should also exit out of the loop if the window is destroyed.  
@param aStatus - the result code to return from showAsModal  
  

#### Parameters ####

<table>

<tr>
<td>aStatus</td>
<td>- the result code to return from showAsModal  
</td>
</tr>

</table>

## Attributes ##

### webBrowser ###
  
The currently loaded WebBrowser.  The browser chrome may be  
told to set the WebBrowser object to a new object by setting this  
attribute.  In this case the implementer is responsible for taking the   
new WebBrowser object and doing any necessary initialization or setup   
as if it had created the WebBrowser itself.  This includes positioning  
setting up listeners etc.  
  

### chromeFlags ###
  
The chrome flags for this browser chrome. The implementation should  
reflect the value of this attribute by hiding or showing its chrome  
appropriately.  
  

## Constants ##

### STATUS_SCRIPT ###

### STATUS_LINK ###

### CHROME_DEFAULT ###
  
Definitions for the chrome flags  
  

### CHROME_WINDOW_BORDERS ###

### CHROME_WINDOW_CLOSE ###

### CHROME_WINDOW_RESIZE ###

### CHROME_MENUBAR ###

### CHROME_TOOLBAR ###

### CHROME_LOCATIONBAR ###

### CHROME_STATUSBAR ###

### CHROME_PERSONAL_TOOLBAR ###

### CHROME_SCROLLBARS ###

### CHROME_TITLEBAR ###

### CHROME_EXTRA ###

### CHROME_WITH_SIZE ###

### CHROME_WITH_POSITION ###

### CHROME_WINDOW_MIN ###

### CHROME_WINDOW_POPUP ###

### CHROME_PRIVATE_WINDOW ###

### CHROME_NON_PRIVATE_WINDOW ###

### CHROME_PRIVATE_LIFETIME ###

### CHROME_MODAL_CONTENT_WINDOW ###

### CHROME_REMOTE_WINDOW ###

### CHROME_MAC_SUPPRESS_ANIMATION ###

### CHROME_WINDOW_RAISED ###

### CHROME_WINDOW_LOWERED ###

### CHROME_CENTER_SCREEN ###

### CHROME_DEPENDENT ###

### CHROME_MODAL ###

### CHROME_OPENAS_DIALOG ###

### CHROME_OPENAS_CHROME ###

### CHROME_ALL ###
