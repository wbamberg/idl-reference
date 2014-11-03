---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIChildChannel.idl">Source file</a>
</div>

# nsIChildChannel #
  
Implemented by content side of IPC protocols.  
  

## Methods ##

### connectParent(id) ###
  
Create the chrome side of the IPC protocol and join an existing 'real'  
channel on the parent process.  The id is provided by  
nsIRedirectChannelRegistrar on the chrome process and pushed to the child  
protocol as an argument to event starting a redirect.  
  
Primarilly used in HttpChannelChild::Redirect1Begin on a newly created  
child channel, where the new channel is intended to be created on the  
child process.  
  

### completeRedirectSetup(aListener, aContext) ###
  
As AsyncOpen is called on the chrome process for redirect target channels,  
we have to inform the child side of the protocol of that fact by a special  
method.  
  
