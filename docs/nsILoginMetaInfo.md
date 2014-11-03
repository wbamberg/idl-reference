---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/passwordmgr/nsILoginMetaInfo.idl">Source file</a>
</div>

# nsILoginMetaInfo #
<code>  
An object containing metainfo for a login stored by the login manager.  
  
Code using login manager can generally ignore this interface. When adding  
logins, default value will be created. When modifying logins, these  
properties will be unchanged unless a change is explicitly requested [by  
using modifyLogin() with a nsIPropertyBag]. When deleting a login or  
comparing logins, these properties are ignored.  
  
</code>
## Attributes ##

### guid ###
  
The GUID to uniquely identify the login. This can be any arbitrary  
string, but a format as created by nsIUUIDGenerator is recommended.  
For example, "{d4e1a1f6-5ea0-40ee-bff5-da57982f21cf}"  
  
addLogin will generate a random value unless a value is provided.  
  
addLogin and modifyLogin will throw if the GUID already exists.  
  

### timeCreated ###
  
The time, in Unix Epoch milliseconds, when the login was first created.  
  

### timeLastUsed ###
  
The time, in Unix Epoch milliseconds, when the login was last submitted  
in a form or used to begin an HTTP auth session.  
  

### timePasswordChanged ###
  
The time, in Unix Epoch milliseconds, when the login's password was  
last modified.  
  

### timesUsed ###
  
The number of times the login was submitted in a form or used to begin  
an HTTP auth session.  
  
