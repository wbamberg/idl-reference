---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/network/interfaces/nsITCPServerSocketParent.idl">Source file</a>
</div>
# nsITCPServerSocketParent #
   
Interface required to allow the TCP server-socket object in the parent process  
to talk to the parent IPC actor.  
It is used in the server socket implementation on the parent side.  
  

## Methods ##

### sendCallbackAccept(socket) ###
  
Trigger a callback in the content process when the socket accepts any request.  
  
@param socket  
       The socket generated in accepting any open request on the parent side.  
  

#### Parameters ####

<table>

<tr>
<td>socket</td>
<td>       The socket generated in accepting any open request on the parent side.  
</td>
</tr>

</table>

### sendCallbackError(message, filename, lineNumber, columnNumber) ###
  
Trigger a callback in the content process when an error occurs.  
  
@param message  
       The error message.  
@param filename  
       The file name in which the error occured.  
@param lineNumber  
       The line number in which the error occured.  
@param columnNumber  
       The column number in which the error occured.  
  

#### Parameters ####

<table>

<tr>
<td>message</td>
<td>       The error message.  
</td>
</tr>

<tr>
<td>filename</td>
<td>       The file name in which the error occured.  
</td>
</tr>

<tr>
<td>lineNumber</td>
<td>       The line number in which the error occured.  
</td>
</tr>

<tr>
<td>columnNumber</td>
<td>       The column number in which the error occured.  
</td>
</tr>

</table>
