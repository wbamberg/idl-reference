---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/ipc/nsIRemoteOpenFileListener.idl">Source file</a>
</div>

# nsIRemoteOpenFileListener #
  
nsIRemoteOpenFileListener: passed to RemoteOpenFileChild::AsyncRemoteFileOpen.  
  
Interface for notifying when the file has been opened and is available in  
child.  
  

## Methods ##

### onRemoteFileOpenComplete(aOpenStatus) ###
  
Called when result of opening RemoteOpenFileChild:AsyncRemoteFileOpen()  
is available in child.  
  
@param aOpenStatus: nsresult from opening file in parent.  If NS_OK,  
then a following call to RemoteOpenFileChild::OpenNSPRFileDesc that  
passes the same flags as were passed to  
RemoteOpenFileChild::AsyncRemoteFileOpen is guaranteed to succeed.  If  
!NS_OK or if different flags were passed, the call will fail.  
  

#### Parameters ####

<table>

<tr>
<td>aOpenStatus:</td>
<td>nsresult from opening file in parent.  If NS_OK,  
then a following call to RemoteOpenFileChild::OpenNSPRFileDesc that  
passes the same flags as were passed to  
RemoteOpenFileChild::AsyncRemoteFileOpen is guaranteed to succeed.  If  
!NS_OK or if different flags were passed, the call will fail.  
</td>
</tr>

</table>
