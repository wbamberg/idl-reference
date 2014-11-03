---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIDocShell.idl">Source file</a>
</div>

# nsIDocShell #

## Methods ##

### loadURI(uri, loadInfo, aLoadFlags, firstParty) ###
<code>  
Loads a given URI.  This will give priority to loading the requested URI  
in the object implementing	this interface.  If it can't be loaded here  
however, the URL dispatcher will go through its normal process of content  
loading.  
  
@param uri        - The URI to load.  
@param loadInfo   - This is the extended load info for this load.  This  
                    most often will be null, but if you need to do   
                    additional setup for this load you can get a loadInfo  
                    object by calling createLoadInfo.  Once you have this  
                    object you can set the needed properties on it and  
                    then pass it to loadURI.  
@param aLoadFlags - Flags to modify load behaviour. Flags are defined in  
                    nsIWebNavigation.  Note that using flags outside  
                    LOAD_FLAGS_MASK is only allowed if passing in a  
                    non-null loadInfo.  And even some of those might not  
                    be allowed.  Use at your own risk.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>- The URI to load.  
</td>
</tr>

<tr>
<td>loadInfo</td>
<td>- This is the extended load info for this load.  This  
                    most often will be null, but if you need to do   
                    additional setup for this load you can get a loadInfo  
                    object by calling createLoadInfo.  Once you have this  
                    object you can set the needed properties on it and  
                    then pass it to loadURI.  
</td>
</tr>

<tr>
<td>aLoadFlags</td>
<td>- Flags to modify load behaviour. Flags are defined in  
                    nsIWebNavigation.  Note that using flags outside  
                    LOAD_FLAGS_MASK is only allowed if passing in a  
                    non-null loadInfo.  And even some of those might not  
                    be allowed.  Use at your own risk.  
</td>
</tr>

</table>

### loadStream(aStream, aURI, aContentType, aContentCharset, aLoadInfo) ###
<code>  
Loads a given stream. This will give priority to loading the requested  
stream in the object implementing this interface. If it can't be loaded  
here however, the URL dispatched will go through its normal process of  
content loading.  
  
@param aStream         - The input stream that provides access to the data  
                         to be loaded.  This must be a blocking, threadsafe  
                         stream implementation.  
@param aURI            - The URI representing the stream, or null.  
@param aContentType    - The type (MIME) of data being loaded (empty if unknown).  
@param aContentCharset - The charset of the data being loaded (empty if unknown).  
@param aLoadInfo       - This is the extended load info for this load.  This  
                         most often will be null, but if you need to do   
                         additional setup for this load you can get a  
                         loadInfo object by calling createLoadInfo.  Once  
                         you have this object you can set the needed   
                         properties on it and then pass it to loadStream.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>- The input stream that provides access to the data  
                         to be loaded.  This must be a blocking, threadsafe  
                         stream implementation.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>- The URI representing the stream, or null.  
</td>
</tr>

<tr>
<td>aContentType</td>
<td>- The type (MIME) of data being loaded (empty if unknown).  
</td>
</tr>

<tr>
<td>aContentCharset</td>
<td>- The charset of the data being loaded (empty if unknown).  
</td>
</tr>

<tr>
<td>aLoadInfo</td>
<td>- This is the extended load info for this load.  This  
                         most often will be null, but if you need to do   
                         additional setup for this load you can get a  
                         loadInfo object by calling createLoadInfo.  Once  
                         you have this object you can set the needed   
                         properties on it and then pass it to loadStream.  
</td>
</tr>

</table>

### internalLoad(aURI, aReferrer, aOwner, aFlags, aWindowTarget, aTypeHint, aFileName, aPostDataStream, aHeadersStream, aLoadFlags, aSHEntry, firstParty, aSrcdoc, aSourceDocShell, aBaseURI, aDocShell, aRequest) ###
<code>  
Loads the given URI.  This method is identical to loadURI(...) except  
that its parameter list is broken out instead of being packaged inside  
of an nsIDocShellLoadInfo object...  
  
