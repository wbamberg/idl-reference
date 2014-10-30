---
layout: default
---

# nsISpeechTaskCallback #
  
A callback is implemented by the service. For direct audio services, it is  
required to implement these, although it could be helpful to use the  
cancel method for shutting down the speech resources.  
  

## Methods ##

### onPause() ###
  
The user or application has paused the speech.  
  

### onResume() ###
  
The user or application has resumed the speech.  
  

### onCancel() ###
  
The user or application has canceled the speech.  
  
