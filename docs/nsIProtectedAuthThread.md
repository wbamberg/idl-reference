---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIProtectedAuthThread.idl">Source file</a>
</div>

# nsIProtectedAuthThread #
<pre>  
nsIProtectedAuthThread  
 This is used to communicate with the thread login on to   
 a token with CKF_PROTECTED_AUTHENTICATION_PATH set.  
  
</pre>
## Methods ##

### login(observer) ###
<pre>  
login - run the thread  
  A user interface implementing this interface needs to  
  call this method as soon as the message to the user is  
  displayed. This will trigger login operation. No user   
  cancellation is possible during login operation.  
  
  When the login is done, the observe method of @observer will  
  be called on the UI thread with a topic of "login-finished"  
  and null data and subject.  
  
</pre>
### getTokenName() ###
<pre>  
Gets token to be logged in name.  
  
</pre>
## Attributes ##

### slot ###
<pre>  
The PKCS11 slot  
  
</pre>