@param aURI            - The URI to load.  
@param aReferrer       - Referring URI  
@param aOwner          - Owner (security principal)   
@param aInheritOwner   - Flag indicating whether the owner of the current  
                         document should be inherited if aOwner is null.  
@param aStopActiveDoc  - Flag indicating whether loading the current  
                         document should be stopped.  
@param aWindowTarget   - Window target for the load.  
@param aTypeHint       - A hint as to the content-type of the resulting  
                         data.  May be null or empty if no hint.  
@param aFileName       - Non-null when the link should be downloaded as  
the given filename.  
@param aPostDataStream - Post data stream (if POSTing)  
@param aHeadersStream  - Stream containing "extra" request headers...  
@param aLoadFlags      - Flags to modify load behaviour. Flags are defined  
                         in nsIWebNavigation.  
@param aSHEntry        - Active Session History entry (if loading from SH)  
@param aSrcdoc           When INTERNAL_LOAD_FLAGS_IS_SRCDOC is set, the  
                         contents of this parameter will be loaded instead  
                         of aURI.  
@param aSourceDocShell - The source browsing context for the navigation.  
@param aBaseURI        - The base URI to be used for the load.  Set in  
                         srcdoc loads as it cannot otherwise be inferred  
                         in certain situations such as view-source.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>- The URI to load.  
</td>
</tr>

<tr>
<td>aReferrer</td>
<td>- Referring URI  
</td>
</tr>

<tr>
<td>aOwner</td>
<td>- Owner (security principal)   
</td>
</tr>

<tr>
<td>aInheritOwner</td>
<td>- Flag indicating whether the owner of the current  
                         document should be inherited if aOwner is null.  
</td>
</tr>

<tr>
<td>aStopActiveDoc</td>
<td>- Flag indicating whether loading the current  
                         document should be stopped.  
</td>
</tr>

<tr>
<td>aWindowTarget</td>
<td>- Window target for the load.  
</td>
</tr>

<tr>
<td>aTypeHint</td>
<td>- A hint as to the content-type of the resulting  
                         data.  May be null or empty if no hint.  
</td>
</tr>

<tr>
<td>aFileName</td>
<td>- Non-null when the link should be downloaded as  
the given filename.  
</td>
</tr>

<tr>
<td>aPostDataStream</td>
<td>- Post data stream (if POSTing)  
</td>
</tr>

<tr>
<td>aHeadersStream</td>
<td>- Stream containing "extra" request headers...  
</td>
</tr>

<tr>
<td>aLoadFlags</td>
<td>- Flags to modify load behaviour. Flags are defined  
                         in nsIWebNavigation.  
</td>
</tr>

<tr>
<td>aSHEntry</td>
<td>- Active Session History entry (if loading from SH)  
</td>
</tr>

<tr>
<td>aSrcdoc</td>
<td>When INTERNAL_LOAD_FLAGS_IS_SRCDOC is set, the  
                         contents of this parameter will be loaded instead  
                         of aURI.  
</td>
</tr>

<tr>
<td>aSourceDocShell</td>
<td>- The source browsing context for the navigation.  
</td>
</tr>

<tr>
<td>aBaseURI</td>
<td>- The base URI to be used for the load.  Set in  
                         srcdoc loads as it cannot otherwise be inferred  
                         in certain situations such as view-source.  
</td>
</tr>

</table>

### addState(aData, aTitle, aURL, aReplace) ###
<code>  
Do either a history.pushState() or history.replaceState() operation,  
depending on the value of aReplace.  
  
</code>
### createLoadInfo(loadInfo) ###
<code>  
Creates a DocShellLoadInfo object that you can manipulate and then pass  
to loadURI.  
  
</code>
### prepareForNewContentModel() ###
<code>  
Reset state to a new content model within the current document and the document  
viewer.  Called by the document before initiating an out of band document.write().  
  
</code>
### setCurrentURI(aURI) ###
<code>  
For editors and suchlike who wish to change the URI associated with the  
document. Note if you want to get the current URI, use the read-only  
property on nsIWebNavigation.  
  
