---
layout: default
---

# nsIMozBrowserFrame #

## Methods ##

### disallowCreateFrameLoader() ###
  
Normally, a frame tries to create its frame loader when its src is  
modified, or its contentWindow is accessed.  
  
disallowCreateFrameLoader prevents the frame element from creating its  
frame loader (in the same way that not being inside a document prevents the  
creation of a frame loader).  allowCreateFrameLoader lifts this restriction.  
  
These methods are not re-entrant -- it is an error to call  
disallowCreateFrameLoader twice without first calling allowFrameLoader.  
  
It's also an error to call either method if we already have a frame loader.  
  

### allowCreateFrameLoader() ###

### createRemoteFrameLoader(aTabParent) ###
  
Create a remote (i.e., out-of-process) frame loader attached to the given  
tab parent.  
  
It is an error to call this method if we already have a frame loader.  
  

## Attributes ##

### reallyIsBrowserOrApp ###
  
Gets whether this frame really is a browser or app frame.  
  
In order to really be a browser frame, this frame's  
nsIDOMMozBrowserFrame::mozbrowser attribute must be true, and the frame  
may have to pass various security checks.  
  

### reallyIsApp ###
  
Gets whether this frame really is an app frame.  
  
In order to really be an app frame, this frame must really be a browser  
frame (this requirement will go away eventually), and must satisfy one  
and only one of the following conditions:  
1. the frame's mozapp attribute must point to the manifest of a valid app  
2. the frame's mozwidget attribute must point to the manifest of a valid  
app, and the src should be in the |widgetPages| specified by the manifest.  
  

### reallyIsWidget ###
  
Gets whether this frame really is a widget frame.  
  
In order to really be a frame, this frame must really be a browser  
frame (this requirement will go away eventually), the frame's mozwidget  
attribute must point to the manifest of a valid app, and the src should  
be in the |widgetPages| specified by the manifest.  
  

### isExpectingSystemMessage ###
  
This corresponds to the expecting-system-message attribute, which tells us  
whether we should expect that this frame will receive a system message once  
it starts up.  
  
It's the embedder's job to set this attribute on a frame.  Its presence  
might cause us to increase the priority of the frame's process.  
  

### appManifestURL ###
  
Gets this frame's app manifest URL or widget manifest URL, if the frame  
really is an app frame.  
Otherwise, returns the empty string.  
  
This method is guaranteed not to fail.  
  
