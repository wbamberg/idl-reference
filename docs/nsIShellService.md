---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/mobile/android/components/build/nsIShellService.idl">Source file</a>
</div>

# nsIShellService #

## Methods ##

### switchTask() ###
  
This method displays a UI to switch to (or launch) a different task  
  

### createShortcut(aTitle, aURI, aIconData, aIntent) ###
  
This method creates a shortcut on a desktop or homescreen that opens in  
the our application.  
  
@param aTitle     the user-friendly name of the shortcut.  
@param aURI       the URI to open.  
@param aIconData  a base64-encoded data: URI representation of the shortcut's icon, as accepted by the favicon decoder.  
@param aIntent    obsolete and ignored, but remains for backward compatibility; pass an empty string  
  

#### Parameters ####

<table>

<tr>
<td>aTitle</td>
<td>the user-friendly name of the shortcut.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>the URI to open.  
</td>
</tr>

<tr>
<td>aIconData</td>
<td>a base64-encoded data: URI representation of the shortcut's icon, as accepted by the favicon decoder.  
</td>
</tr>

<tr>
<td>aIntent</td>
<td>obsolete and ignored, but remains for backward compatibility; pass an empty string  
</td>
</tr>

</table>
