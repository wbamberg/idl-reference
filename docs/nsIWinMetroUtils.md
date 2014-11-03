---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIWinMetroUtils.idl">Source file</a>
</div>

# nsIWinMetroUtils #
<code>  
Integration with the "Metro"/"Modern" UI environment in Windows 8.  
  
Note: browser/metro/base/content/browser.js contains a stub  
implementation of this interface for non-Windows systems, for testing and  
development purposes only.  
  
</code>
## Methods ##

### showSettingsFlyout() ###
<code>  
Show the settings flyout  
  
</code>
### launchInDesktop(aPath, aArguments) ###
<code>  
Launches the specified application with the specified arguments and  
switches to Desktop mode if in metro mode.  
  
</code>
### showNativeToast(aTitle, aMessage, anImage, aCookie, aAppId) ###
<code>  
Displays a native Windows 8 toast.  
  
@param aAppId  Application ID for current application.  
               If using Metro mode, it can be null string.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aAppId</td>
<td>Application ID for current application.  
               If using Metro mode, it can be null string.  
</td>
</tr>

</table>

### pinTileAsync(aTileID, aShortName, aDisplayName, aActivationArgs, aTileImage, aSmallTileImage) ###
<code>  
Secondary tiles are a Windows 8 specific feature for pinning new tiles  
to the start screen.   Tiles can later be activated whether the browser is  
already opened or not.   
  
</code><code>  
Pins a new tile to the Windows 8 start screen.  
  
@param aTileID         An ID which can later be used to remove the tile  
                       ID must only contain valid filesystem characters  
@param aShortName      A short name for the tile  
@param aDiplayName     The name that will be displayed on the tile  
@param aActivationArgs The arguments to pass to the browser upon   
                       activation of the tile  
@param aTileImage An image for the normal tile view  
@param aSmallTileImage An image for the small tile view  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aTileID</td>
<td>An ID which can later be used to remove the tile  
                       ID must only contain valid filesystem characters  
</td>
</tr>

<tr>
<td>aShortName</td>
<td>A short name for the tile  
</td>
</tr>

<tr>
<td>aDiplayName</td>
<td>The name that will be displayed on the tile  
</td>
</tr>

<tr>
<td>aActivationArgs</td>
<td>The arguments to pass to the browser upon   
                       activation of the tile  
</td>
</tr>

<tr>
<td>aTileImage</td>
<td>An image for the normal tile view  
</td>
</tr>

<tr>
<td>aSmallTileImage</td>
<td>An image for the small tile view  
</td>
</tr>

</table>

### unpinTileAsync(aTileID) ###
<code>  
Unpins a tile from the Windows 8 start screen.  
  
@param aTileID An existing ID which was previously pinned  
               ID must only contain valid filesystem characters  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aTileID</td>
<td>An existing ID which was previously pinned  
               ID must only contain valid filesystem characters  
</td>
</tr>

</table>

### isTilePinned(aTileID) ###
<code>  
Determines if a tile is pinned to the Windows 8 start screen.  
  
@param aTileID An ID which may have been pinned with pinTileAsync  
               ID must only contain valid filesystem characters  
@return true if the tile is pinned  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aTileID</td>
<td>An ID which may have been pinned with pinTileAsync  
               ID must only contain valid filesystem characters  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the tile is pinned  
</td>
</tr>

</table>

### addSettingsPanelEntry(aLabel) ###
<code>  
Settings panel links. addSettingsPanelEntry adds an entry to  
the settings flyout panel that the user can invoke.  
  
@param aChromePanelId panel id invoked via nsIBrowserDOMWindow's  
ShowPanel api. Example: 'prefs-container'  
@return a unique identifier that will be passed as "data" in the  
"metro-settings-entry-selected" notification when the entry is clicked  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aChromePanelId</td>
<td>panel id invoked via nsIBrowserDOMWindow's  
ShowPanel api. Example: 'prefs-container'  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a unique identifier that will be passed as "data" in the  
"metro-settings-entry-selected" notification when the entry is clicked  
</td>
</tr>

</table>

### swapMouseButton(aSwap) ###
<code>  
Change the value of the "switch primary and secondary buttons" preference.  
See the Windows SwapMouseButton API docs for details.  
Included here for use in automated tests (see bug 839460).  
  
@param aSwap true to enable the preference, false to disable it.  
@return original value of the preference.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aSwap</td>
<td>true to enable the preference, false to disable it.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>original value of the preference.  
</td>
</tr>

</table>

## Attributes ##

### supported ###
  
Determine if the current device has the hardware capabilities to run  
in metro mode.  
  

### immersive ###
  
Determine if the current browser is running in the metro immersive  
environment.  
  

### activationURI ###
  
Determine the activation URI  
  

### previousExecutionState ###
  
Determine the previous execution state. The possible values of this  
attribute are exactly those values in the  
Windows::ApplicationModel::Activation enumeration.  
  

### updatePending ###
  
Helper for our restart logic up in the about flyout. We set this  
right before we restart for an update so that MetroAppShell can  
communicate this to the ceh.  
  

### foreground ###

### keyboardVisible ###
  
Soft keyboard attributes. Used in unison with shown/hidden observer  
events sent via FrameworkView.  
  
keyboardVisible - returns true if the soft keyboard is currently  
displayed, false otherwise.  
keyboardX, keyboardY, keyboardWidth, keyboardHeight - occlude rect  
of the keyboard when displayed in device independent pixels.  
  

### keyboardX ###

### keyboardY ###

### keyboardWidth ###

### keyboardHeight ###
