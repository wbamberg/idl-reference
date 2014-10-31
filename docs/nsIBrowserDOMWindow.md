---
layout: default
---

# nsIBrowserDOMWindow #
  
The C++ source has access to the browser script source through  
nsIBrowserDOMWindow. It is intended to be attached to the chrome DOMWindow  
of a toplevel browser window (a XUL window). A DOMWindow that does not  
happen to be a browser chrome window will simply have no access to any such  
interface.  
  

## Methods ##

### openURI(aURI, aOpener, aWhere, aContext) ###
  
Load a URI  
  
@param aURI the URI to open. null is allowed.  If null is passed in, no  
            load will be done, though the window the load would have  
            happened in will be returned.  
@param aWhere see possible values described above.  
@param aOpener window requesting the open (can be null).  
@param aContext the context in which the URI is being opened. This  
                is used only when aWhere == OPEN_DEFAULTWINDOW.  
@return the window into which the URI was opened.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the URI to open. null is allowed.  If null is passed in, no  
            load will be done, though the window the load would have  
            happened in will be returned.  
</td>
</tr>

<tr>
<td>aWhere</td>
<td>see possible values described above.  
</td>
</tr>

<tr>
<td>aOpener</td>
<td>window requesting the open (can be null).  
</td>
</tr>

<tr>
<td>aContext</td>
<td>the context in which the URI is being opened. This  
                is used only when aWhere == OPEN_DEFAULTWINDOW.  
</td>
</tr>

</table>

### openURIInFrame(aURI, aOpener, aWhere, aContext) ###
  
As above, but return the nsIFrameLoaderOwner for the new window.  
// XXXbz is this the right API? Do we really need the opener here?  
// See bug 537428  
  

### isTabContentWindow(aWindow) ###
  
@param  aWindow the window to test.  
@return whether the window is the main content window for any  
        currently open tab in this toplevel browser window.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aWindow the window to test.  
</td>
</tr>

</table>

## Constants ##

### OPEN_DEFAULTWINDOW ###
  
Values for openURI's aWhere parameter.  
  
  
Do whatever the default is based on application state, user preferences,  
and the value of the aContext parameter to openURI.  
  

### OPEN_CURRENTWINDOW ###
  
Open in the "current window".  If aOpener is provided, this should be the  
top window in aOpener's window hierarchy, but exact behavior is  
application-dependent.  If aOpener is not provided, it's up to the  
application to decide what constitutes a "current window".  
  

### OPEN_NEWWINDOW ###
  
Open in a new window.  
  

### OPEN_NEWTAB ###
  
Open in a new content tab in the toplevel browser window corresponding to  
this nsIBrowserDOMWindow.  
  

### OPEN_SWITCHTAB ###
  
Open in an existing content tab based on the URI. If a match can't be  
found, revert to OPEN_NEWTAB behavior.  
  

### OPEN_EXTERNAL ###
  
Values for openURI's aContext parameter.  These affect the behavior of  
OPEN_DEFAULTWINDOW.  
  
  
external link (load request from another application, xremote, etc).  
  

### OPEN_NEW ###
  
internal open new window  
  