</code>
### firePageHideNotification(isUnload) ###
<code>  
Notify the associated content viewer and all child docshells that they are  
about to be hidden.  If |isUnload| is true, then the document is being  
unloaded as well.  
  
@param isUnload if true, fire the unload event in addition to the pagehide  
                event.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>isUnload</td>
<td>if true, fire the unload event in addition to the pagehide  
                event.  
</td>
</tr>

</table>

### GetPresShell() ###
<code>  
Presentation shell for the currently loaded document.  This may be null.  
  
</code>
### getDocShellEnumerator(aItemType, aDirection) ###

### tabToTreeOwner(forward, tookFocus) ###

### isBeingDestroyed() ###

### suspendRefreshURIs() ###
<code>  
Cancel the XPCOM timers for each meta-refresh URI in this docshell,  
and this docshell's children, recursively. The meta-refresh timers can be  
restarted using resumeRefreshURIs().  If the timers are already suspended,  
this has no effect.  
  
</code>
### resumeRefreshURIs() ###
<code>  
Restart the XPCOM timers for each meta-refresh URI in this docshell,  
and this docshell's children, recursively.  If the timers are already  
running, this has no effect.  
  
</code>
### beginRestore(viewer, top) ###
<code>  
Begin firing WebProgressListener notifications for restoring a page  
presentation. |viewer| is the content viewer whose document we are  
starting to load.  If null, it defaults to the docshell's current content  
viewer, creating one if necessary.  |top| should be true for the toplevel  
docshell that is being restored; it will be set to false when this method  
is called for child docshells.  This method will post an event to  
complete the simulated load after returning to the event loop.  
  
</code>
### finishRestore() ###
<code>  
Finish firing WebProgressListener notifications and DOM events for  
restoring a page presentation.  This should only be called via  
beginRestore().  
  
</code>
### displayLoadError(aError, aURI, aURL, aFailedChannel) ###
<code>  
Display a load error in a frame while keeping that frame's currentURI  
pointing correctly to the page where the error ocurred, rather than to  
the error document page. You must provide either the aURI or aURL parameter.  
  
@param  aError         The error code to be displayed  
@param  aURI           nsIURI of the page where the error happened  
@param  aURL           wstring of the page where the error happened  
@param  aFailedChannel The channel related to this error  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aError</td>
<td>The error code to be displayed  
</td>
</tr>

<tr>
<td>aURI</td>
<td>nsIURI of the page where the error happened  
</td>
</tr>

<tr>
<td>aURL</td>
<td>wstring of the page where the error happened  
</td>
</tr>

<tr>
<td>aFailedChannel</td>
<td>The channel related to this error  
</td>
</tr>

</table>

### historyPurged(numEntries) ###
<code>  
Notification that entries have been removed from the beginning of a  
nsSHistory which has this as its rootDocShell.  
  
@param numEntries - The number of entries removed  
  
</code>
#### Parameters ####

<table>

<tr>
<td>numEntries</td>
<td>- The number of entries removed  
</td>
</tr>

</table>

### getSessionStorageForPrincipal(principal, documentURI, create) ###

### addSessionStorage(principal, storage) ###

### setChildOffset(offset) ###
<code>  
Set the offset of this child in its container.  
  
</code>
### DetachEditorFromWindow() ###
<code>  
Disconnects this docshell's editor from its window, and stores the  
editor data in the open document's session history entry.  This  
should be called only during page transitions.  
  
</code>
### createAboutBlankContentViewer(aPrincipal) ###
<code>  
Create a new about:blank document and content viewer.  
@param aPrincipal the principal to use for the new document.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aPrincipal</td>
<td>the principal to use for the new document.  
</td>
</tr>

</table>

### gatherCharsetMenuTelemetry() ###
<code>  
Called when the user chose an encoding override from the character  
encoding menu. Separate from the setter for the charset property to avoid  
extensions adding noise to the data.  
  
</code>
### setParentCharset(parentCharset, parentCharsetSource, parentCharsetPrincipal) ###
<code>  
In a child docshell, this is the charset of the parent docshell  
  
</code>
### getParentCharset(parentCharset, parentCharsetSource, parentCharsetPrincipal) ###

