---
layout: default
---

# nsIProtectedAuthThread #
  
nsIProtectedAuthThread  
 This is used to communicate with the thread login on to   
 a token with CKF_PROTECTED_AUTHENTICATION_PATH set.  
  

## Methods ##

### login ###
  
login - run the thread  
  A user interface implementing this interface needs to  
  call this method as soon as the message to the user is  
  displayed. This will trigger login operation. No user   
  cancellation is possible during login operation.  
  
  When the login is done, the observe method of @observer will  
  be called on the UI thread with a topic of "login-finished"  
  and null data and subject.  
  

### getTokenName ###
  
Gets token to be logged in name.  
  

## Attributes ##

### slot ###
  
The PKCS11 slot  
  
