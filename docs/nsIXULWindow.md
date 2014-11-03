---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpfe/appshell/nsIXULWindow.idl">Source file</a>
</div>

# nsIXULWindow #

## Methods ##

### getContentShellById(ID) ###
<pre>  
The content shell specified by the supplied id.  
  
Note that this is a docshell tree item and therefore can not be assured of  
what object it is.  It could be an editor, a docshell, or a browser object.  
Or down the road any other object that supports being a DocShellTreeItem  
Query accordingly to determine the capabilities.  
  
</pre>
### addChildWindow(aChild) ###
<pre>  
Tell this window that it has picked up a child XUL window  
@param aChild the child window being added  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aChild</td>
<td>the child window being added  
</td>
</tr>

</table>

### removeChildWindow(aChild) ###
<pre>  
Tell this window that it has lost a child XUL window  
@param aChild the child window being removed  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aChild</td>
<td>the child window being removed  
</td>
</tr>

</table>

### center(aRelative, aScreen, aAlert) ###
<pre>  
Move the window to a centered position.  
@param aRelative If not null, the window relative to which the window is  
                 moved. See aScreen parameter for details.  
@param aScreen   PR_TRUE to center the window relative to the screen  
                 containing aRelative if aRelative is not null. If  
                 aRelative is null then relative to the screen of the  
                 opener window if it was initialized by passing it to  
                 nsWebShellWindow::Initialize. Failing that relative to  
                 the main screen.  
                 PR_FALSE to center it relative to aRelative itself.  
@param aAlert    PR_TRUE to move the window to an alert position,  
                 generally centered horizontally and 1/3 down from the top.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aRelative</td>
<td>If not null, the window relative to which the window is  
                 moved. See aScreen parameter for details.  
</td>
</tr>

<tr>
<td>aScreen</td>
<td>PR_TRUE to center the window relative to the screen  
                 containing aRelative if aRelative is not null. If  
                 aRelative is null then relative to the screen of the  
                 opener window if it was initialized by passing it to  
                 nsWebShellWindow::Initialize. Failing that relative to  
                 the main screen.  
                 PR_FALSE to center it relative to aRelative itself.  
</td>
</tr>

<tr>
<td>aAlert</td>
<td>PR_TRUE to move the window to an alert position,  
                 generally centered horizontally and 1/3 down from the top.  
</td>
</tr>

</table>

### showModal() ###
<pre>  
Shows the window as a modal window. That is, ensures that it is visible  
and runs a local event loop, exiting only once the window has been closed.  
  
</pre>
### assumeChromeFlagsAreFrozen() ###
<pre>  
Begin assuming |chromeFlags| don't change hereafter, and assert  
if they do change.  The state change is one-way and idempotent.  
  
</pre>
### createNewWindow(aChromeFlags, aOpeningTab) ###
<pre>  
Create a new window.  
@param aChromeFlags see nsIWebBrowserChrome  
@param aOpeningTab the TabParent that requested this new window be opened.  
                   Can be left null.  
@return the newly minted window  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aChromeFlags</td>
<td>see nsIWebBrowserChrome  
</td>
</tr>

<tr>
<td>aOpeningTab</td>
<td>the TabParent that requested this new window be opened.  
                   Can be left null.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the newly minted window  
</td>
</tr>

</table>

### applyChromeFlags() ###
<pre>  
Back-door method to force application of chrome flags at a particular  
time.  Do NOT call this unless you know what you're doing!  In particular,  
calling this when this XUL window doesn't yet have a document in its  
docshell could cause problems.  
  
</pre>
## Attributes ##

### docShell ###
<pre>  
The docshell owning the XUL for this window.  
  
</pre>
### intrinsicallySized ###
<pre>  
Indicates if this window is instrinsically sized.	  
  
</pre>
### primaryContentShell ###
<pre>  
The primary content shell.    
  
Note that this is a docshell tree item and therefore can not be assured of  
what object it is. It could be an editor, a docshell, or a browser object.  
Or down the road any other object that supports being a DocShellTreeItem  
Query accordingly to determine the capabilities.  
  
</pre>
### zLevel ###

### contextFlags ###
<pre>  
contextFlags are from nsIWindowCreator2  
  
</pre>
### chromeFlags ###

### XULBrowserWindow ###

## Constants ##

### lowestZ ###

### loweredZ ###

### normalZ ###

### raisedZ ###

### highestZ ###
