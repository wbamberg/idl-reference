---
layout: default
---

# nsINotificationStorage #
  
Interface for notification persistence layer.  
  

## Methods ##

### put ###
  
Add/replace a notification to the persistence layer.  
  
@param origin: the origin/app of this notification  
@param id: a uuid for this notification  
@param title: the notification title  
@param dir: the notification direction,  
            possible values are "ltr", "rtl", "auto"  
@param lang: the notification language  
@param body: the notification body  
@param tag: notification tag, will replace any existing  
            notifications with same origin/tag pair  
@param alertName: the alert identifier as used by system app.  
                  Stored in the database to avoid re-computing  
                  it. Built from origin and tag or id depending  
                  whether there is a tag defined.  
  

### get ###
  
Retrieve a list of notifications.  
  
@param origin: the origin/app for which to fetch notifications from  
@param tag: used to fetch only a specific tag  
@param callback: nsINotificationStorageCallback, used for  
                 returning notifications objects  
  

### delete ###
  
Remove a notification from storage.  
  
@param origin: the origin/app to delete the notification from  
@param id: the uuid for the notification to delete  
  
