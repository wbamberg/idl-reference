---
layout: default
---

# nsPIWindowWatcher #

## Methods ##

### addWindow(aWindow, aChrome) ###
 A window has been created. Add it to our list.  
@param aWindow the window to add  
@param aChrome the corresponding chrome window. The DOM window  
and chrome will be mapped together, and the corresponding  
chrome can be retrieved using the (not private)  
method getChromeForWindow. If null, any extant mapping  
will be cleared.  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>the window to add  
</td>
</tr>

<tr>
<td>aChrome</td>
<td>the corresponding chrome window. The DOM window  
and chrome will be mapped together, and the corresponding  
chrome can be retrieved using the (not private)  
method getChromeForWindow. If null, any extant mapping  
will be cleared.  
</td>
</tr>

</table>

### removeWindow(aWindow) ###
 A window has been closed. Remove it from our list.  
@param aWindow the window to remove  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>the window to remove  
</td>
</tr>

</table>

### openWindow2(aParent, aUrl, aName, aFeatures, aCalledFromScript, aDialog, aNavigate, aOpeningTab, aArgs) ###
 Like the public interface's open(), but can handle openDialog-style  
arguments and calls which shouldn't result in us navigating the window.  
  
@param aParent parent window, if any. Null if no parent.  If it is  
impossible to get to an nsIWebBrowserChrome from aParent, this  
method will effectively act as if aParent were null.  
@param aURL url to which to open the new window. Must already be  
escaped, if applicable. can be null.  
@param aName window name from JS window.open. can be null.  If a window  
with this name already exists, the openWindow call may just load  
aUrl in it (if aUrl is not null) and return it.  
@param aFeatures window features from JS window.open. can be null.  
@param aCalledFromScript true if we were called from script.  
@param aDialog use dialog defaults (see nsIDOMWindow::openDialog)  
@param aNavigate true if we should navigate the new window to the  
specified URL.  
@param aOpeningTab the nsITabParent that is opening the new window. The  
nsITabParent is a remote tab belonging to aParent. Can  
be nullptr if this window is not being opened from a tab.  
@param aArgs Window argument  
@return the new window  
  
@note This method may examine the JS context stack for purposes of  
determining the security context to use for the search for a given  
window named aName.  
@note This method should try to set the default charset for the new  
window to the default charset of the document in the calling window  
(which is determined based on the JS stack and the value of  
aParent).  This is not guaranteed, however.  
  

#### Parameters ####

<table>

<tr>
<td>aParent</td>
<td>parent window, if any. Null if no parent.  If it is  
impossible to get to an nsIWebBrowserChrome from aParent, this  
method will effectively act as if aParent were null.  
</td>
</tr>

<tr>
<td>aURL</td>
<td>url to which to open the new window. Must already be  
escaped, if applicable. can be null.  
</td>
</tr>

<tr>
<td>aName</td>
<td>window name from JS window.open. can be null.  If a window  
with this name already exists, the openWindow call may just load  
aUrl in it (if aUrl is not null) and return it.  
</td>
</tr>

<tr>
<td>aFeatures</td>
<td>window features from JS window.open. can be null.  
</td>
</tr>

<tr>
<td>aCalledFromScript</td>
<td>true if we were called from script.  
</td>
</tr>

<tr>
<td>aDialog</td>
<td>use dialog defaults (see nsIDOMWindow::openDialog)  
</td>
</tr>

<tr>
<td>aNavigate</td>
<td>true if we should navigate the new window to the  
specified URL.  
</td>
</tr>

<tr>
<td>aOpeningTab</td>
<td>the nsITabParent that is opening the new window. The  
nsITabParent is a remote tab belonging to aParent. Can  
be nullptr if this window is not being opened from a tab.  
</td>
</tr>

<tr>
<td>aArgs</td>
<td>Window argument  
</td>
</tr>

</table>

### findItemWithName(aName, aRequestor, aOriginalRequestor) ###
  
Find a named docshell tree item amongst all windows registered  
with the window watcher.  This may be a subframe in some window,  
for example.  
  
@param aName the name of the window.  Must not be null.  
@param aRequestor the tree item immediately making the request.  
       We should make sure to not recurse down into its findItemWithName  
       method.  
@param aOriginalRequestor the original treeitem that made the request.  
       Used for security checks.  
@return the tree item with aName as the name, or null if there  
        isn't one.  "Special" names, like _self, _top, etc, will be  
        treated specially only if aRequestor is null; in that case they  
        will be resolved relative to the first window the windowwatcher  
        knows about.  
@see findItemWithName methods on nsIDocShellTreeItem and  
     nsIDocShellTreeOwner  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>the name of the window.  Must not be null.  
</td>
</tr>

<tr>
<td>aRequestor</td>
<td>the tree item immediately making the request.  
       We should make sure to not recurse down into its findItemWithName  
       method.  
</td>
</tr>

<tr>
<td>aOriginalRequestor</td>
<td>the original treeitem that made the request.  
       Used for security checks.  
</td>
</tr>

</table>