### now() ###
<code>  
Return a DOMHighResTimeStamp representing the number of  
milliseconds from an arbitrary point in time.  The reference  
point is shared by all DocShells and is also used by timestamps  
on markers.  
  
</code>
### popProfileTimelineMarkers() ###
<code>  
Returns and flushes the profile timeline markers gathered by the docShell  
  
</code>
### addWeakPrivacyTransitionObserver(obs) ###
<code>  
Add an observer to the list of parties to be notified when this docshell's  
private browsing status is changed. |obs| must support weak references.  
  
</code>
### addWeakReflowObserver(obs) ###
<code>  
Add an observer to the list of parties to be notified when reflows are  
occurring. |obs| must support weak references.  
  
</code>
### removeWeakReflowObserver(obs) ###
<code>  
Remove an observer from the list of parties to be notified about reflows.  
  
</code>
### notifyReflowObservers(interruptible, start, end) ###
<code>  
Notify all attached observers that a reflow has just occurred.  
  
@param interruptible if true, the reflow was interruptible.  
@param start         timestamp when reflow started, in milliseconds since  
                     navigationStart (accurate to 1/1000 of a ms)  
@param end           timestamp when reflow ended, in milliseconds since  
                     navigationStart (accurate to 1/1000 of a ms)  
  
</code>
#### Parameters ####

<table>

<tr>
<td>interruptible</td>
<td>if true, the reflow was interruptible.  
</td>
</tr>

<tr>
<td>start</td>
<td>timestamp when reflow started, in milliseconds since  
                     navigationStart (accurate to 1/1000 of a ms)  
</td>
</tr>

<tr>
<td>end</td>
<td>timestamp when reflow ended, in milliseconds since  
                     navigationStart (accurate to 1/1000 of a ms)  
</td>
</tr>

</table>

### addWeakScrollObserver(obs) ###
<code>  
Add an observer to the list of parties to be notified when scroll position  
of some elements is changed.  
  
</code>
### removeWeakScrollObserver(obs) ###
<code>  
Add an observer to the list of parties to be notified when scroll position  
of some elements is changed.  
  
</code>
### notifyScrollObservers() ###
<code>  
Notify all attached observers that the scroll position of some element  
has changed.  
  
</code>
### setIsApp(ownAppId) ###
<code>  
Indicate that this docshell corresponds to an app with the given app id.  
  
You may pass NO_APP_ID or UNKNOWN_APP_ID for containingAppId.  If you  
pass NO_APP_ID, then this docshell will return NO_APP_ID for appId.  If  
you pass UNKNOWN_APP_ID, then this docshell will search its hiearchy for  
an app frame and use that frame's appId.  
  
You can call this method more than once, but there's no guarantee that  
other components will update their view of the world if you change a  
docshell's app id, so tread lightly.  
  
If you call this method after calling setIsBrowserInsideApp, this  
docshell will forget the fact that it was a browser.  
  
</code>
### setIsBrowserInsideApp(containingAppId) ###
<code>  
Indicate that this docshell corresponds to a browser inside an app with  
the given ID.  As with setIsApp, you may pass NO_APP_ID or  
UNKNOWN_APP_ID.  
  
As with setIsApp, you may call this more than once, but it's kind of a  
hack, so be careful.  
  
</code>
### getSameTypeParentIgnoreBrowserAndAppBoundaries() ###
<code>  
Like nsIDocShellTreeItem::GetSameTypeParent, except this ignores <iframe  
mozbrowser> and <iframe mozapp> boundaries.  
  
</code>
### isSandboxedFrom(aTargetDocShell) ###
<code>  
Returns true if we are sandboxed from aTargetDocShell.  
aTargetDocShell - the browsing context we are attempting to navigate.  
  
</code>
### GetAllowMixedContentAndConnectionData(rootHasSecureConnection, allowMixedContent, isRootDocShell) ###
<code>  
Checks whether the channel associated with the root docShell is equal to  
mMixedContentChannel. If they are the same, allowMixedContent is set to true.  
Checks if the root document has a secure connection. If it is, sets   
rootHasSecureConnection to true. If the docShell is the root doc shell,   
isRootDocShell is set to true.   
  
