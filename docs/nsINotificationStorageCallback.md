---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/notification/nsINotificationStorage.idl">Source file</a>
</div>

# nsINotificationStorageCallback #

## Methods ##

### handle(id, title, dir, lang, body, tag, icon, data, behavior) ###
<pre>  
Callback function used to pass single notification back  
into C++ land for Notification.get return data.  
  
@param id: a uuid for this notification  
@param title: the notification title  
@param dir: the notification direction,  
            possible values are "ltr", "rtl", "auto"  
@param lang: the notification language  
@param body: the notification body  
@param tag: the notification tag  
  
</pre>
#### Parameters ####

<table>

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
<td>the notification tag  
</td>
</tr>

</table>

### done() ###
<pre>  
Callback function used to notify C++ the we have returned  
all notification objects for this Notification.get call.  
  
</pre>