---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpfe/appshell/nsIAppShellService.idl">Source file</a>
</div>

# nsIAppShellService #

## Methods ##

### createTopLevelWindow(aParent, aUrl, aChromeMask, aInitialWidth, aInitialHeight, aOpeningTab) ###

### createWindowlessBrowser(aIsChrome) ###
<code>  
This is the constructor for creating an invisible DocShell.  
It is used to simulate DOM windows without an actual physical  
representation.  
@param aIsChrome Set true if you want to use it for chrome content.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aIsChrome</td>
<td>Set true if you want to use it for chrome content.  
</td>
</tr>

</table>

### createHiddenWindow() ###

### destroyHiddenWindow() ###

### getHiddenWindowAndJSContext(aHiddenDOMWindow, aJSContext) ###
<code>  
Return the (singleton) application hidden window as an nsIDOMWindow,  
and, the corresponding JavaScript context pointer.  This is useful  
if you'd like to subsequently call OpenDialog on the hidden window.  
@aHiddenDOMWindow the hidden window QI'd to type nsIDOMWindow  
@aJSContext       the corresponding JavaScript context  
  
</code>
### registerTopLevelWindow(aWindow) ###
<code>  
Add a window to the application's registry of windows.  These windows  
are generally shown in the Windows taskbar, and the application  
knows it can't quit until it's out of registered windows.  
@param aWindow the window to register  
@note When this method is successful, it fires the global notification  
      "xul-window-registered"  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>the window to register  
@note When this method is successful, it fires the global notification  
      "xul-window-registered"  
</td>
</tr>

</table>

### unregisterTopLevelWindow(aWindow) ###
<code>  
Remove a window from the application's window registry. Note that  
this method won't automatically attempt to quit the app when  
the last window is unregistered. For that, see Quit().  
@param aWindow you see the pattern  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>you see the pattern  
</td>
</tr>

</table>

### startEventLoopLagTracking() ###
<code>  
Start/stop tracking lags in the event loop.  
If the event loop gets unresponsive, a "event-loop-lag" notification  
is sent. Note that calling `startEventLoopLagTracking` when tracking  
is already enabled has no effect.  
@return true if tracking succeeded.  
  
</code>
#### Returns ####

<table>

<tr>
<td>true if tracking succeeded.  
</td>
</tr>

</table>

### stopEventLoopLagTracking() ###

## Attributes ##

### hiddenWindow ###
  
Return the (singleton) application hidden window, automatically created  
and maintained by this AppShellService.  
@param aResult the hidden window.  Do not unhide hidden window.  
               Do not taunt hidden window.  
  

### hiddenDOMWindow ###
  
Return the (singleton) application hidden window, automatically created  
and maintained by this AppShellService.  
@param aResult the hidden window.  Do not unhide hidden window.  
               Do not taunt hidden window.  
  

### hiddenPrivateWindow ###
  
Return the (singleton) application hidden private window, automatically  
created and maintained by this AppShellService.  This window is created  
in private browsing mode.  
@param aResult the hidden private window.  Do not unhide hidden window.  
               Do not taunt hidden window.  
  

### hiddenPrivateDOMWindow ###
  
Return the (singleton) application hidden private window, automatically  
created and maintained by this AppShellService.  This window is created  
in private browsing mode.  
@param aResult the hidden private window.  Do not unhide hidden window.  
               Do not taunt hidden window.  
  

### applicationProvidedHiddenWindow ###
  
Return true if the application hidden window was provided by the  
application. If it wasn't, the default hidden window was used. This will  
usually be false on all non-mac platforms.  
  

### hasHiddenPrivateWindow ###
  
Whether the hidden private window has been lazily created.  
  

## Constants ##

### SIZE_TO_CONTENT ###
  
Create a window, which will be initially invisible.  
@param aParent the parent window.  Can be null.  
@param aUrl the contents of the new window.  
@param aChromeMask chrome flags affecting the kind of OS border  
                   given to the window. see nsIBrowserWindow for  
                   bit/flag definitions.  
@param aCallbacks interface providing C++ hooks for window initialization  
                  before the window is made visible.  Can be null.  
                  Deprecated.  
@param aInitialWidth width, in pixels, of the window.  Width of window  
                     at creation.  Can be overridden by the "width"  
                     tag in the XUL.  Set to NS_SIZETOCONTENT to force  
                     the window to wrap to its contents.  
@param aInitialHeight like aInitialWidth, but subtly different.  
@param aOpeningTab The TabParent that requested that this window be opened.  
                   Can be left null.  
  
