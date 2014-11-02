---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/notification/nsINotificationStorage.idl">Source file</a>
</div>

# nsINotificationStorage #
  
Interface for notification persistence layer.  
  

## Methods ##

### put(origin, id, title, dir, lang, body, tag, icon, alertName, data, behavior) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>origin:</td>
<td>the origin/app of this notification  
</td>
</tr>

<tr>
<td>id:</td>
<td>a uuid for this notification  
</td>
</tr>

<tr>
<td>title:</td>
<td>the notification title  
</td>
</tr>

<tr>
<td>dir:</td>
<td>the notification direction,  
            possible values are "ltr", "rtl", "auto"  
</td>
</tr>

<tr>
<td>lang:</td>
<td>the notification language  
</td>
</tr>

<tr>
<td>body:</td>
<td>the notification body  
</td>
</tr>

<tr>
<td>tag:</td>
<td>notification tag, will replace any existing  
            notifications with same origin/tag pair  
</td>
</tr>

<tr>
<td>alertName:</td>
<td>the alert identifier as used by system app.  
                  Stored in the database to avoid re-computing  
                  it. Built from origin and tag or id depending  
                  whether there is a tag defined.  
</td>
</tr>

</table>

### get(origin, tag, aCallback) ###
  
Retrieve a list of notifications.  
  
@param origin: the origin/app for which to fetch notifications from  
@param tag: used to fetch only a specific tag  
@param callback: nsINotificationStorageCallback, used for  
                 returning notifications objects  
  

#### Parameters ####

<table>

<tr>
<td>origin:</td>
<td>the origin/app for which to fetch notifications from  
</td>
</tr>

<tr>
<td>tag:</td>
<td>used to fetch only a specific tag  
</td>
</tr>

<tr>
<td>callback:</td>
<td>nsINotificationStorageCallback, used for  
                 returning notifications objects  
</td>
</tr>

</table>

### delete(origin, id) ###
  
Remove a notification from storage.  
  
@param origin: the origin/app to delete the notification from  
@param id: the uuid for the notification to delete  
  

#### Parameters ####

<table>

<tr>
<td>origin:</td>
<td>the origin/app to delete the notification from  
</td>
</tr>

<tr>
<td>id:</td>
<td>the uuid for the notification to delete  
</td>
</tr>

</table>
