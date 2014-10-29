---
layout: default
---

# nsISecurityWarningDialogs #

Functions that display warnings for transitions between secure
and insecure pages, posts to insecure servers etc.


## confirmPostToInsecureFromSecure ##

 Inform the user: Although the currently displayed
 page was loaded using a secure connection, and the UI probably
 currently indicates a secure page, 
 that information is being submitted to an insecure page.

 @param ctx A user interface context.

 @return true if the user confirms to submit.

