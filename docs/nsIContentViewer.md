---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIContentViewer.idl">Source file</a>
</div>

# nsIContentViewer #

## Methods ##

### init(aParentWidget, aBounds) ###

### loadStart(aDoc) ###

### loadComplete(aStatus) ###

### permitUnload(aCallerClosesWindow) ###
<pre>  
Checks if the document wants to prevent unloading by firing beforeunload on  
the document, and if it does, prompts the user. The result is returned.  
  
@param aCallerClosesWindow indicates that the current caller will close the  
       window. If the method returns true, all subsequent calls will be  
       ignored.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aCallerClosesWindow</td>
<td>indicates that the current caller will close the  
       window. If the method returns true, all subsequent calls will be  
       ignored.  
</td>
</tr>

</table>

### permitUnloadInternal(aCallerClosesWindow, aShouldPrompt) ###
<pre>  
As above, but this passes around the aShouldPrompt argument to keep  
track of whether the user has responded to a prompt.  
Used internally by the scriptable version to ensure we only prompt once.  
  
</pre>
### resetCloseWindow() ###
<pre>  
Works in tandem with permitUnload, if the caller decides not to close the  
window it indicated it will, it is the caller's responsibility to reset  
that with this method.  
  
@Note this method is only meant to be called on documents for which the  
 caller has indicated that it will close the window. If that is not the case  
 the behavior of this method is undefined.  
  
</pre>
### pageHide(isUnload) ###

### close(historyEntry) ###
<pre>  
All users of a content viewer are responsible for calling both  
close() and destroy(), in that order.   
  
close() should be called when the load of a new page for the next  
content viewer begins, and destroy() should be called when the next  
content viewer replaces this one.  
  
|historyEntry| sets the session history entry for the content viewer.  If  
this is null, then Destroy() will be called on the document by close().  
If it is non-null, the document will not be destroyed, and the following  
actions will happen when destroy() is called (*):  
 - Sanitize() will be called on the viewer's document  
 - The content viewer will set the contentViewer property on the  
   history entry, and release its reference (ownership reversal).  
 - hide() will be called, and no further destruction will happen.  
  
 (*) unless the document is currently being printed, in which case  
     it will never be saved in session history.  
  
  
</pre>
### destroy() ###

### stop() ###

### getDocument() ###
<pre>  
Returns DOMDocument as nsIDocument and without addrefing.  
  
</pre>
### getBounds(aBounds) ###

### setBounds(aBounds) ###

### move(aX, aY) ###

### show() ###

### hide() ###

### requestWindowClose() ###

### open(aState, aSHEntry) ###
<pre>  
Attach the content viewer to its DOM window and docshell.  
@param aState A state object that might be useful in attaching the DOM  
              window.  
@param aSHEntry The history entry that the content viewer was stored in.  
                The entry must have the docshells for all of the child  
                documents stored in its child shell list.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aState</td>
<td>A state object that might be useful in attaching the DOM  
              window.  
</td>
</tr>

<tr>
<td>aSHEntry</td>
<td>The history entry that the content viewer was stored in.  
                The entry must have the docshells for all of the child  
                documents stored in its child shell list.  
</td>
</tr>

</table>

### clearHistoryEntry() ###
<pre>  
Clears the current history entry.  This is used if we need to clear out  
the saved presentation state.  
  
</pre>
### setPageMode(aPageMode, aPrintSettings) ###
<pre>  
Change the layout to view the document with page layout (like print preview), but  
dynamic and editable (like Galley layout).  
  
</pre>
### setDocumentInternal(aDocument, aForceReuseInnerWindow) ###

### findContainerView() ###
<pre>  
Find the view to use as the container view for MakeWindow. Returns  
null if this will be the root of a view manager hierarchy. In that  
case, if mParentWidget is null then this document should not even  
be displayed.  
  
</pre>
### setNavigationTiming(aTiming) ###
<pre>  
Set collector for navigation timing data (load, unload events).  
  
</pre>
### scrollToNode(node) ###

### getContentSize(width, height) ###
<pre>  
Requests the size of the content to the container.  
  
</pre>
### appendSubtree(array) ###
<pre>  
Append |this| and all of its descendants to the given array,  
in depth-first pre-order traversal.  
  
</pre>
### changeMaxLineBoxWidth(maxLineBoxWidth) ###
<pre>  
Set the maximum line width for the document.  
NOTE: This will generate a reflow!  
  
@param maxLineWidth The maximum width of any line boxes on the page,  
       in CSS pixels.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>maxLineWidth</td>
<td>The maximum width of any line boxes on the page,  
       in CSS pixels.  
</td>
</tr>

</table>

### pausePainting() ###
<pre>  
Instruct the refresh driver to discontinue painting until further  
notice.  
  
</pre>
### resumePainting() ###
<pre>  
Instruct the refresh driver to resume painting after a previous call to  
pausePainting().  
  
</pre>
### emulateMedium(aMediaType) ###

### stopEmulatingMedium() ###

## Attributes ##

### container ###

### inPermitUnload ###
<pre>  
Exposes whether we're blocked in a call to permitUnload.  
  
</pre>
### beforeUnloadFiring ###
<pre>  
Exposes whether we're in the process of firing the beforeunload event.  
In this case, the corresponding docshell will not allow navigation.  
  
</pre>
### DOMDocument ###

### previousViewer ###
<pre>  
The previous content viewer, which has been |close|d but not  
|destroy|ed.  
  
</pre>
### sticky ###

### historyEntry ###
<pre>  
Get the history entry that this viewer will save itself into when  
destroyed.  Can return null  
  
</pre>
### isTabModalPromptAllowed ###
<pre>  
Indicates when we're in a state where content shouldn't be allowed to  
trigger a tab-modal prompt (as opposed to a window-modal prompt) because  
we're part way through some operation (eg beforeunload) that shouldn't be  
rentrant if the user closes the tab while the prompt is showing.  
See bug 613800.  
  
</pre>
### isHidden ###
<pre>  
Returns whether this content viewer is in a hidden state.  
  
@note Only Gecko internal code should set the attribute!  
  
</pre>
### presShell ###

### presContext ###

### textZoom ###
<pre> The amount by which to scale all text. Default is 1.0. */  
</pre>
### fullZoom ###
<pre> The amount by which to scale all lengths. Default is 1.0. */  
</pre>
### authorStyleDisabled ###
<pre> Disable entire author style level (including HTML presentation hints) */  
</pre>
### forceCharacterSet ###
<pre>  
XXX comm-central only: bug 829543. Not the Character Encoding menu in   
browser!  
  
</pre>
### hintCharacterSet ###
<pre>  
XXX comm-central only: bug 829543.  
  
</pre>
### hintCharacterSetSource ###
<pre>  
XXX comm-central only: bug 829543.  
  
</pre>
### minFontSize ###
<pre> The minimum font size  */  
</pre>