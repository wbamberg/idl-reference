---
layout: default
---

# nsIAlertsProgressListener #

## Methods ##

### onProgress ###
  
Called to notify the alert service that progress has occurred for the  
given notification previously displayed with showAlertNotification().  
  
@param name         The name of the notification displaying the  
                    progress. On Android the name is hashed and used  
                    as a notification ID.  
@param progress     Numeric value in the range 0 to progressMax  
                    indicating the current progress.  
@param progressMax  Numeric value indicating the maximum progress.  
@param text         The contents of the alert. If not provided,  
                    the percentage will be displayed.  
  

### onCancel ###
  
Called to cancel and hide the given notification previously displayed  
with showAlertNotification().  
  
@param name         The name of the notification.  
  
