---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIContentPermissionPrompt.idl">Source file</a>
</div>
# nsIContentPermissionRequest #
  
Interface allows access to a content to request  
permission to perform a privileged operation such as  
geolocation.  
  

## Methods ##

### cancel() ###
  
allow or cancel the request  
  

### allow(choices) ###

## Attributes ##

### types ###
  
 The array will include the request types. Elements of this array are  
 nsIContentPermissionType object.  
  

### principal ###

### window ###
  
 The window or element that the permission request was  
 originated in.  Typically the element will be non-null  
 in when using out of process content.  window or  
 element can be null but not both.  
  

### element ###