</code>
### pluginsAllowedInCurrentDoc() ###
<code>  
Are plugins allowed in the current document loaded in this docshell ?  
(if there is one). This depends on whether plugins are allowed by this  
docshell itself or if the document is sandboxed and hence plugins should  
not be allowed.  
  
</code>
### setFullscreenAllowed(allowed) ###

### makeEditable(inWaitForUriLoad) ###
<code>  
Make this docShell editable, setting a flag that causes  
an editor to get created, either immediately, or after  
a url has been loaded.  
     @param  inWaitForUriLoad    true to wait for a URI before  
                                 creating the editor.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>inWaitForUriLoad</td>
<td>true to wait for a URI before  
                                 creating the editor.  
</td>
</tr>

</table>

### getChildSHEntry(aChildOffset) ###
<code>  
Get the SHEntry associated with a child docshell  
  
</code>
### addChildSHEntry(aCloneReference, aHistoryEntry, aChildOffset, aLoadType, aCloneChilden) ###
<code>  
Add a Child SHEntry for a frameset page, given the child's loadtype.  
If aCloneChildren is true, then aCloneReference's children will be  
cloned onto aHistoryEntry.  
  
</code>
### removeFromSessionHistory() ###
<code>  
Removes nsISHEntry objects related to this docshell from session history.  
Use this only with subdocuments, like iframes.  
  
</code>
### getCurrentSHEntry(aEntry) ###
<code>  
Returns false for mLSHE, true for mOSHE  
  
</code>
### isCommandEnabled(command) ###
<code>  
Cherry picked parts of nsIController.  
They are here, because we want to call these functions  
from JS.  
  
</code>
### doCommand(command) ###

### IsInvisible() ###
<code>  
Invisible DocShell are dummy construct to simulate DOM windows  
without any actual visual representation. They have to be marked  
at construction time, to avoid any painting activity.  
  
</code>
### SetInvisible(aIsInvisibleDochsell) ###

### GetScriptGlobalObject() ###
<code>  
Get the script global for the document in this docshell.  
  
</code>
### setOpener(aOpener) ###
<code>  
Regarding setOpener / getOpener - We can't use XPIDL's "attribute"  
for notxpcom, so we're relegated to using explicit gets / sets. This  
should be fine, considering that these methods should only ever be  
called from native code.  
  
</code>
### getOpener() ###

### setOpenedRemote(aOpenedRemote) ###
<code>  
See the documentation for setOpener and getOpener about why we  
don't use attribute here instead.  
  
</code>
### getOpenedRemote() ###

### getURLSearchParams() ###

## Attributes ##

### presContext ###
  
Presentation context for the currently loaded document.  This may be null.  
  

### eldestPresShell ###
  
Presentation shell for the oldest document, if this docshell is  
currently transitioning between documents.  
  

### contentViewer ###
  
Content Viewer that is currently loaded for this DocShell.  This may  
change as the underlying content changes.  
  

### chromeEventHandler ###
  
This attribute allows chrome to tie in to handle DOM events that may  
be of interest to chrome.  
  

### allowPlugins ###
  
Whether to allow plugin execution  
  

### allowJavascript ###
  
Whether to allow Javascript execution  
  

### allowMetaRedirects ###
  
Attribute stating if refresh based redirects can be allowed  
  

### allowSubframes ###
  
Attribute stating if it should allow subframes (framesets/iframes) or not  
  

### allowImages ###
  
Attribute stating whether or not images should be loaded.  
  

### allowMedia ###
  
Attribute stating whether or not media (audio/video) should be loaded.  
  

### allowDNSPrefetch ###
  
Attribute that determines whether DNS prefetch is allowed for this subtree  
of the docshell tree.  Defaults to true.  Setting this will make it take  
effect starting with the next document loaded in the docshell.  
  

### allowWindowControl ###
  
Attribute that determines whether window control (move/resize) is allowed.  
  

### allowContentRetargeting ###
  
