---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/alerts/nsIAlertsService.idl">Source file</a>
</div>

# nsIAlertsService #

## Methods ##

### showAlertNotification(imageUrl, title, text, textClickable, cookie, alertListener, name, dir, lang, data, principal) ###
<pre>  
Displays a sliding notification window.  
  
@param imageUrl       A URL identifying the image to put in the alert.  
                      The OS X implemenation limits the amount of time it  
                      will wait for an icon to load to six seconds. After  
                      that time the alert will show with no icon.  
@param title          The title for the alert.  
@param text           The contents of the alert.  
@param textClickable  If true, causes the alert text to look like a link  
                      and notifies the listener when user attempts to   
                      click the alert text.  
@param cookie         A blind cookie the alert will pass back to the   
                      consumer during the alert listener callbacks.  
@param alertListener  Used for callbacks. May be null if the caller   
                      doesn't care about callbacks.  
@param name           The name of the notification. This is currently only  
                      used on Android and OS X. On Android the name is  
                      hashed and used as a notification ID. Notifications  
                      will replace previous notifications with the same name.  
@param dir            Bidi override for the title. Valid values are  
                      "auto", "ltr" or "rtl". Only available on supported  
                      platforms.  
@param lang           Language of title and text of the alert. Only available  
                      on supported platforms.  
@throws NS_ERROR_NOT_AVAILABLE If the notification cannot be displayed.  
  
The following arguments will be passed to the alertListener's observe()   
method:  
  subject - null  
  topic   - "alertfinished" when the alert goes away  
            "alertclickcallback" when the text is clicked  
            "alertshow" when the alert is shown  
  data    - the value of the cookie parameter passed to showAlertNotification.  
  
@note Depending on current circumstances (if the user's in a fullscreen  
      application, for instance), the alert might not be displayed at all.  
      In that case, if an alert listener is passed in it will receive the  
      "alertfinished" notification immediately.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>imageUrl</td>
<td>A URL identifying the image to put in the alert.  
                      The OS X implemenation limits the amount of time it  
                      will wait for an icon to load to six seconds. After  
                      that time the alert will show with no icon.  
</td>
</tr>

<tr>
<td>title</td>
<td>The title for the alert.  
</td>
</tr>

<tr>
<td>text</td>
<td>The contents of the alert.  
</td>
</tr>

<tr>
<td>textClickable</td>
<td>If true, causes the alert text to look like a link  
                      and notifies the listener when user attempts to   
                      click the alert text.  
</td>
</tr>

<tr>
<td>cookie</td>
<td>A blind cookie the alert will pass back to the   
                      consumer during the alert listener callbacks.  
</td>
</tr>

<tr>
<td>alertListener</td>
<td>Used for callbacks. May be null if the caller   
                      doesn't care about callbacks.  
</td>
</tr>

<tr>
<td>name</td>
<td>The name of the notification. This is currently only  
                      used on Android and OS X. On Android the name is  
                      hashed and used as a notification ID. Notifications  
                      will replace previous notifications with the same name.  
</td>
</tr>

<tr>
<td>dir</td>
<td>Bidi override for the title. Valid values are  
                      "auto", "ltr" or "rtl". Only available on supported  
                      platforms.  
</td>
</tr>

<tr>
<td>lang</td>
<td>Language of title and text of the alert. Only available  
                      on supported platforms.  
@throws NS_ERROR_NOT_AVAILABLE If the notification cannot be displayed.  
</td>
</tr>

</table>

### closeAlert(name, principal) ###
<pre>  
Close alerts created by the service.  
  
@param name           The name of the notification to close. If no name  
                      is provided then only a notification created with  
                      no name (if any) will be closed.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The name of the notification to close. If no name  
                      is provided then only a notification created with  
                      no name (if any) will be closed.  
</td>
</tr>

</table>
