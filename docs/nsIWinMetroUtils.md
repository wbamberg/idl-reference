---
layout: default
---

# nsIWinMetroUtils #
  
Integration with the "Metro"/"Modern" UI environment in Windows 8.  
  
Note: browser/metro/base/content/browser.js contains a stub  
implementation of this interface for non-Windows systems, for testing and  
development purposes only.  
  

## Methods ##

### showSettingsFlyout ###
  
Show the settings flyout  
  

### launchInDesktop ###
  
Launches the specified application with the specified arguments and  
switches to Desktop mode if in metro mode.  
  

### showNativeToast ###
  
Displays a native Windows 8 toast.  
  
@param aAppId  Application ID for current application.  
               If using Metro mode, it can be null string.  
  

### pinTileAsync ###
  
Secondary tiles are a Windows 8 specific feature for pinning new tiles  
to the start screen.   Tiles can later be activated whether the browser is  
already opened or not.   
  
  
Pins a new tile to the Windows 8 start screen.  
  
@param aTileID         An ID which can later be used to remove the tile  
                       ID must only contain valid filesystem characters  
@param aShortName      A short name for the tile  
@param aDiplayName     The name that will be displayed on the tile  
@param aActivationArgs The arguments to pass to the browser upon   
                       activation of the tile  
@param aTileImage An image for the normal tile view  
@param aSmallTileImage An image for the small tile view  
  

### unpinTileAsync ###
  
Unpins a tile from the Windows 8 start screen.  
  
@param aTileID An existing ID which was previously pinned  
               ID must only contain valid filesystem characters  
  

### isTilePinned ###
  
Determines if a tile is pinned to the Windows 8 start screen.  
  
@param aTileID An ID which may have been pinned with pinTileAsync  
               ID must only contain valid filesystem characters  
@return true if the tile is pinned  
  

### addSettingsPanelEntry ###
  
Settings panel links. addSettingsPanelEntry adds an entry to  
the settings flyout panel that the user can invoke.  
  
@param aChromePanelId panel id invoked via nsIBrowserDOMWindow's  
ShowPanel api. Example: 'prefs-container'  
@return a unique identifier that will be passed as "data" in the  
"metro-settings-entry-selected" notification when the entry is clicked  
  

### swapMouseButton ###
  
Change the value of the "switch primary and secondary buttons" preference.  
See the Windows SwapMouseButton API docs for details.  
Included here for use in automated tests (see bug 839460).  
  
@param aSwap true to enable the preference, false to disable it.  
@return original value of the preference.  
  

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