True if the docshell allows its content to be handled by a content listener  
other than the docshell itself, including the external helper app service,  
and false otherwise.  Defaults to true.  
  

### appType ###

### allowAuth ###
  
certain dochshells (like the message pane)  
should not throw up auth dialogs  
because it can act as a password trojan  
  

### zoom ###
  
Set/Get the document scale factor.  When setting this attribute, a  
NS_ERROR_NOT_IMPLEMENTED error may be returned by implementations  
not supporting zoom.  Implementations not supporting zoom should return  
1.0 all the time for the Get operation.  1.0 by the way is the default  
of zoom.  This means 100% of normal scaling or in other words normal size  
no zoom.   
  

### marginWidth ###

### marginHeight ###

### busyFlags ###

### loadType ###

### defaultLoadFlags ###

### isExecutingOnLoadHandler ###

### layoutHistoryState ###

### shouldSaveLayoutState ###

### securityUI ###
  
The SecureBrowserUI object for this docshell.  This is set by XUL  
<browser> or nsWebBrowser for their root docshell.  
  

### restoringDocument ###

### useErrorPages ###

### failedChannel ###
  
The channel that failed to load and resulted in an error page.  
May be null. Relevant only to error pages.  
  

### previousTransIndex ###
  
Keeps track of the previous SHTransaction index and the current  
SHTransaction index at the time that the doc shell begins to load.  
Used for ContentViewer eviction.  
  

### loadedTransIndex ###

### currentDocumentChannel ###
  
Gets the channel for the currently loaded document, if any.   
For a new document load, this will be the channel of the previous document  
until after OnLocationChange fires.  
  

### isInUnload ###
  
Find out whether the docshell is currently in the middle of a page  
transition. This is set just before the pagehide/unload events fire.  
  

### channelIsUnsafe ###
  
Find out if the currently loaded document came from a suspicious channel  
(such as a JAR channel where the server-returned content type isn't a  
known JAR type).  
  

### hasMixedActiveContentLoaded ###
  
This attribute determines whether Mixed Active Content is loaded on the  
document. When it is true, mixed active content was not blocked and has  
loaded (or is about to load) on the page. When it is false, mixed active content  
has not loaded on the page, either because there was no mixed active content  
requests on the page or such requests were blocked by nsMixedContentBlocker.  
This boolean is set to true in nsMixedContentBlocker if Mixed Active Content  
is allowed (either explicitly on the page by the user or when the about:config  
setting security.mixed_content.block_active_content is set to false).  
  

### hasMixedActiveContentBlocked ###
  
This attribute determines whether a document has Mixed Active Content  
that has been blocked from loading. When it is true, there is definitely  
mixed active content on a page that has been blocked by  
nsMixedContentBlocker.  When it is false, there may or may not be mixed  
active content on a page, but if there is, it will load. Note that if the  
about:config setting security.mixed_content.block_active_content is set  
false, this boolean will be false, since blocking active content has been  
disabled.  
  

### hasMixedDisplayContentLoaded ###
  
This attribute determines whether Mixed Display Content is loaded on the  
document. When it is true, mixed display content was not blocked and has  
loaded (or is about to load) on the page. Similar behavior to  
hasMixedActiveContentLoaded.  
  

### hasMixedDisplayContentBlocked ###
  
This attribute determines whether a document has Mixed Display Content  
that has been blocked from loading. Similar behavior to  
hasMixedActiveContentBlocked.  
  

### hasTrackingContentBlocked ###
  
This attribute determines whether a document has Tracking Content  
that has been blocked from loading.  
  

### hasTrackingContentLoaded ###
  
This attribute determines whether Tracking Content is loaded on the  
document. When it is true, tracking content was not blocked and has  
loaded (or is about to load) on the page.  
  

### isOffScreenBrowser ###
  
If true, this browser is not visible in the traditional sense, but  
is actively being rendered to the screen (ex. painted on a canvas)  
and should be treated accordingly.  
/  

### printPreview ###
  
If the current content viewer isn't initialized for print preview,  
it is replaced with one which is and to which an about:blank document  
is loaded.  
  

