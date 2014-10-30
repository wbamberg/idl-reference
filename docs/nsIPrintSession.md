---
layout: default
---

# nsIPrintSession #
  
nsIPrintSession  
  
Stores data pertaining only to a single print job. This  
differs from nsIPrintSettings, which stores data which may  
be valid across a number of jobs.  
  
This interface is currently empty since, at this point, only  
platform-specific derived interfaces offer any functionality.  
It is here as a placeholder for when the printing session has  
XP functionality.  
  
The creation of a component which implements this interface  
will begin the session. Likewise, destruction of that object  
will end the session.  
  
@status  
  
