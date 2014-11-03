---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIContentPermissionPrompt.idl">Source file</a>
</div>

# nsIContentPermissionRequest #
<pre>  
Interface allows access to a content to request  
permission to perform a privileged operation such as  
geolocation.  
  
</pre>
## Methods ##

### cancel() ###
<pre>  
allow or cancel the request  
  
</pre>
### allow(choices) ###

## Attributes ##

### types ###
<pre>  
 The array will include the request types. Elements of this array are  
 nsIContentPermissionType object.  
  
</pre>
### principal ###

### window ###
<pre>  
 The window or element that the permission request was  
 originated in.  Typically the element will be non-null  
 in when using out of process content.  window or  
 element can be null but not both.  
  
</pre>
### element ###