### canExecuteScripts ###
  
Whether this docshell can execute scripts based on its hierarchy.  
The rule of thumb here is that we disable js if this docshell or any  
of its parents disallow scripting.  
  

### isActive ###
  
Sets whether a docshell is active. An active docshell is one that is  
visible, and thus is not a good candidate for certain optimizations  
like image frame discarding. Docshells are active unless told otherwise.  
  

### historyID ###
  
The ID of the docshell in the session history.  
  

### isAppTab ###
  
Sets whether a docshell is an app tab. An app tab docshell may behave  
differently than a non-app tab docshell in some cases, such as when  
handling link clicks. Docshells are not app tabs unless told otherwise.  
  

### charset ###
  
Upon getting, returns the canonical encoding label of the document  
currently loaded into this docshell.  
  
Upon setting, sets forcedCharset for compatibility with legacy callers.  
  

### forcedCharset ###
  
The charset forced by the user.  
  

### recordProfileTimelineMarkers ###
  
Whether the docShell records profile timeline markers at the moment  
  

### isBrowserElement ###
  
Returns true if this docshell corresponds to an <iframe mozbrowser>.  
(<iframe mozapp mozbrowser> is not considered a browser.)  
  

### isApp ###
  
Returns true iff the docshell corresponds to an <iframe mozapp>.  
  

### isBrowserOrApp ###
  
Returns isBrowserElement || isApp.  
  

### isInBrowserElement ###
  
Returns true if this docshell corresponds to an <iframe mozbrowser> or if  
the docshell is contained in an <iframe mozbrowser>.  (<iframe mozapp  
mozbrowser> does not count as a browser.)  
  
Our notion here of "contained in" means: Walk up the docshell hierarchy in  
this process until we hit an <iframe mozapp> or <iframe mozbrowser> (or  
until the hierarchy ends).  Return true iff the docshell we stopped on has  
isBrowserElement == true.  
  

### isInBrowserOrApp ###
  
Returns true if this docshell corresponds to an <iframe mozbrowser> or  
<iframe mozap>, or if this docshell is contained in an <iframe mozbrowser>  
or <iframe mozapp>.  
  
To compute this value, we walk up the docshell hierarchy.  If we encounter  
a docshell with isBrowserElement or isApp before we hit the end of the  
hierarchy, we return true.  Otherwise, we return false.  
  

### appId ###
  
Returns the id of the app associated with this docshell.  If this docshell  
is an <iframe mozbrowser> inside an <iframe mozapp>, we return the app's  
appId.  
  
We compute this value by walking up the docshell hierarchy until we find a  
docshell on which setIsApp(x) or setIsBrowserInsideApp(x) was called  
(ignoring those docshells where x == UNKNOWN_APP_ID).  We return the app  
id x.  
  
If we don't find a docshell with an associated app id in our hierarchy, we  
return NO_APP_ID.  We never return UNKNOWN_APP_ID.  
  
Notice that a docshell may have an associated app even if it returns true  
for isBrowserElement!  
  

### appManifestURL ###
  
Return the manifest URL of the app associated with this docshell.  
  
If there is no associated app in our hierarchy, we return empty string.  
  

### asyncPanZoomEnabled ###
   
True iff asynchronous panning and zooming is enabled for this  
docshell.  
  

### sandboxFlags ###
  
The sandbox flags on the docshell. These reflect the value of the sandbox  
attribute of the associated IFRAME or CSP-protectable content, if  
existent. See the HTML5 spec for more details.  
These flags on the docshell reflect the current state of the sandbox  
attribute, which is modifiable. They are only used when loading new  
content, sandbox flags are also immutably set on the document when it is  
loaded.  
The sandbox flags of a document depend on the sandbox flags on its  
docshell and of its parent document, if any.  
See nsSandboxFlags.h for the possible flags.  
  

### onePermittedSandboxedNavigator ###
  
When a new browsing context is opened by a sandboxed document, it needs to  
keep track of the browsing context that opened it, so that it can be  
navigated by it.  This is the "one permitted sandboxed navigator".  
  

### mixedContentChannel ###
  
