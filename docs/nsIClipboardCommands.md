---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIClipboardCommands.idl">Source file</a>
</div>

# nsIClipboardCommands #
<pre>  
An interface for embedding clients who wish to interact with  
the system-wide OS clipboard. Mozilla does not use a private  
clipboard, instead it places its data directly onto the system   
clipboard. The webshell implements this interface.  
  
</pre>
## Methods ##

### canCutSelection() ###
<pre>  
Returns whether there is a selection and it is not read-only.  
  
@return <code>true</code> if the current selection can be cut,  
         <code>false</code> otherwise.  
  
</pre>
#### Returns ####

<table>

<tr>
<td><code>true</code> if the current selection can be cut,  
         <code>false</code> otherwise.  
</td>
</tr>

</table>

### canCopySelection() ###
<pre>  
Returns whether there is a selection and it is copyable.  
  
@return <code>true</code> if there is a selection,  
         <code>false</code> otherwise.  
  
</pre>
#### Returns ####

<table>

<tr>
<td><code>true</code> if there is a selection,  
         <code>false</code> otherwise.  
</td>
</tr>

</table>

### canCopyLinkLocation() ###
<pre>  
Returns whether we can copy a link location.  
  
@return <code>true</code> if a link is selected,  
          <code>false</code> otherwise.  
  
</pre>
#### Returns ####

<table>

<tr>
<td><code>true</code> if a link is selected,  
          <code>false</code> otherwise.  
</td>
</tr>

</table>

### canCopyImageLocation() ###
<pre>  
Returns whether we can copy an image location.  
  
@return <code>true</code> if an image is selected,  
<code>false</code> otherwise.  
  
</pre>
#### Returns ####

<table>

<tr>
<td><code>true</code> if an image is selected,  
<code>false</code> otherwise.  
</td>
</tr>

</table>

### canCopyImageContents() ###
<pre>  
Returns whether we can copy an image's contents.  
  
@return <code>true</code> if an image is selected,  
         <code>false</code> otherwise  
  
</pre>
#### Returns ####

<table>

<tr>
<td><code>true</code> if an image is selected,  
         <code>false</code> otherwise  
</td>
</tr>

</table>

### canPaste() ###
<pre>  
Returns whether the current contents of the clipboard can be  
pasted and if the current selection is not read-only.  
  
@return <code>true</code> there is data to paste on the clipboard  
         and the current selection is not read-only,  
         <code>false</code> otherwise  
  
</pre>
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
<pre>  
Cut the current selection onto the clipboard.  
  
</pre>
### copySelection() ###
<pre>  
Copy the current selection onto the clipboard.  
  
</pre>
### copyLinkLocation() ###
<pre>  
Copy the link location of the current selection (e.g.,  
the |href| attribute of a selected |a| tag).  
  
</pre>
### copyImageLocation() ###
<pre>  
Copy the location of the selected image.  
  
</pre>
### copyImageContents() ###
<pre>  
Copy the contents of the selected image.  
  
</pre>
### paste() ###
<pre>  
Paste the contents of the clipboard into the current selection.  
  
</pre>
### selectAll() ###
<pre>  
Select the entire contents.  
  
</pre>
### selectNone() ###
<pre>  
Clear the current selection (if any). Insertion point ends up  
at beginning of current selection.  
  
</pre>