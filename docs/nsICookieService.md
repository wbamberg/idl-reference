---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cookie/nsICookieService.idl">Source file</a>
</div>

# nsICookieService #
  
nsICookieService  
  
Provides methods for setting and getting cookies in the context of a  
page load.  See nsICookieManager for methods to manipulate the cookie  
database directly.  This separation of interface is mainly historical.  
  
This service broadcasts the notifications detailed below when the cookie  
list is changed, or a cookie is rejected.  
  
NOTE: observers of these notifications *must* not attempt to change profile  
      or switch into or out of private browsing mode from within the  
      observer. Doing so will cause undefined behavior. Mutating the cookie  
      list (e.g. by calling methods on nsICookieService and friends) is  
      allowed, but beware that there may be pending notifications you haven't  
      seen yet -- for instance, a "batch-deleted" notification will likely be  
      immediately followed by "added". You may check the state of the cookie  
      list to determine if this is the case.  
  
topic  : "cookie-changed"  
         broadcast whenever the cookie list changes in some way. see  
         explanation of data strings below.  
subject: see below.  
data   : "deleted"  
         a cookie was deleted. the subject is an nsICookie2 representing  
         the deleted cookie.  
         "added"  
         a cookie was added. the subject is an nsICookie2 representing  
         the added cookie.  
         "changed"  
         a cookie was changed. the subject is an nsICookie2 representing  
         the new cookie. (note that host, path, and name are invariant  
         for a given cookie; other parameters may change.)  
         "batch-deleted"  
         a set of cookies was purged (typically, because they have either  
         expired or because the cookie list has grown too large). The subject  
         is an nsIArray of nsICookie2's representing the deleted cookies.  
         Note that the array could contain a single cookie.  
         "cleared"  
         the entire cookie list was cleared. the subject is null.  
         "reload"  
         the entire cookie list should be reloaded.  the subject is null.  
  
topic  : "cookie-rejected"  
         broadcast whenever a cookie was rejected from being set as a  
         result of user prefs.  
subject: an nsIURI interface pointer representing the URI that attempted  
         to set the cookie.  
data   : none.  
  
topic  : "third-party-cookie-accepted"  
          broadcast whenever a third party cookie was accepted  
subject:  an nsIURI interface pointer representing the URI that attempted  
          to set the cookie.  
data   :  the referrer, or "?" if unknown  
  
topic  : "third-party-cookie-rejected"  
          broadcast whenever a third party cookie was rejected  
subject:  an nsIURI interface pointer representing the URI that attempted  
          to set the cookie.  
data   :  the referrer, or "?" if unknown  
  

## Methods ##

### getCookieString(aURI, aChannel) ###

### getCookieStringFromHttp(aURI, aFirstURI, aChannel) ###

### setCookieString(aURI, aPrompt, aCookie, aChannel) ###

### setCookieStringFromHttp(aURI, aFirstURI, aPrompt, aCookie, aServerTime, aChannel) ###
