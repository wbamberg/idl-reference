---
layout: default
---

# nsINotificationStorageCallback #

## Methods ##

### handle ###

Callback function used to pass single notification back
into C++ land for Notification.get return data.

@param id: a uuid for this notification
@param title: the notification title
@param dir: the notification direction,
            possible values are "ltr", "rtl", "auto"
@param lang: the notification language
@param body: the notification body
@param tag: the notification tag


### done ###

Callback function used to notify C++ the we have returned
all notification objects for this Notification.get call.

