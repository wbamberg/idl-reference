---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIStandaloneNativeMenu.idl">Source file</a>
</div>

# nsIStandaloneNativeMenu #
<code>  
Platform-independent interface to platform native menu objects.  
  
</code>
## Methods ##

### init(aDOMElement) ###
<code>  
Initialize the native menu using given XUL DOM element.  
  
@param aDOMElement A XUL DOM element of tag type |menu| or |menupopup|.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDOMElement</td>
<td>A XUL DOM element of tag type |menu| or |menupopup|.  
</td>
</tr>

</table>

### menuWillOpen() ###
<code>  
This method must be called before the menu is opened and displayed to the  
user. It allows the platform code to update the menu and also determine  
whether the menu should even be shown.  
  
@return true if the menu can be shown, false if it should not be shown  
  
</code>
#### Returns ####

<table>

<tr>
<td>true if the menu can be shown, false if it should not be shown  
</td>
</tr>

</table>

### activateNativeMenuItemAt(anIndexString) ###
<code>  
Activate the native menu item specified by |anIndexString|. This method  
is intended to be used by the test suite.  
  
@param anIndexString string containing a list of indices separated by  
       pipe ('|') characters  
  
</code>
#### Parameters ####

<table>

<tr>
<td>anIndexString</td>
<td>string containing a list of indices separated by  
       pipe ('|') characters  
</td>
</tr>

</table>

### forceUpdateNativeMenuAt(anIndexString) ###
<code>  
Force an update of the native menu item specified by |anIndexString|. This  
method is intended to be used by the test suite.  
  
@param anIndexString string containing a list of indices separated by  
       pipe ('|') characters  
  
</code>
#### Parameters ####

<table>

<tr>
<td>anIndexString</td>
<td>string containing a list of indices separated by  
       pipe ('|') characters  
</td>
</tr>

</table>

## Attributes ##

### nativeMenu ###
  
The native object representing the XUL menu that was passed to Init(). On  
Mac OS X, this will be a NSMenu pointer, which will be retained and  
autoreleased when the attribute is retrieved.  
  
