---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsILoadInfo.idl">Source file</a>
</div>

# nsILoadInfo #
  
An nsILoadOwner represents per-load information about who started the load.  
  

## Methods ##

### binaryLoadingPrincipal() ###
  
A C++-friendly version of loadingPrincipal.  
  

### binaryLoadingNode() ###
  
A C++-friendly version of loadingDocument (loadingNode).  
This is the node most proximally responsible for the load.  
  

## Attributes ##

### loadingPrincipal ###
  
The loadingPrincipal is the principal that is responsible for the load.  
It is *NOT* the principal tied to the resource/URI that this  
channel is loading, it's the principal of the resource's  
caller or requester. For example, if this channel is loading  
an image from http://b.com that is embedded in a document  
who's origin is http://a.com, the loadingPrincipal is http://a.com.  
  
The loadingPrincipal will never be null.  
  

### loadingDocument ###
  
The loadingDocument of the channel.  
  
The loadingDocument of a channel is the document that requested the  
load of the resource. It is *not* the resource itself, it's the  
resource's caller or requester in which the load is happening.  
  
<script> example: Assume a document who's origin is http://a.com embeds  
a script from http://b.com. The loadingDocument for the channel  
associated with the http://b.com script load is the document with origin  
http://a.com  
  
<iframe> example: Assume a document with origin http://a.com embeds  
<iframe src="http://b.com">. The loadingDocument for the channel associated  
with the http://b.com network request is the document who's origin is  
http://a.com. Now assume the iframe to http://b.com then further embeds  
<script src="http://c.com">. The loadingDocument for the channel associated  
with the http://c.com network request is the iframe with origin http://b.com.  
  
Warning: The loadingDocument can be null!  
  

### securityFlags ###
  
The securityFlags of that channel.  
  

### forceInheritPrincipal ###
  
If forceInheritPrincipal is true, the data coming from the channel should  
use loadingPrincipal for its principal, even when the data is loaded over  
http:// or another protocol that would normally use a URI-based principal.  
This attribute will never be true when loadingSandboxed is true.  
  

### loadingSandboxed ###
  
If loadingSandboxed is true, the data coming from the channel is  
being loaded sandboxed, so it should have a nonce origin and  
hence should use a NullPrincipal.  
  

### contentPolicyType ###
  
The contentPolicyType of the channel, used for security checks  
like Mixed Content Blocking and Content Security Policy.  
  

## Constants ##

### SEC_NORMAL ###
  
No special security flags:  
  

### SEC_FORCE_INHERIT_PRINCIPAL ###
  
Force inheriting of the Principal. The resulting resource will use the  
principal of the document which is doing the load. Setting this flag  
will cause GetChannelResultPrincipal to return the same principal as  
the loading principal that's passed in when creating the channel.  
  
This will happen independently of the scheme of the URI that the  
channel is loading.  
  
So if the loading document comes from "http://a.com/", and the channel  
is loading the URI "http://b.com/whatever", GetChannelResultPrincipal  
will return a principal from "http://a.com/".  
  
This flag can not be used together with SEC_SANDBOXED.  
  

### SEC_SANDBOXED ###
  
Sandbox the load. The resulting resource will use a freshly created  
null principal. So GetChannelResultPrincipal will always return a  
null principal whenever this flag is set.  
  
This will happen independently of the scheme of the URI that the  
channel is loading.  
  
This flag can not be used together with SEC_FORCE_INHERIT_PRINCIPAL.  
  
