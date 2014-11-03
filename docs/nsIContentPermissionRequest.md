---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIContentPermissionPrompt.idl">Source file</a>
</div>

# nsIContentPermissionRequest #
<code>  
Interface allows access to a content to request  
permission to perform a privileged operation such as  
geolocation.  
  
</code>
## Methods ##

### cancel() ###
<code>  
allow or cancel the request  
  
</code>
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
