---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/mobile/android/components/SessionStore.idl">Source file</a>
</div>
# nsISessionStore #
  
nsISessionStore keeps track of the current browsing state.  
  
The nsISessionStore API operates mostly on browser windows and the browser  
tabs contained in them.  
  

## Methods ##

### getBrowserState() ###
  
Get the current browsing state.  
@returns a JSON string representing the session state.  
  

#### Returns ####

<table>

<tr>
<td>a JSON string representing the session state.  
</td>
</tr>

</table>

### getClosedTabCount(aWindow) ###
  
Get the number of restore-able tabs for a browser window  
  

### getClosedTabs(aWindow) ###
  
Get closed tab data  
  
@param aWindow is the browser window for which to get closed tab data  
@returns a JS array of closed tabs.  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>is the browser window for which to get closed tab data  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a JS array of closed tabs.  
</td>
</tr>

</table>

### undoCloseTab(aWindow, aCloseTabData) ###
  
@param aWindow is the browser window to reopen a closed tab in.  
@param aCloseTabData is the data of the tab to be restored.  
@returns a reference to the reopened tab.  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>is the browser window to reopen a closed tab in.  
</td>
</tr>

<tr>
<td>aCloseTabData</td>
<td>is the data of the tab to be restored.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a reference to the reopened tab.  
</td>
</tr>

</table>

### forgetClosedTab(aWindow, aIndex) ###
  
@param aWindow is the browser window associated with the closed tab.  
@param aIndex  is the index of the closed tab to be removed (FIFO ordered).  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>is the browser window associated with the closed tab.  
</td>
</tr>

<tr>
<td>aIndex</td>
<td>is the index of the closed tab to be removed (FIFO ordered).  
</td>
</tr>

</table>

### getTabValue(aTab, aKey) ###
  
@param aTab is the browser tab to get the value for.  
@param aKey is the value's name.  
  
@returns A string value or an empty string if none is set.  
  

#### Parameters ####

<table>

<tr>
<td>aTab</td>
<td>is the browser tab to get the value for.  
</td>
</tr>

<tr>
<td>aKey</td>
<td>is the value's name.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A string value or an empty string if none is set.  
</td>
</tr>

</table>

### setTabValue(aTab, aKey, aStringValue) ###
  
@param aTab         is the browser tab to set the value for.  
@param aKey         is the value's name.  
@param aStringValue is the value itself (use JSON.stringify/parse before setting JS objects).  
  

#### Parameters ####

<table>

<tr>
<td>aTab</td>
<td>is the browser tab to set the value for.  
</td>
</tr>

<tr>
<td>aKey</td>
<td>is the value's name.  
</td>
</tr>

<tr>
<td>aStringValue</td>
<td>is the value itself (use JSON.stringify/parse before setting JS objects).  
</td>
</tr>

</table>

### deleteTabValue(aTab, aKey) ###
  
@param aTab is the browser tab to get the value for.  
@param aKey is the value's name.  
  

#### Parameters ####

<table>

<tr>
<td>aTab</td>
<td>is the browser tab to get the value for.  
</td>
</tr>

<tr>
<td>aKey</td>
<td>is the value's name.  
</td>
</tr>

</table>

### restoreLastSession(aSessionString) ###
  
Restores the previous browser session using a fast, lightweight strategy  
@param aSessionString The session string to restore from. If null, the  
                      backup session file is read from.  
  

#### Parameters ####

<table>

<tr>
<td>aSessionString</td>
<td>The session string to restore from. If null, the  
                      backup session file is read from.  
</td>
</tr>

</table>

### removeWindow(aWindow) ###
  
Removes a window from the current session history. Data from this window  
won't be saved when its closed.  
@param aWindow The window to remove  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>The window to remove  
</td>
</tr>

</table>
