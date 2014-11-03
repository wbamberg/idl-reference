---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIClipboardCommands.idl">Source file</a>
</div>

# nsIClipboardCommands #
<code>  
An interface for embedding clients who wish to interact with  
the system-wide OS clipboard. Mozilla does not use a private  
clipboard, instead it places its data directly onto the system   
clipboard. The webshell implements this interface.  
  
</code>
## Methods ##

### canCutSelection() ###
<code>  
Returns whether there is a selection and it is not read-only.  
  
@return <code>true</code> if the current selection can be cut,  
         <code>false</code> otherwise.  
  
</code>
#### Returns ####

<table>

<tr>
<td><code>true</code> if the current selection can be cut,  
         <code>false</code> otherwise.  
</td>
</tr>

</table>

### canCopySelection() ###
<code>  
Returns whether there is a selection and it is copyable.  
  
@return <code>true</code> if there is a selection,  
         <code>false</code> otherwise.  
  
</code>
#### Returns ####

<table>

<tr>
<td><code>true</code> if there is a selection,  
         <code>false</code> otherwise.  
</td>
</tr>

</table>

### canCopyLinkLocation() ###
<code>  
Returns whether we can copy a link location.  
  
@return <code>true</code> if a link is selected,  
          <code>false</code> otherwise.  
  
</code>
#### Returns ####

<table>

<tr>
<td><code>true</code> if a link is selected,  
          <code>false</code> otherwise.  
</td>
</tr>

</table>

### canCopyImageLocation() ###
<code>  
Returns whether we can copy an image location.  
  
@return <code>true</code> if an image is selected,  
<code>false</code> otherwise.  
  
</code>
#### Returns ####

<table>

<tr>
<td><code>true</code> if an image is selected,  
<code>false</code> otherwise.  
</td>
</tr>

</table>

### canCopyImageContents() ###
<code>  
Returns whether we can copy an image's contents.  
  
@return <code>true</code> if an image is selected,  
         <code>false</code> otherwise  
  
</code>
#### Returns ####

<table>

<tr>
<td><code>true</code> if an image is selected,  
         <code>false</code> otherwise  
</td>
</tr>

</table>

### canPaste() ###
<code>  
Returns whether the current contents of the clipboard can be  
pasted and if the current selection is not read-only.  
  
@return <code>true</code> there is data to paste on the clipboard  
         and the current selection is not read-only,  
         <code>false</code> otherwise  
  
</code>
#### Returns ####

<table>

<tr>
<td><code>true</code> there is data to paste on the clipboard  
         and the current selection is not read-only,  
         <code>false</code> otherwise  
</td>
</tr>

</table>

### cutSelection() ###
<code>  
Cut the current selection onto the clipboard.  
  
</code>
### copySelection() ###
<code>  
Copy the current selection onto the clipboard.  
  
</code>
### copyLinkLocation() ###
<code>  
Copy the link location of the current selection (e.g.,  
the |href| attribute of a selected |a| tag).  
  
</code>
### copyImageLocation() ###
<code>  
Copy the location of the selected image.  
  
</code>
### copyImageContents() ###
<code>  
Copy the contents of the selected image.  
  
</code>
### paste() ###
<code>  
Paste the contents of the clipboard into the current selection.  
  
</code>
### selectAll() ###
<code>  
Select the entire contents.  
  
</code>
### selectNone() ###
<code>  
Clear the current selection (if any). Insertion point ends up  
at beginning of current selection.  
  
</code>