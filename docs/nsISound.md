---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsISound.idl">Source file</a>
</div>
# nsISound #

## Methods ##

### play(aURL) ###

### playSystemSound(soundAlias) ###
  
for playing system sounds  
  
NS_SYSSOUND_* params are obsolete. The new events will not be supported by  
this method.  You should use playEventSound method instaed.  
  

### beep() ###

### init() ###
  
Not strictly necessary, but avoids delay before first sound.  
The various methods on nsISound call Init() if they need to.  
  

### playEventSound(aEventId) ###

## Constants ##

### EVENT_NEW_MAIL_RECEIVED ###
  
In some situations, playEventSound will be called.  Then, each  
implementations will play a system sound for the event if it's necessary.  
  
NOTE: Don't change these values because they are used in  
nsPIPromptService.idl. So, if they are changed, that makes big impact for  
the embedders.  
  

### EVENT_ALERT_DIALOG_OPEN ###

### EVENT_CONFIRM_DIALOG_OPEN ###

### EVENT_PROMPT_DIALOG_OPEN ###

### EVENT_SELECT_DIALOG_OPEN ###

### EVENT_MENU_EXECUTE ###

### EVENT_MENU_POPUP ###

### EVENT_EDITOR_MAX_LEN ###