This member variable determines whether a document has Mixed Active Content that  
was initially blocked from loading, but the user has choosen to override the  
block and allow the content to load. mMixedContentChannel is set to the document's  
channel when the user allows mixed content. The nsMixedContentBlocker content policy  
checks if the document's root channel matches the mMixedContentChannel.  If it matches,  
then Mixed Content is loaded.  If it does match, mixed content is blocked.  
  
A match implies that there is definitely mixed active content on a page that was  
initially blocked by nsMixedContentBlocker and then allowed and loaded by the user.  
A miss imples that IF there is mixed active content on the page AND it was  
blocked by nsMixedContentBlocker.cpp, the user has not choosen to override  
the block. Note that if the about:config setting  
security.mixed_content.block_active_content is set to false, this boolean  
will be false, mMixedContentChannel will remain null since blocking active content has  
been disabled and hence mMixedContentChannel will never be set.  
  

### fullscreenAllowed ###
  
Attribute that determines whether fullscreen is allowed to be entered for  
this subtree of the docshell tree. This is true when all iframes containing  
this docshell have their "allowfullscreen" attribute set to "true".  
fullscreenAllowed is only writable at content boundaries, where it is used  
to propagate the value of the cross process parent's iframe's  
"allowfullscreen" attribute to the child process. Setting  
fullscreenAllowed on docshells which aren't content boundaries throws an  
exception.  
  

### affectPrivateSessionLifetime ###

### mayEnableCharacterEncodingMenu ###
  
Indicates whether the UI may enable the character encoding menu. The UI  
must disable the menu when this property is false.  
  

### editor ###

### editable ###

### hasEditingSession ###

### useGlobalHistory ###
  
Whether this docshell should save entries in global history.  
  

### createdDynamically ###
  
Set when an iframe/frame is added dynamically.  
  

### deviceSizeIsPageSize ###
  
If deviceSizeIsPageSize is set to true, device-width/height media queries  
will be calculated from the page size, not the device size.  
  
Used by the Responsive Design View and B2G Simulator.  
  
Default is False.  
Default value can be overriden with  
docshell.device_size_is_page_size pref.  
  

### hasLoadedNonBlankURI ###
  
This attribute determines whether a document which is not about:blank has  
already be loaded by this docShell.  
  

## Constants ##

### INTERNAL_LOAD_FLAGS_NONE ###

### INTERNAL_LOAD_FLAGS_INHERIT_OWNER ###

### INTERNAL_LOAD_FLAGS_DONT_SEND_REFERRER ###

### INTERNAL_LOAD_FLAGS_ALLOW_THIRD_PARTY_FIXUP ###

### INTERNAL_LOAD_FLAGS_FIRST_LOAD ###

### INTERNAL_LOAD_FLAGS_BYPASS_CLASSIFIER ###

### INTERNAL_LOAD_FLAGS_FORCE_ALLOW_COOKIES ###

### INTERNAL_LOAD_FLAGS_IS_SRCDOC ###

### INTERNAL_LOAD_FLAGS_NO_OPENER ###

### ENUMERATE_FORWARDS ###
  
Get an enumerator over this docShell and its children.  
  
@param aItemType  - Only include docShells of this type, or if typeAll,  
                    include all child shells.  
                    Uses types from nsIDocShellTreeItem.  
@param aDirection - Whether to enumerate forwards or backwards.  
  

### ENUMERATE_BACKWARDS ###

### APP_TYPE_UNKNOWN ###
  
The type of application that created this window  
  

### APP_TYPE_MAIL ###

### APP_TYPE_EDITOR ###

### BUSY_FLAGS_NONE ###
  
Current busy state for DocShell  
  

### BUSY_FLAGS_BUSY ###

### BUSY_FLAGS_BEFORE_PAGE_LOAD ###

### BUSY_FLAGS_PAGE_LOADING ###

### LOAD_CMD_NORMAL ###
  
Load commands for the document   
  

### LOAD_CMD_RELOAD ###

### LOAD_CMD_HISTORY ###

### LOAD_CMD_PUSHSTATE ###
