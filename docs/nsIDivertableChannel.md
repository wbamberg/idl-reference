---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIDivertableChannel.idl">Source file</a>
</div>

# nsIDivertableChannel #
<pre>  
A channel implementing this interface allows diverting from an  
nsIStreamListener in the child process to one in the parent.  
  
</pre>
## Methods ##

### divertToParent() ###
<pre>  
CHILD ONLY.  
Called by Necko client in child process during OnStartRequest to divert  
nsIStreamListener and nsIRequest callbacks to the parent process.  
  
The process should look like the following:  
  
1) divertToParent is called in the child process.  It can only be called  
   during OnStartRequest().  
  
2) The ChannelDiverterChild that is returned is an IPDL object. It should  
   be passed via some other IPDL method of the client's choosing to the  
   parent.  On the parent the ChannelDiverterParent's divertTo() function  
   should be called with an nsIStreamListener that will then receive the  
   OnStartRequest/OnDataAvailable/OnStopRequest for the channel.  The  
   ChannelDiverterParent can then be deleted (which will also destroy the  
   ChannelDiverterChild in the child).  
  
   After divertToParent() has been called, NO further function calls  
   should be made on the channel.  It is a dead object for all purposes.  
   The reference that the channel holds to the listener in the child is  
   released is once OnStartRequest completes, and no other  
   nsIStreamListener calls (OnDataAvailable, OnStopRequest) will be made  
   to it.  
  
@return ChannelDiverterChild IPDL actor to be passed to parent process by  
        client IPDL message, e.g. PClient.DivertUsing(PDiverterChild).  
  
@throws exception if the channel was canceled early. Throws status code of  
        canceled channel.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>ChannelDiverterChild IPDL actor to be passed to parent process by  
        client IPDL message, e.g. PClient.DivertUsing(PDiverterChild).  
</td>
</tr>

</table>
